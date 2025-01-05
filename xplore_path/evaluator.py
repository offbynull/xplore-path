import cProfile
import itertools
import math
from dataclasses import dataclass
from enum import Enum
from itertools import product
from typing import Any, Callable, Type, Literal, Hashable

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from xplore_path.invocable import Invocable
from xplore_path.invocables.count_invocable import CountInvocable
from xplore_path.invocables.distinct_invocable import DistinctInvocable
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.invocables.regex_extract_invocable import RegexExtractInvocable
from xplore_path.invocables.whitespace_collapse_invocable import WhitespaceCollapseInvocable
from xplore_path.invocables.whitespace_remove_invocable import WhitespaceRemoveInvocable
from xplore_path.invocables.whitespace_strip_invocable import WhitespaceStripInvocable
from xplore_path.matchers.ignore_case_matcher import IgnoreCaseMatcher
from xplore_path.matchers.numeric_range_matcher import NumericRangeMatcher
from xplore_path.XplorePathGrammarLexer import XplorePathGrammarLexer
from xplore_path.XplorePathGrammarParser import XplorePathGrammarParser
from xplore_path.XplorePathGrammarVisitor import XplorePathGrammarVisitor
from xplore_path.paths.filesystem.filesystem_path import FileSystemPath
from xplore_path.paths.filesystem.context import FileSystemContext
from xplore_path.path import Path
from xplore_path.paths.mirror.mirror_path import MirrorPath
from xplore_path.paths.python_object.python_object_path import PythonObjectPath
from xplore_path.coercions import coerce_single_value
from xplore_path.matcher import Matcher
from xplore_path.matchers.combined_matcher import CombinedMatcher
from xplore_path.matchers.fuzzy_matcher import FuzzyMatcher
from xplore_path.matchers.glob_matcher import GlobMatcher
from xplore_path.matchers.regex_matcher import RegexMatcher
from xplore_path.matchers.strict_matcher import StrictMatcher
from xplore_path.matchers.wildcard_matcher import WildcardMatcher
from xplore_path.paths.simple.simple_path import SimplePath
from xplore_path.raise_parse_error_listener import RaiseParseErrorListener
from xplore_path.sequence import Sequence, SingleWrapSequence, TransformSequence, FullSequence, FallbackMode, \
    DiscardFallbackMode, ErrorFallbackMode, DefaultFallbackMode, EmptySequence, FilterSequence, \
    SingleOrSequenceWrapSequence, DoNothingFallbackMode


class PathResetMode(Enum):
    RESET_WITH_ROOT = 'RESET_WITH_ROOT'
    RESET_WITH_SELF = 'RESET_WITH_SELF'
    RESET_WITH_EMPTY = 'RESET_WITH_EMPTY'


class RootResetMode(Enum):
    RESET_WITH_SELF = 'RESET_WITH_SELF'


@dataclass
class _EvaluatorVisitorContext:
    root: Path
    entities: Sequence
    entities_save_stack: list[Sequence]
    variables: dict[str, Any]

    def __post_init__(self):
        if self.root.full_label() != [None]:
            raise ValueError('Root path in context not root path')

    def reset_entities(self, new_entities: PathResetMode | Sequence):
        if isinstance(new_entities, Sequence):
            self.entities = new_entities
        elif new_entities == PathResetMode.RESET_WITH_ROOT:
            self.entities = [self.root]
        elif new_entities == PathResetMode.RESET_WITH_SELF:
            self.entities = self.entities  # Normally it'd be a copy of the self.entities, but Sequences should be immutable
        elif new_entities == PathResetMode.RESET_WITH_EMPTY:
            self.entities = []
        else:
            raise ValueError('This should never happen')

    def save(self, new_paths: PathResetMode | Sequence, new_root: RootResetMode | Any = RootResetMode.RESET_WITH_SELF):
        self.entities_save_stack.append((self.entities, self.root))
        if new_root != RootResetMode.RESET_WITH_SELF:
            self.root = new_root
        self.reset_entities(new_paths)

    def restore(self) -> Sequence:
        current_paths = self.entities
        self.entities, self.root = self.entities_save_stack.pop()
        return current_paths

    @staticmethod
    def prime(
            root_: Path | Any,
            variables_: dict[str, Any]
    ):
        return _EvaluatorVisitorContext(
            root=root_,
            entities=SingleWrapSequence(root_),
            entities_save_stack=[],
            variables=variables_
        )


class _EvaluatorVisitor(XplorePathGrammarVisitor):
    def __init__(
            self,
            root: Any,
            variables: dict[str, Any]
    ):
        self.root = root
        self.context = _EvaluatorVisitorContext.prime(root, variables)

    def visitXplorePath(self, ctx: XplorePathGrammarParser.XplorePathContext):
        return self.visit(ctx.expr())

    def visitExprPath(self, ctx: XplorePathGrammarParser.ExprPathContext):
        entities = self.visit(ctx.path())
        if ctx.filter_():
            entities = self._apply_filter(entities, ctx.filter_())
        return entities

    def visitExprLiteral(self, ctx: XplorePathGrammarParser.ExprLiteralContext):
        return self.visit(ctx.literal())

    def visitExprVariable(self, ctx: XplorePathGrammarParser.ExprVariableContext):
        if ctx.varRef().Name():
            name = ctx.varRef().Name().getText()
        elif ctx.varRef().IntegerLiteral():
            name = str(ctx.varRef().IntegerLiteral().getText())
        elif ctx.varRef().StringLiteral():
            name = self._decode_str(ctx.varRef().StringLiteral().getText())
        else:
            raise ValueError('Unexpected')

        return self.context.variables.get(name, None)

    def visitExprUnary(self, ctx: XplorePathGrammarParser.ExprUnaryContext):
        if ctx.coerceFallback():
            fallback = self.visit(ctx.coerceFallback())
        else:
            fallback = DiscardFallbackMode()
        inner = self.visit(ctx.atomicOrEncapsulate())
        if ctx.MINUS():
            if isinstance(inner, Sequence):
                inner = TransformSequence(inner, lambda _, v: coerce_single_value(v, float), fallback)
                inner = TransformSequence(inner, lambda _, v: -v, DoNothingFallbackMode())
                return inner
            else:
                inner = SingleWrapSequence(inner)
                inner = TransformSequence(inner, lambda _, v: coerce_single_value(v, float), fallback)
                inner = TransformSequence(inner, lambda _, v: -v, DoNothingFallbackMode())
                if inner:
                    return next(iter(inner))
                else:
                    return EmptySequence()
        elif ctx.PLUS():
            return inner  # Keep it as-is -- not required to do any manipulation here
        raise ValueError('Unexpected')

    def visitExprAtomicOrEncapsulate(self, ctx: XplorePathGrammarParser.ExprAtomicOrEncapsulateContext):
        return self.visit(ctx.atomicOrEncapsulate())

    def visitExprFunctionCall(self, ctx: XplorePathGrammarParser.ExprFunctionCallContext):
        if ctx.coerceFallback():
            fallback = self.visit(ctx.coerceFallback())
        else:
            fallback = DiscardFallbackMode()

        def op(_invocable, _args):
            if isinstance(_invocable, Invocable):
                try:
                    return _invocable.invoke(_args)
                except Exception:
                    ...  # do nothing
            return None

        invocable = self.visit(ctx.atomicOrEncapsulate())
        args = [self.visit(n) for n in ctx.argumentList().expr()]
        if isinstance(invocable, Sequence):
            ret = TransformSequence(invocable, lambda _, i: op(i, args), fallback)
            return ret
        else:
            ret = SingleWrapSequence(invocable)
            ret = TransformSequence(ret, lambda _, i: op(i, args), fallback)
            if ret:
                return next(iter(ret))
            else:
                return EmptySequence()

    # TODO: Deeply inefficient - rework this to properly index before joining based on the condition. For example, if
    #       condition is == and both operands are known to be hashable, then create hash table and use that for quick
    #       lookup. Likewise, if relational operator (e.g. > or <=) and operands support sorting, sort and lookup using
    #       binary search.
    #
    #       Maybe, instead of passing around lists of Paths (and singular values), create a Sequence class that holds
    #       these values. The Sequence class can generate an index (e.g. hash or sorted) based on the values within the
    #       sequence.
    def visitExprJoin(self, ctx: XplorePathGrammarParser.ExprJoinContext):
        def _create_join_obj(parent, parent_idx, l_item, r_item):
            test_path = SimplePath(parent, parent_idx, 'joined', None)
            if isinstance(l_item, Path):
                l_path = SimplePath(test_path, 0, 'l', None)
                l_path.add_child(
                    MirrorPath(l_item, l_path, 0)
                )
            else:
                l_path = SimplePath(test_path, 0, 'l', l_item)
            l_path.seal()
            test_path.add_child(l_path)
            if isinstance(r_item, Path):
                r_path = SimplePath(test_path, 1, 'r', None)
                r_path.add_child(
                    MirrorPath(r_item, r_path, 0)
                )
            else:
                r_path = SimplePath(test_path, 1, 'r', r_item)
            r_path.seal()
            test_path.add_child(r_path)
            test_path.seal()
            return test_path

        def _create_join_obj_left_only(parent, parent_idx, l_item):
            test_path = SimplePath(parent, parent_idx, 'joined', None)
            if isinstance(l_item, Path):
                l_path = SimplePath(test_path, 0, 'l', None)
                l_path.add_child(
                    MirrorPath(l_item, l_path, 0)
                )
            else:
                l_path = SimplePath(test_path, 0, 'l', l_item)
            l_path.seal()
            test_path.add_child(l_path)
            test_path.seal()
            return test_path

        def _create_join_obj_right_only(parent, parent_idx, r_item):
            test_path = SimplePath(parent, parent_idx, 'joined', None)
            if isinstance(r_item, Path):
                r_path = SimplePath(test_path, 0, 'r', None)
                r_path.add_child(
                    MirrorPath(r_item, r_path, 0)
                )
            else:
                r_path = SimplePath(test_path, 0, 'r', r_item)
            r_path.seal()
            test_path.add_child(r_path)
            test_path.seal()
            return test_path

        l = SingleOrSequenceWrapSequence(self.visit(ctx.expr(0)))
        r = SingleOrSequenceWrapSequence(self.visit(ctx.expr(1)))
        root_path = SimplePath(None, None, None, None)
        root_path_next_child_idx = 0
        if ctx.joinOp().KW_INNER():
            for l_item in l:
                for r_item in r:
                    test_path = _create_join_obj(root_path, root_path_next_child_idx, l_item, r_item)
                    entities = SingleWrapSequence(test_path)
                    self.context.save(entities, test_path)
                    try:
                        entities = self._apply_filter(entities, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if entities:
                        root_path.add_child(test_path)
                        root_path_next_child_idx += 1
        elif ctx.joinOp().KW_RIGHT():
            for r_item in r:
                joined = False
                for l_item in l:
                    test_path = _create_join_obj(root_path, root_path_next_child_idx, l_item, r_item)
                    entities = SingleWrapSequence(test_path)
                    self.context.save(entities, test_path)
                    try:
                        entities = self._apply_filter(entities, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if entities:
                        root_path.add_child(test_path)
                        root_path_next_child_idx += 1
                        joined = True
                if not joined:
                    r_path = _create_join_obj_right_only(root_path, root_path_next_child_idx, r_item)
                    root_path.add_child(r_path)
                    root_path_next_child_idx += 1
        else:  # if KW_LEFT not set explicitly, assume KW_LEFT
            for l_item in l:
                joined = False
                for r_item in r:
                    test_path = _create_join_obj(root_path, root_path_next_child_idx, l_item, r_item)
                    entities = SingleWrapSequence(test_path)
                    self.context.save(entities, test_path)
                    try:
                        entities = self._apply_filter(entities, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if entities:
                        root_path.add_child(test_path)
                        root_path_next_child_idx += 1
                        joined = True
                if not joined:
                    l_path = _create_join_obj_left_only(root_path, root_path_next_child_idx, l_item)
                    root_path.add_child(l_path)
                    root_path_next_child_idx += 1
        root_path.seal()
        return FullSequence([root_path] + root_path.all_descendants())

    def visitExprSetIntersect(self, ctx: XplorePathGrammarParser.ExprSetIntersectContext):
        l = self._coerce_for_set_operation(self.visit(ctx.expr(0)))
        r = self._coerce_for_set_operation(self.visit(ctx.expr(1)))
        if ctx.KW_INTERSECT():
            result_keys = l.keys() & r.keys()
        elif ctx.KW_EXCEPT():
            result_keys = l.keys() - r.keys()
        else:
            raise ValueError('Unexpected')
        return FullSequence(l[p] for p in result_keys)

    def visitExprSetUnion(self, ctx: XplorePathGrammarParser.ExprSetUnionContext):
        l = self._coerce_for_set_operation(self.visit(ctx.expr(0)))
        r = self._coerce_for_set_operation(self.visit(ctx.expr(1)))
        result = l | r
        return FullSequence(result.values())

    def _coerce_for_set_operation(self, value: Any) -> dict[tuple[Literal['PATH', 'RAW'], Hashable], Any]:
        if not isinstance(value, Sequence):
            value = SingleWrapSequence(value)
        ret = {}
        for v in value:
            if isinstance(v, Path):
                k = 'PATH', tuple(v.full_label())
            else:
                k = 'RAW', v
            try:
                ret[k] = v
            except TypeError:
                ...  # type is unhashable? silently discard it and move on
        return ret  # noqa

    def visitExprBoolAggregate(self, ctx: XplorePathGrammarParser.ExprBoolAggregateContext):
        if ctx.coerceFallback():
            fallback = self.visit(ctx.coerceFallback())
        else:
            fallback = DefaultFallbackMode(False)
        if ctx.KW_ANY():
            op = any
        elif ctx.KW_ALL():
            op = all
        else:
            raise ValueError('Unexpected')
        r = self.visit(ctx.expr())
        if isinstance(r, Sequence):
            r = TransformSequence(r, lambda _, v: coerce_single_value(v, bool), fallback)
            return op(r)
        else:
            r = SingleWrapSequence(r)
            r = TransformSequence(r, lambda _, v: coerce_single_value(v, bool), fallback)
            return op(r)

    def _apply_binary_arithmetic_op(
            self,
            l: int | float | str | bool | list[Any],
            r: int | float | str | bool | list[Any],
            combine_op: Callable[[Any, Any], Any],
            op: Callable[[Any, Any], Any],
            expected_type: Type[bool | int | float | str],
            fallback: FallbackMode
    ):
        if isinstance(l, Sequence) and isinstance(r, Sequence):
            l = TransformSequence(l, lambda _, v: coerce_single_value(v, expected_type), fallback)
            r = TransformSequence(r, lambda _, v: coerce_single_value(v, expected_type), fallback)
            return FullSequence(op(l_, r_) for l_, r_ in combine_op(l, r))
        elif isinstance(l, Sequence):
            l = TransformSequence(l, lambda _, v: coerce_single_value(v, expected_type), fallback)
            r = TransformSequence(SingleWrapSequence(r), lambda _, v: coerce_single_value(v, expected_type), fallback)
            return FullSequence(op(l_, r_) for l_, r_ in combine_op(l, r))
        elif isinstance(r, Sequence):
            l = TransformSequence(SingleWrapSequence(l), lambda _, v: coerce_single_value(v, expected_type), fallback)
            r = TransformSequence(r, lambda _, v: coerce_single_value(v, expected_type), fallback)
            return FullSequence(op(l_, r_) for l_, r_ in combine_op(l, r))
        else:
            l = TransformSequence(SingleWrapSequence(l), lambda _, v: coerce_single_value(v, expected_type), fallback)
            r = TransformSequence(SingleWrapSequence(r), lambda _, v: coerce_single_value(v, expected_type), fallback)
            ret = FullSequence(op(l_, r_) for l_, r_ in combine_op(l, r))
            if ret:
                return next(iter(ret))
            else:
                return EmptySequence()

    def visitExprMultiplicative(self, ctx: XplorePathGrammarParser.ExprMultiplicativeContext):
        if ctx.coerceFallback():
            fallback = self.visit(ctx.coerceFallback())
        else:
            fallback = DiscardFallbackMode()
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        # default to zip if both are lists, otherwise use product as default - that's what xpath does
        combine_op = zip if isinstance(l, Sequence) and isinstance(r, Sequence) else product
        if ctx.mulOp().KW_ZIP():
            combine_op = lambda a,b: zip(a, b)
        elif ctx.mulOp().KW_PRODUCT():
            combine_op = lambda a,b: product(a, b)
        if ctx.mulOp().STAR():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l * _r, float, fallback)
        elif ctx.mulOp().KW_DIV():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l / _r, float, fallback)
        elif ctx.mulOp().KW_IDIV():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l // _r, float, fallback)
        elif ctx.mulOp().KW_MOD():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l % _r, float, fallback)
        raise ValueError('Unexpected')

    def visitExprAdditive(self, ctx: XplorePathGrammarParser.ExprAdditiveContext):
        if ctx.coerceFallback():
            fallback = self.visit(ctx.coerceFallback())
        else:
            fallback = DiscardFallbackMode()
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        # default to zip if both are lists, otherwise use product as default - that's what xpath does
        combine_op = zip if isinstance(l, Sequence) and isinstance(r, Sequence) else product
        if ctx.addOp().KW_ZIP():
            combine_op = lambda a,b: zip(a, b)
        elif ctx.addOp().KW_PRODUCT():
            combine_op = lambda a,b: product(a, b)
        if ctx.addOp().PLUS():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l + _r, float, fallback)
        elif ctx.addOp().MINUS():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l - _r, float, fallback)
        elif ctx.addOp().PP():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l + _r, str, fallback)
        raise ValueError('Unexpected')

    def visitExprExtractLabel(self, ctx: XplorePathGrammarParser.ExprExtractLabelContext):
        l = self.visit(ctx.expr())
        if isinstance(l, Sequence):
            ret = FilterSequence(l, lambda _, v: isinstance(v, Path))
            ret = TransformSequence(ret, lambda _, v: v.label(), DoNothingFallbackMode())
            return ret
        elif isinstance(l, Path):
            return l.label()
        return EmptySequence()

    def visitExprExtractPosition(self, ctx: XplorePathGrammarParser.ExprExtractPositionContext):
        l = self.visit(ctx.expr())
        if isinstance(l, Sequence):
            ret = FilterSequence(l, lambda _, v: isinstance(v, Path))
            ret = TransformSequence(ret, lambda _, v: v.position(), DoNothingFallbackMode())
            return ret
        elif isinstance(l, Path):
            return l.position()
        return EmptySequence()

    def _apply_binary_boolean_op(
            self,
            l: int | float | str | bool | Sequence,
            r: int | float | str | bool | Sequence,
            combine_op: Callable[[Any, Any], Any],
            test_op: Callable[[Any, Any], Any],
            required_type: Type | None,
            fallback: FallbackMode
    ):
        def _coerce_eval_insert(l_, r_):
            # Paths to values
            if isinstance(l_, Path):
                l_ = l_.value()
            if isinstance(r_, Path):
                r_ = r_.value()
            # Coerce to comparable types
            if required_type is not None:
                l_ = coerce_single_value(l_, required_type)  # noqa
                r_ = coerce_single_value(r_, required_type)  # noqa
            elif isinstance(l_, Matcher) or isinstance(r_, Matcher):
                ...  # skip cohersion if either is a label matcher
            else:
                new_r_ = coerce_single_value(r_, type(l_))
                if new_r_ is None:
                    new_l_ = coerce_single_value(l_, type(r_))
                    l_ = new_l_
                else:
                    r_ = new_r_
            if l_ is None or r_ is None:
                return None
            return test_op(l_, r_)

        if isinstance(l, Sequence) and isinstance(r, Sequence):  # list vs list - what happens depends on mode
            ret = FullSequence(_coerce_eval_insert(l_, r_) for l_, r_ in combine_op(l, r))
            ret = TransformSequence(ret, lambda _, v: v, fallback)
            return ret
        elif isinstance(l, Sequence): # for each comparison regardless of mode
            ret = FullSequence(_coerce_eval_insert(l_, r) for l_ in l)
            ret = TransformSequence(ret, lambda _, v: v, fallback)
            return ret
        elif isinstance(r, Sequence):  # for each comparison regardless of mode
            ret = FullSequence(_coerce_eval_insert(l, r_) for r_ in r)
            ret = TransformSequence(ret, lambda _, v: v, fallback)
            return ret
        else:  # single comparison regardless of mode
            ret = SingleWrapSequence(_coerce_eval_insert(l, r))
            ret = TransformSequence(ret, lambda _, v: v, fallback)
            return next(iter(ret)) if ret else EmptySequence()

    def visitExprComparison(self, ctx: XplorePathGrammarParser.ExprComparisonContext):
        if ctx.coerceFallback():
            fallback = self.visit(ctx.coerceFallback())
        else:
            fallback = DefaultFallbackMode(False)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        def eq_op(_l, _r):
            if isinstance(_l, Matcher):
                return _l.match(_r)
            elif isinstance(_r, Matcher):
                return _r.match(_l)
            # WHAT IF THEY'RE BOTH LABEL MATCHERS? ALWAYS RETURN FALSE?
            return _l == _r

        if ctx.relOp().EQ():
            op = eq_op
            required_type = None
        elif ctx.relOp().NE():
            op = lambda _l, _r: not eq_op(_l, _r)
            required_type = None
        elif ctx.relOp().LT():
            op = lambda _l, _r: _l < _r
            required_type = float
        elif ctx.relOp().LE():
            op = lambda _l, _r: _l <= _r
            required_type = float
        elif ctx.relOp().GT():
            op = lambda _l, _r: _l > _r
            required_type = float
        elif ctx.relOp().GE():
            op = lambda _l, _r: _l >= _r
            required_type = float
        elif ctx.relOp().LL():
            raise ValueError('Test if node A is before node B - unimplemented')
        elif ctx.relOp().GG():
            raise ValueError('Test if node A is after node B - unimplemented')
        else:
            raise ValueError('Unexpected')
        combine_op = self._boolean_op_combiner(ctx.relOp())
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, required_type, fallback)  # noqa
        agg_op, ret = self._boolean_op_aggregator(ctx.relOp(), ret)
        ret = agg_op(ret)
        return ret

    def visitExprOr(self, ctx: XplorePathGrammarParser.ExprAndContext):
        if ctx.coerceFallback():
            coercer = self.visit(ctx.coerceFallback())
        else:
            coercer = DefaultFallbackMode(False)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = lambda _l, _r: _l or _r
        combine_op = self._boolean_op_combiner(ctx.orOp())
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, bool, coercer)  # noqa
        agg_op, ret = self._boolean_op_aggregator(ctx.orOp(), ret)
        ret = agg_op(ret)
        return ret

    def visitExprAnd(self, ctx: XplorePathGrammarParser.ExprAndContext):
        if ctx.coerceFallback():
            coercer = self.visit(ctx.coerceFallback())
        else:
            coercer = DefaultFallbackMode(False)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = lambda _l, _r: _l and _r
        combine_op = self._boolean_op_combiner(ctx.andOp())
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, bool, coercer)  # noqa
        agg_op, ret = self._boolean_op_aggregator(ctx.andOp(), ret)
        ret = agg_op(ret)
        return ret

    def _boolean_op_combiner(self, ctx):
        combine_op = product  # default is product, override if set - product is default in xpath
        if ctx.KW_ZIP():
            combine_op = zip
        elif ctx.KW_PRODUCT():
            combine_op = product
        return combine_op

    def _boolean_op_aggregator(self, ctx, ret):
        if ctx.KW_ALL():
            ret = SingleOrSequenceWrapSequence(ret)
            agg_op = all
        elif ctx.KW_SEQUENCE():  # keep as-is
            agg_op = lambda x: x
        else:  # if ctx.KW_ANY or no agg was explicitly specified (in which case it should default to ANY)
            ret = SingleOrSequenceWrapSequence(ret)
            agg_op = any
        return agg_op, ret

    def visitExprWrap(self, ctx: XplorePathGrammarParser.ExprWrapContext):
        entities = self.visit(ctx.wrap())
        if ctx.filter_():
            entities = self._apply_filter(entities, ctx.filter_())
        return entities

    def visitExprWrapSingle(self, ctx: XplorePathGrammarParser.ExprWrapSingleContext):
        return self.visit(ctx.expr())

    def visitExprWrapSingleAsList(self, ctx: XplorePathGrammarParser.ExprWrapSingleAsListContext):
        return SingleOrSequenceWrapSequence(self.visit(ctx.expr()))

    def visitExprWrapConcatenateList(self, ctx: XplorePathGrammarParser.ExprWrapConcatenateListContext):
        entities = []
        for e in ctx.expr():
            entities.append(SingleOrSequenceWrapSequence(self.visit(e)))
        return FullSequence(itertools.chain(*entities), order_paths=False, deduplicate_paths=False)  # concatenation never dedupes/orders paths

    def visitExprEmptyList(self, ctx: XplorePathGrammarParser.ExprEmptyListContext):
        return EmptySequence()

    def visitPathAtRoot(self, ctx: XplorePathGrammarParser.PathAtRootContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_ROOT)
            new_entities = self.context.entities
            if ctx.filter_():
                new_entities = self._apply_filter(new_entities, ctx.filter_())
            return new_entities
        finally:
            self.context.restore()

    def visitPathFromRoot(self, ctx: XplorePathGrammarParser.PathFromRootContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_ROOT)
            new_entities = self.context.entities
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            self.context.entities = new_entities  # will not include p, only descendants of p
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromRootAny(self, ctx: XplorePathGrammarParser.PathFromRootAnyContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_EMPTY)
            root = self.context.root
            new_entities = FullSequence([root] + root.all_descendants())
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            self.context.entities = new_entities
            return self.visit(ctx.relPath())  # BUG: //* must return in document order, use position_in_parent of each path in the output to sort?
        finally:
            self.context.restore()

    def visitPathAtSelf(self, ctx: XplorePathGrammarParser.PathAtSelfContext):
        return self.context.entities

    def visitPathFromSelf(self, ctx: XplorePathGrammarParser.PathFromSelfContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_SELF)
            new_entities = self.context.entities
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            self.context.entities = new_entities
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromSelfAny(self, ctx: XplorePathGrammarParser.PathFromSelfAnyContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_SELF)
            new_entities = FullSequence(
                itertools.chain(*(p.all_descendants() for p in self.context.entities))
            )
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            self.context.entities = new_entities  # will not include p, only descendants of p
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathAtParent(self, ctx: XplorePathGrammarParser.PathAtParentContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_SELF)
            new_entities = [e.parent() for e in self.context.entities]
            new_entities = [e for e in new_entities if e is not None]
            new_entities = FullSequence(new_entities)
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            return new_entities
        finally:
            self.context.restore()

    def visitPathFromParent(self, ctx: XplorePathGrammarParser.PathFromParentContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_SELF)
            new_entities = [e.parent() for e in self.context.entities]
            new_entities = [e for e in new_entities if e is not None]
            new_entities = FullSequence(new_entities)
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            self.context.entities = new_entities
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromParentAny(self, ctx: XplorePathGrammarParser.PathFromParentAnyContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_SELF)
            new_entities = [e.parent() for e in self.context.entities]
            new_entities = [e for e in new_entities if e is not None]
            new_entities = FullSequence(
                itertools.chain(*(p.all_descendants() for p in new_entities))
            )
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            self.context.entities = new_entities  # will not include p's parent, only descendants of p's parent
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromNested(self, ctx: XplorePathGrammarParser.PathFromNestedContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_SELF)
            new_entities = self.visit(ctx.wrap())
            new_entities = [e for e in new_entities if isinstance(e, Path)]
            new_entities = FullSequence(new_entities)
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            self.context.entities = new_entities
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromNestedAny(self, ctx: XplorePathGrammarParser.PathFromNestedAnyContext):
        try:
            self.context.save(new_paths=PathResetMode.RESET_WITH_SELF)
            new_entities = self.visit(ctx.wrap())
            new_entities = [e for e in new_entities if isinstance(e, Path)]
            new_entities = FullSequence(
                itertools.chain(*([p] + p.all_descendants() for p in new_entities))
            )
            new_entities = self._apply_filter(new_entities, ctx.filter_())
            self.context.entities = new_entities
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitRelPathChain(self, ctx: XplorePathGrammarParser.RelPathChainContext):
        # TODO: Pushing / popping state not required?
        try:
            self.context.save(PathResetMode.RESET_WITH_SELF)
            new_paths = []
            if ctx.SLASH():
                left_contexts = self.visit(ctx.relPath(0))
                for left_path in left_contexts:
                    self.context.save(SingleWrapSequence(left_path))
                    right_contexts = self.visit(ctx.relPath(1))
                    for right_path in right_contexts:
                        new_paths.append(right_path)
                    self.context.restore()
            elif ctx.SS():
                left_contexts = []
                for e in self.visit(ctx.relPath(0)):
                    left_contexts.append(e)
                    left_contexts += e.all_descendants()
                for left_path in left_contexts:
                    self.context.save(SingleWrapSequence(left_path))
                    right_contexts = self.visit(ctx.relPath(1))
                    for right_path in right_contexts:
                        new_paths.append(right_path)
                    self.context.restore()
            else:
                raise ValueError('Unexpected')
            return FullSequence(new_paths)
        finally:
            self.context.restore()

    def visitRelPathStep(self, ctx: XplorePathGrammarParser.RelPathStepContext):
        if ctx.forwardStep():
            ret = self.visit(ctx.forwardStep())
        elif ctx.reverseStep():
            ret = self.visit(ctx.reverseStep())
        else:
            raise ValueError('Unexpected')
        if ctx.filter_():
            ret = self._apply_filter(ret, ctx.filter_())
        return ret

    def visitReverseStepParent(self, ctx: XplorePathGrammarParser.ReverseStepParentContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                parent_path = e.parent()
                if parent_path is not None:
                    new_paths.append(parent_path)
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepAncestor(self, ctx: XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.all_ancestors()
        new_paths = new_paths[::-1]
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepPreceding(self, ctx: XplorePathGrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.preceding()
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepPrecedingSibling(self, ctx: XplorePathGrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.preceding_sibling()
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepAncestorOrSelf(self, ctx: XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths.append(e)
                new_paths += e.all_ancestors()
        new_paths = new_paths[::-1]
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepDirectParent(self, ctx: XplorePathGrammarParser.ReverseStepDirectParentContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                parent_path = e.parent()
                if parent_path is not None:
                    new_paths.append(parent_path)
        return FullSequence(new_paths)

    def visitForwardStepChild(self, ctx: XplorePathGrammarParser.ForwardStepChildContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.all_children()
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDescendant(self, ctx: XplorePathGrammarParser.ForwardStepDescendantContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.all_descendants()
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepSelf(self, ctx: XplorePathGrammarParser.ForwardStepSelfContext):
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDescendantOrSelf(self, ctx: XplorePathGrammarParser.ForwardStepDescendantOrSelfContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths.append(e)
                new_paths += e.all_descendants()
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepFollowingSibling(self, ctx: XplorePathGrammarParser.ForwardStepFollowingSiblingContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.following_sibling()
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepFollowing(self, ctx: XplorePathGrammarParser.ForwardStepFollowingContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.following()
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepValue(self, ctx: XplorePathGrammarParser.ForwardStepValueContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.all_children()
        self.context.reset_entities(FullSequence(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDirectSelf(self, ctx: XplorePathGrammarParser.ForwardStepDirectSelfContext):
        return self.context.entities  # Return existing

    def _walk_down(self, result: Any):
        to_matcher = lambda v: v if isinstance(v, Matcher) else StrictMatcher(v)
        matchers = []
        if isinstance(result, Sequence):
            for v in result:
                if isinstance(v, Path):
                    v = v.value()
                matchers.append(to_matcher(v))
        else:
            matchers.append(to_matcher(result))
        # test
        combined_matcher = CombinedMatcher(matchers)
        ret = []
        for e in self.context.entities:
            if isinstance(e, Path):
                label = e.label()
            else:
                label = e
            if combined_matcher.match(label):
                ret.append(e)
        return FullSequence(ret)

    def _apply_filter(self, entities: Sequence, ctx: XplorePathGrammarParser.FilterContext | None):
        if ctx is None:
            return entities

        root = self.context.root  # explicitly get root for use in transformer, in case it changes by the time lazy evaluation takes place (it does when this is called by join condition)
                                  # -- simplest thing to do would be to not evaluate this lazily?
        def transformer(idx, e):
            self.context.save(
                SingleWrapSequence(e),
                root
            )
            try:
                result = self.visit(ctx.expr())
                if type(result) == bool and result == True:  # /a/b[bool] - return if true
                    return e
                elif type(result) in {float, int} and result == idx:  # /a/b[int] - return if index in the result set matches int
                    return e
                elif type(result) == NumericRangeMatcher and result.match(idx):  # /a/b[numericrangematcher] - return if index in the result set is in range
                    return e
                elif isinstance(result, Sequence) and result:  # /a/b[list] - return if non-empty (e.g. result was a list of paths looking for children, and some were found - e.g. /a/b[./c]
                    return e
                elif isinstance(result, Matcher) and not isinstance(e, Path) \
                        and result.match(e):  # (a,b,c)[matcher] - if list of non paths, matcher should match against value directly
                    return e
                elif isinstance(result, Matcher) and isinstance(e, Path) \
                        and any(result.match(c.label()) for c in e.all_children()):  # /a/b[matcher] - ir a path,  return if has child with name matching label, if numericrangematcher above didn't match, it might match now
                    return e
                elif type(result) in {str, int} and isinstance(e, Path) and any(
                        self._apply_binary_boolean_op(
                            l=FullSequence(c.label() for c in e.all_children()),
                            r=result,
                            combine_op=lambda a, b: zip(a, b),
                            test_op=lambda l, r: l == r,
                            required_type=None,
                            fallback=DiscardFallbackMode()
                        )
                ):  # /a/b[str_or_int]  - return if has child with label (coerced to match if possible)
                    # you don't want to do /a/b[bool] because bool can get coerced to 0 - imagine /a/b[./c = some_val], if b is a list (labels with 0, 1, 2, 3, ...) and ./c = some_val evaluates to False, that False will coerce to int=0 for comparison and it'll always be True on first element?
                    return e
                elif not isinstance(e, Path) and \
                        self._apply_binary_boolean_op(
                            l=e,
                            r=result,
                            combine_op=lambda a, b: zip(a, b),
                            test_op=lambda l, r: l == r,
                            required_type=None,
                            fallback=DiscardFallbackMode()
                        ):  # if not a path - return if values match (coerced to match if possible)
                    return e
                return None
            finally:
                self.context.restore()

        return TransformSequence(
            sequence=entities,
            transformer=transformer,
            fallback_mode=DiscardFallbackMode()
        )

    def _decode_str(self, text: str) -> str:
        mode = text[0]
        text_decoded = text[1:-1]
        if mode == '"':
            return text_decoded.replace('""', '"')
        elif mode == '\'':
            return text_decoded.replace('\'\'', '\'')
        else:
            raise ValueError('Unexpected')

    def visitLiteral(self, ctx: XplorePathGrammarParser.LiteralContext):
        if ctx.IntegerLiteral():
            return int(ctx.getText())
        elif ctx.DecimalLiteral():
            return float(ctx.getText())
        elif ctx.DoubleLiteral():
            return float(ctx.getText())
        elif ctx.StringLiteral():
            return self._decode_str(ctx.getText())
        elif ctx.KW_TRUE():
            return True
        elif ctx.KW_FALSE():
            return False
        elif ctx.KW_NAN():
            return math.nan
        elif ctx.KW_INF():
            return math.inf
        elif ctx.Name():
            return ctx.Name().getText()
        raise ValueError('Unexpected')

    def visitExprMatcher(self, ctx: XplorePathGrammarParser.ExprMatcherContext):
        return self.visit(ctx.matcher())

    def visitMatcherStrict(self, ctx: XplorePathGrammarParser.MatcherStrictContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return StrictMatcher(pattern)

    def visitMatcherRegex(self, ctx: XplorePathGrammarParser.MatcherRegexContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return RegexMatcher(pattern)

    def visitMatcherGlob(self, ctx: XplorePathGrammarParser.MatcherGlobContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return GlobMatcher(pattern)

    def visitMatcherFuzzy(self, ctx: XplorePathGrammarParser.MatcherGlobContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return FuzzyMatcher(pattern)

    def visitMatcherCaseInsensitive(self, ctx: XplorePathGrammarParser.MatcherCaseInsensitiveContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return IgnoreCaseMatcher(pattern)

    def visitMatcherNumericRange(self, ctx: XplorePathGrammarParser.MatcherNumericRangeContext):
        return self.visit(ctx.numericRangeMatcher())

    def visitMatcherWildcard(self, ctx: XplorePathGrammarParser.MatcherWildcardContext):
        return WildcardMatcher()

    def visitNumericRangeMatcherTolerance(self, ctx: XplorePathGrammarParser.NumericRangeMatcherToleranceContext):
        value = self.visit(ctx.numericRangeMatcherLiteral(0))
        if ctx.numericRangeMatcherLiteral(1):
            tolerance = self.visit(ctx.numericRangeMatcherLiteral(1))
        else:
            tolerance = 0.001
        min_ = value - tolerance
        max_ = value + tolerance
        return NumericRangeMatcher(min_, True, max_, True)

    def visitNumericRangeMatcherBounded(self, ctx: XplorePathGrammarParser.NumericRangeMatcherBoundedContext):
        min_ = self.visit(ctx.numericRangeMatcherLiteral(0))
        min_inclusive = bool(ctx.OB())
        max_ = self.visit(ctx.numericRangeMatcherLiteral(1))
        max_inclusive = bool(ctx.CB())
        return NumericRangeMatcher(min_, min_inclusive, max_, max_inclusive)

    def visitNumericRangeMatcherInclusive(self, ctx: XplorePathGrammarParser.NumericRangeMatcherInclusiveContext):
        min_ = self.visit(ctx.numericRangeMatcherLiteral(0))
        max_ = self.visit(ctx.numericRangeMatcherLiteral(1))
        return NumericRangeMatcher(min_, True, max_, True)

    def visitNumericRangeMatcherLiteral(self, ctx: XplorePathGrammarParser.NumericRangeMatcherLiteralContext):
        if ctx.IntegerLiteral():
            v = int(ctx.IntegerLiteral().getText())
        elif ctx.DecimalLiteral():
            v = float(ctx.DecimalLiteral().getText())
        elif ctx.DoubleLiteral():
            v = float(ctx.DoubleLiteral().getText())
        elif ctx.KW_INF():
            v = math.inf
        else:
            raise ValueError('Unexpected')
        if ctx.MINUS():
            v = -v
        return v

    def visitCoerceFallback(self, ctx: XplorePathGrammarParser.CoerceFallbackContext):
        if ctx.KW_DISCARD():
            return DiscardFallbackMode()
        elif ctx.KW_FAIL():
            return ErrorFallbackMode()
        elif ctx.expr():
            res = self.visit(ctx.expr())
            if isinstance(res, Sequence):
                try:
                    res = next(iter(res), None)
                    return DefaultFallbackMode(res)
                except StopIteration:
                    return DiscardFallbackMode()
            return DefaultFallbackMode(res)
        raise ValueError('Unexpected')


def evaluate(
        root: Any,
        expr: str,
        variables: dict[str, Any] | None = None
) -> Sequence | Any:
    if variables is None:
        variables = {}
    input_stream = InputStream(expr)
    lexer = XplorePathGrammarLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(RaiseParseErrorListener())
    token_stream = CommonTokenStream(lexer)
    parser = XplorePathGrammarParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(RaiseParseErrorListener())
    tree = parser.xplorePath()
    visitor = _EvaluatorVisitor(root, variables)
    return tree.accept(visitor)


class Evaluator:
    _DEFAULT_VARIABLES = {
        'distinct': DistinctInvocable(),
        'count': CountInvocable(),
        'frequency_count': FrequencyCountInvocable(),
        'whitespace_collapse': WhitespaceCollapseInvocable(),
        'whitespace_strip': WhitespaceStripInvocable(),
        'whitespace_remove': WhitespaceRemoveInvocable(),
        'regex_extract': RegexExtractInvocable()
    }

    def __init__(
            self,
            variables: dict[str, Any] | None = None
    ):
        if variables is None:
            variables = {}
        self.variables = Evaluator._DEFAULT_VARIABLES | variables  # same key? _DEFAULT_VARIABLES loses

    def evaluate(
            self,
            root: Any,
            expr: str
    ):
        return evaluate(root, expr, self.variables)


def _test(root_obj, expr):
    return _test_with_path(PythonObjectPath.create_root_path(root_obj), expr)


def _test_with_fs_path(dir, expr):
    print(f'---- res for {expr}')
    fs_path = FileSystemPath.create_root_path(
        dir,
        FileSystemContext(
            cache_notifier=lambda notice_type, real_path: print(f'{notice_type}: {real_path}')
        )
    )
    ret = Evaluator().evaluate(fs_path, expr)
    if isinstance(ret, Sequence):
        for v in ret:
            print(f'  {v}')
        return ret
    else:
        print(f'  {ret}')

def _test_with_path(p, expr):
    print(f'---- res for {expr}')
    ret = Evaluator().evaluate(p, expr)
    if isinstance(ret, Sequence):
        for v in ret:
            print(f'  {v}')
        return ret
    else:
        print(f'  {ret}')


if __name__ == '__main__':
    root = {'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}}
    # evaluate(root, '/')
    # evaluate(root, '/*')
    # test(root, '/a')
    # test(root, '/a/b')
    # test(root, '/a/*')
    # test(root, '/a/b/c')
    # test(root, '/a/b/d')
    # evaluate(root, '/a/b/*')
    # test(root, '/a/b/following::*')
    # test(root, '/a/b/following::z')
    # test(root, '/a/b/d/following-sibling::*')
    # test(root, '/a/b/d/following-sibling::f')
    # test(root, '/a/descendant-or-self::*')
    # test(root, '/a/descendant-or-self::d')
    # test(root, '/a/descendant::*')
    # test(root, '/a/descendant::d')
    # test(root, '/a/b/self::*')
    # test(root, '/a/b/self::d')
    # test(root, '/a/b/self::b')
    # test(root, '/a/b/child::*')
    # test(root, '/a/b/child::d')
    #
    # test(root, '/a/b/..')
    # test(root, '/a/b/e/ancestor-or-self::*')
    # test(root, '/a/b/e/ancestor-or-self::a')
    # test(root, '/y/preceding::*')
    # test(root, '/y/preceding::b')
    # test(root, '/y/preceding-sibling::*')
    # test(root, '/y/preceding-sibling::b')
    # test(root, '/a/b/e/parent::*')
    # test(root, '/a/b/e/parent::d')
    # test(root, '/a/b/e/parent::b')
    #
    # test(root, '/a/"b"')  # Test literal in path
    # test(root, '/a/"b"/./d')   # Test dot in path
    # test(root, '/a/b/*')  # Test looking up another path to walk forward
    # test(root, '/a/b/*[. = /ptrs/*]')  # Test looking up another path to walk forward

    # test(root, '-/a/b/*')
    # test(root, '-/*')

    # test(root, '/a/b/* , /a/b/*')
    # test(root, '/a/b/* , /y')

    # test(root, '/a/b/* intersect /a/b/*')
    # test(root, '/a/b/* intersect (/a/b/c, /a/b/e)')
    # test(root, '/a/b/* intersect /y')

    # test(root, '/a/b/* union /a/b/*')
    # test(root, '/a/b/* union (/a/b/c, /a/b/e)')
    # test(root, '/a/b/* union /y')

    # test(root, '/a/b/* + /a/b/*')
    # test(root, '/a/b/* + 1')
    # test(root, '/a/b/* + [1]')  # right is now a sequence - meaning only first elem is added
    # test(root, '/a/b/* + [1,2]')  # right is now a sequence - meaning only first elem is added
    # test(root, '5+4')

    # test(root, '5 to 7')
    # test(root, '5.0 to 7')
    # test(root, '5 to 7.0')
    # test(root, '5.0 to 7.0')
    # test(root, '5 to 5')
    # test(root, '5 to 4')

    # test(root, '/a/b[./d]')  # Get all children, so long as one of the children is d
    # test(root, '/a/b[./z]')  # Get all children, so long as one of the children is z
    # test(root, '/a/b/*[./self::d]')  # Get child with path label d
    # test(root, '/a/b/*[2]')  # Get child in 2nd position
    # test(root, '/a/b/*[. = 2]')  # Get child with value of 2
    # test(root, '[1,2,3] zip = [1,"2","bad"]')
    # test(root, '[1,2,3] zip any = [1,"2","bad"]')
    # test(root, '[1,2,3] zip all = [1,"2","bad"]')
    # test(root, '[1,2,3] product = [1,"2","bad"]')
    # test(root, '[1,2,3] = [1,"2","bad"]')

    # _test({}, '[] product all > 5')
    # _test({}, '5 product all > []')
    # _test({}, '-1 and true')
    # _test({}, '-1 and false')
    # _test(root, '[5,7,9][1]')
    # _test(root, '[5,7,9][. = 7]')
    # _test(root, '.')
    # _test(root, '/a')

    # _test_with_fs_path('~', '/*')
    # _test_with_fs_path('~', '/test.json//*')
    # _test_with_fs_path('~', '/test.json/address/city')
    # _test_with_fs_path('~', '/test.xml//*')
    # _test_with_fs_path('~', '/test.html//*')
    # _test_with_fs_path('~/Downloads', '/pycharm-community-2024.3.1.tar.gz/*')
    # _test_with_fs_path('~/Downloads', "/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/*/'Unnamed: 2'")
    # _test_with_fs_path('~/Downloads', "/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'//*")
    # _test_with_fs_path('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies//*")
    # _test_with_fs_path('~/Downloads', "2025 - (/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/*/'Unnamed: 2')")
    # _test_with_fs_path('~', '/test.yaml//*')
    # _test_with_fs_path('~', '/test.csv/*/Name')
    # _test_with_fs_path('~', '/test.csv/*/Name[. = "John Doe"]')
    # # _test_with_fs_path('~', '/test.csv/*')
    # _test_with_fs_path('~', '/test.csv/*[./Name = f"John Do"]')
    # _test_with_fs_path('~', '/test.csv/*[f"John Do" = ./Name]')
    # _test_with_fs_path('~', '/test.csv/*[r"J.*" = ./Name]')
    # _test_with_fs_path('~', '(/test.csv/*)[./Name/r"J.*"]')

    # _test_with_fs_path('~', '/Downloads/*')
    # _test_with_fs_path('~', '/Downloads/"parabilis.zip"/*')
    # _test_with_fs_path('~', '/Downloads/"parabilis.zip"/parabilis/*')
    # _test_with_fs_path('~', '/Downloads/"parabilis.zip"/parabilis/".idea"/*')
    # _test_with_fs_path('~', '/Downloads/"parabilis.zip"/parabilis/".idea"/modules.xml//*')

    # _test_with_fs_path('~/Downloads', "2025 - (/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/*/'Unnamed: 2')")
    # _test_with_fs_path('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 2'")
    # _test_with_fs_path('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/*[./'Unnamed: 2' = (2025 - (/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/*/'Unnamed: 2'))]")
    # _test_with_fs_path('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/* inner join /Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/* on [./1/'Unnamed: 2' = (2025 - ./2/'Unnamed: 2')]")  # Shows up as [None]: None  because value is none, but data is there under children
    # _test_with_fs_path('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/* left join /Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/* on [./1/'Unnamed: 2' = (2025 - ./2/'Unnamed: 2')]")  # Shows up as [None]: None  because value is none, but data is there under children
    # _test_with_fs_path('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/* right join /Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/* on [./1/'Unnamed: 2' = (2025 - ./2/'Unnamed: 2')]")  # Shows up as [None]: None  because value is none, but data is there under children
    # _test_with_fs_path('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'")
    # _test_with_fs_path('~/Downloads', "$count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3')")
    # _test_with_fs_path('~/Downloads', "$distinct(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3')")
    # _test_with_fs_path('~/Downloads', "$frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3')")
    # _test_with_fs_path('~/Downloads', "($frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'))/*")
    # _test_with_fs_path('~/Downloads', "($frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'))//*")
    # _test_with_fs_path('~/Downloads', "$distinct($regex_extract(/Fake_Mouse_Assays_200.zip/*/0/GO_Term, '\d{7}'))")
    # _test_with_fs_path('~/Downloads', "/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']/*")
    # _test_with_fs_path('~/Downloads', "$regex_extract(/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']/*, '\\d{7}')")
    _test_with_fs_path('~/Downloads', "$distinct(/Fake_Mouse_Assays_200.zip/*/0/GO_Term) inner join /goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*'] on [$regex_extract(//l, '\\d{7}') = $regex_extract(//r//id, '\\d{7}')]")
    # _test_with_fs_path('~/Downloads', "//*")
    # _test_with_fs_path('~/Downloads', "($frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'))[. >= 5]")  # doesn't work, should filter to >= 5 counts
    # _test_with_fs_path('~/Downloads', "$whitespace_collapse(['hello    world', 'hello world', 'helloworld'])")
    # _test_with_fs_path('~/Downloads', "$whitespace_remove(['hello    world', 'hello world', 'helloworld'])")
    # _test_with_fs_path('~/Downloads', "/uniprotkb_mouse_601_to_800_seqlen.json/results/*/genes[.//geneName/value = 'Zmat1']//geneName/value")

    # _test(root, '$regex_extract((hello, yellow, mellow), "low?")')

    # profiler = cProfile.Profile()
    # profiler.enable()
    # try:
    #     fs_path = FileSystemPath.create_root_path(
    #         '~/Downloads',
    #         FileSystemPathContext(
    #             cache_notifier=lambda notice_type, real_path: print(f'{notice_type}: {real_path}')
    #         )
    #     )
    #     ret = Evaluator().evaluate(fs_path, "/uniprotkb_mouse_601_to_800_seqlen.json/results//*[. = g'EC*']")
    #     print(f'{len(ret)=}')
    # except KeyboardInterrupt:
    #     ...
    # profiler.disable()
    # profiler.print_stats(sort='time')
