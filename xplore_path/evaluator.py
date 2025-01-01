import math
from dataclasses import dataclass
from enum import Enum
from itertools import product
from typing import Any, Callable, Type

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from xplore_path.invocable import Invocable
from xplore_path.invocables.count_invocable import CountInvocable
from xplore_path.invocables.distinct_invocable import DistinctInvocable
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.invocables.whitespace_collapse_invocable import WhitespaceCollapseInvocable
from xplore_path.invocables.whitespace_remove_invocable import WhitespaceRemoveInvocable
from xplore_path.invocables.whitespace_strip_invocable import WhitespaceStripInvocable
from xplore_path.matchers.ignore_case_matcher import IgnoreCaseMatcher
from xplore_path.matchers.numeric_range_matcher import NumericRangeMatcher
from xplore_path.XplorePathGrammarLexer import XplorePathGrammarLexer
from xplore_path.XplorePathGrammarParser import XplorePathGrammarParser
from xplore_path.XplorePathGrammarVisitor import XplorePathGrammarVisitor
from xplore_path.paths.filesystem.filesystem_path import FileSystemPath, FileSystemPathContext
from xplore_path.path import Path
from xplore_path.paths.mirror.mirror_path import MirrorPath
from xplore_path.paths.python_object.python_object_path import PythonObjectPath
from xplore_path.coercer_fallback import CoercerFallback
from xplore_path.coercer_fallbacks.default_coercer_fallback import DefaultCoercerFallback
from xplore_path.coercer_fallbacks.discard_coercer_fallback import DiscardCoercerFallback
from xplore_path.coercer_fallbacks.fail_coercer_fallback import FailCoerecerFallback
from xplore_path.coercions import coerce_single_value, coerce_to_list, coerce_for_set_operation
from xplore_path.matcher import Matcher
from xplore_path.matchers.combined_matcher import CombinedMatcher
from xplore_path.matchers.fuzzy_matcher import FuzzyMatcher
from xplore_path.matchers.glob_matcher import GlobMatcher
from xplore_path.matchers.regex_matcher import RegexMatcher
from xplore_path.matchers.strict_matcher import StrictMatcher
from xplore_path.matchers.wildcard_matcher import WildcardMatcher
from xplore_path.paths.simple.simple_path import SimplePath
from xplore_path.raise_parse_error_listener import RaiseParseErrorListener


class PrimeMode(Enum):
    PRIME_WITH_ROOT = 'PRIME_WITH_ROOT'
    PRIME_WITH_SELF = 'PRIME_WITH_SELF'
    PRIME_WITH_EMPTY = 'PRIME_WITH_EMPTY'


EntityType = Path | int | float | str | bool | Matcher


@dataclass
class _EvaluatorVisitorContext:
    original_root: Path
    entities: list[EntityType]
    entities_save_stack: list[list[EntityType]]
    variables: dict[str, Any]

    def __post_init__(self):
        if self.original_root.full_label() != [None]:
            raise ValueError('Root path in context not root path')

    def __contains__(self, item):
        return item in self.entities

    def __iter__(self):
        return iter(self.entities)

    def __getitem__(self, index):
        return self.entities[index]

    def reset_entities(self, new_entities: PrimeMode | list[EntityType]):
        if isinstance(new_entities, list):
            self.entities = new_entities
        elif new_entities == PrimeMode.PRIME_WITH_ROOT:
            self.entities = [self.original_root]
        elif new_entities == PrimeMode.PRIME_WITH_SELF:
            self.entities = self.entities_save_stack[-1][:]  # copy
        elif new_entities == PrimeMode.PRIME_WITH_EMPTY:
            self.entities = []
        else:
            raise ValueError('This should never happen')

    def save_entities(self, new_paths: PrimeMode | list[EntityType]):
        self.entities_save_stack.append(self.entities)
        self.reset_entities(new_paths)

    def restore_entities(self) -> list[EntityType]:
        current_paths = self.entities
        self.entities = self.entities_save_stack.pop()
        return current_paths

    def add_entity(self, entity: EntityType):
        self.entities.append(entity)

    @staticmethod
    def prime(
            root_: EntityType,
            variables_: dict[str, Any]
    ):
        return _EvaluatorVisitorContext(
            original_root=root_,
            entities=[root_],
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
            coercer_fallback = self.visit(ctx.coerceFallback())
        else:
            coercer_fallback = DiscardCoercerFallback()
        inner = self.visit(ctx.atomicOrEncapsulate())
        if ctx.MINUS():
            if type(inner) == list:
                inner = [coerce_single_value(v, float) for v in inner]
                inner = coercer_fallback.coerce(inner)
                inner = [-v for v in inner]
                return inner
            else:
                inner = [coerce_single_value(inner, float)]
                inner = coercer_fallback.coerce(inner)
                inner = [-v for v in inner]
                if inner:
                    return inner[0]
                else:
                    return []
        elif ctx.PLUS():
            return inner  # Keep it as-is -- not required to do any manipulation here
        raise ValueError('Unexpected')

    def visitExprAtomicOrEncapsulate(self, ctx: XplorePathGrammarParser.ExprAtomicOrEncapsulateContext):
        return self.visit(ctx.atomicOrEncapsulate())

    def visitExprFunctionCall(self, ctx: XplorePathGrammarParser.ExprFunctionCallContext):
        if ctx.coerceFallback():
            coercer_fallback = self.visit(ctx.coerceFallback())
        else:
            coercer_fallback = DiscardCoercerFallback()

        def op(_invocable, _args):
            if isinstance(_invocable, Invocable):
                try:
                    return _invocable.invoke(_args)
                except Exception:
                    ...  # do nothing
            return None

        invocable = self.visit(ctx.atomicOrEncapsulate())
        args = [self.visit(n) for n in ctx.argumentList().atomicOrEncapsulate()]
        if type(invocable) == list:
            ret = [op(i, args) for i in invocable]
            ret = coercer_fallback.coerce(ret)
            return ret
        else:
            ret = [op(invocable, args)]
            ret = coercer_fallback.coerce(ret)
            if ret:
                return ret[0]
            else:
                return []

    # TODO: Deeply inefficient - rework this to properly index before joining based on the condition. For example, if
    #       condition is == and both operands are known to be hashable, then create hash table and use that for quick
    #       lookup. Likewise, if relational operator (e.g. > or <=) and operands support sorting, sort and lookup using
    #       binary search.
    #
    #       Maybe, instead of passing around lists of Paths (and singular values), create a Sequence class that holds
    #       these values. The Sequence class can generate an index (e.g. hash or sorted) based on the values within the
    #       sequence.
    def visitExprJoin(self, ctx: XplorePathGrammarParser.ExprJoinContext):
        def _create_join_obj(l_item, r_item):
            test_path = SimplePath(None, None, None)
            mirrored_l_item = MirrorPath(l_item, test_path, 1) if isinstance(l_item, Path) else l_item
            mirrored_r_item = MirrorPath(r_item, test_path, 2) if isinstance(r_item, Path) else r_item
            test_path.add_child(mirrored_l_item)
            test_path.add_child(mirrored_r_item)
            return test_path

        def _create_join_obj_left_only(l_item):
            test_path = SimplePath(None, None, None)
            mirrored_l_item = MirrorPath(l_item, test_path, 1) if isinstance(l_item, Path) else l_item
            test_path.add_child(mirrored_l_item)
            return test_path

        def _create_join_obj_right_only(r_item):
            test_path = SimplePath(None, None, None)
            mirrored_r_item = MirrorPath(r_item, test_path, 2) if isinstance(r_item, Path) else r_item
            test_path.add_child(mirrored_r_item)
            return test_path

        l = coerce_to_list(self.visit(ctx.expr(0)))
        r = coerce_to_list(self.visit(ctx.expr(1)))
        matching_paths = []
        if ctx.joinOp().KW_INNER():
            for l_item in l:
                for r_item in r:
                    test_path = _create_join_obj(l_item, r_item)
                    entities = [test_path]
                    entities = self._apply_filter(entities, ctx.joinCond().filter_())
                    if entities != []:
                        matching_paths.append(test_path)
        elif ctx.joinOp().KW_RIGHT():
            matching_paths = []
            for r_item in r:
                joined = False
                for l_item in l:
                    test_path = _create_join_obj(l_item, r_item)
                    entities = [test_path]
                    entities = self._apply_filter(entities, ctx.joinCond().filter_())
                    if entities != []:
                        matching_paths.append(test_path)
                if not joined:
                    matching_paths.append(_create_join_obj_right_only(r_item))
        else:  # if KW_LEFT not set explicitly, assume KW_LEFT
            matching_paths = []
            for l_item in l:
                joined = False
                for r_item in r:
                    test_path = _create_join_obj(l_item, r_item)
                    entities = [test_path]
                    entities = self._apply_filter(entities, ctx.joinCond().filter_())
                    if entities != []:
                        matching_paths.append(test_path)
                if not joined:
                    matching_paths.append(_create_join_obj_left_only(l_item))
        return matching_paths

    def visitExprConcatenate(self, ctx: XplorePathGrammarParser.ExprConcatenateContext):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        return coerce_to_list(l) + coerce_to_list(r)

    def visitExprSetIntersect(self, ctx: XplorePathGrammarParser.ExprSetIntersectContext):
        l = coerce_for_set_operation(self.visit(ctx.expr(0)))
        r = coerce_for_set_operation(self.visit(ctx.expr(1)))
        if ctx.KW_INTERSECT():
            result_keys = l.keys() & r.keys()
        elif ctx.KW_EXCEPT():
            result_keys = l.keys() - r.keys()
        else:
            raise ValueError('Unexpected')
        return [l[p] for p in result_keys]

    def visitExprSetUnion(self, ctx: XplorePathGrammarParser.ExprSetUnionContext):
        l = coerce_for_set_operation(self.visit(ctx.expr(0)))
        r = coerce_for_set_operation(self.visit(ctx.expr(1)))
        result = l | r
        return list(result.values())

    def visitExprBoolAggregate(self, ctx: XplorePathGrammarParser.ExprBoolAggregateContext):
        if ctx.coerceFallback():
            coercer_fallback = self.visit(ctx.coerceFallback())
        else:
            coercer_fallback = DefaultCoercerFallback(False)
        if ctx.KW_ANY():
            op = any
        elif ctx.KW_ALL():
            op = all
        else:
            raise ValueError('Unexpected')
        r = self.visit(ctx.expr())
        if type(r) == list:
            r = [coerce_single_value(v, bool) for v in r]
            r = coercer_fallback.coerce(r)
            return op(r)
        else:
            r = [coerce_single_value(r, bool)]
            r = coercer_fallback.coerce(r)
            return op(r)

    def _apply_binary_arithmetic_op(
            self,
            l: int | float | str | bool | list[Any],
            r: int | float | str | bool | list[Any],
            combine_op: Callable[[Any, Any], Any],
            op: Callable[[Any, Any], Any],
            expected_type: Type[bool | int | float | str],
            coercer_fallback: CoercerFallback
    ):
        if isinstance(l, list) and isinstance(r, list):
            l = coercer_fallback.coerce([coerce_single_value(v, expected_type) for v in l])
            r = coercer_fallback.coerce([coerce_single_value(v, expected_type) for v in r])
            return [op(l_, r_) for l_, r_ in combine_op(l, r)]
        elif isinstance(l, list):
            l = coercer_fallback.coerce([coerce_single_value(v, expected_type) for v in l])
            r = coercer_fallback.coerce([coerce_single_value(r, expected_type)])
            return [op(l_, r_) for l_, r_ in combine_op(l, r)]
        elif isinstance(r, list):
            l = coercer_fallback.coerce([coerce_single_value(l, expected_type)])
            r = coercer_fallback.coerce([coerce_single_value(v, expected_type) for v in r])
            return [op(l_, r_) for l_, r_ in combine_op(l, r)]
        else:
            l = coercer_fallback.coerce([coerce_single_value(l, expected_type)])
            r = coercer_fallback.coerce([coerce_single_value(r, expected_type)])
            single_or_empty = [op(l_, r_) for l_, r_ in combine_op(l, r)]
            return single_or_empty[0] if single_or_empty else []

    def visitExprMultiplicative(self, ctx: XplorePathGrammarParser.ExprMultiplicativeContext):
        if ctx.coerceFallback():
            coercer_fallback = self.visit(ctx.coerceFallback())
        else:
            coercer_fallback = DiscardCoercerFallback()
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        # default to zip if both are lists, otherwise use product as default - that's what xpath does
        combine_op = zip if type(l) == list and type(r) == list else product
        if ctx.mulOp().KW_ZIP():
            combine_op = zip
        elif ctx.mulOp().KW_PRODUCT():
            combine_op = product
        if ctx.mulOp().STAR():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l * _r, float, coercer_fallback)
        elif ctx.mulOp().KW_DIV():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l / _r, float, coercer_fallback)
        elif ctx.mulOp().KW_IDIV():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l // _r, float, coercer_fallback)
        elif ctx.mulOp().KW_MOD():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l % _r, float, coercer_fallback)
        raise ValueError('Unexpected')

    def visitExprAdditive(self, ctx: XplorePathGrammarParser.ExprAdditiveContext):
        if ctx.coerceFallback():
            coercer_fallback = self.visit(ctx.coerceFallback())
        else:
            coercer_fallback = DiscardCoercerFallback()
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        # default to zip if both are lists, otherwise use product as default - that's what xpath does
        combine_op = zip if type(l) == list and type(r) == list else product
        if ctx.addOp().KW_ZIP():
            combine_op = zip
        elif ctx.addOp().KW_PRODUCT():
            combine_op = product
        if ctx.addOp().PLUS():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l + _r, float, coercer_fallback)
        elif ctx.addOp().MINUS():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l - _r, float, coercer_fallback)
        elif ctx.addOp().PP():
            return self._apply_binary_arithmetic_op(l, r, combine_op, lambda _l, _r: _l + _r, str, coercer_fallback)
        raise ValueError('Unexpected')

    def visitExprExtractLabel(self, ctx: XplorePathGrammarParser.ExprExtractLabelContext):
        l = self.visit(ctx.expr())
        if type(l) is list:
            return [l_.label() for l_ in l if isinstance(l_, Path)]
        elif isinstance(l, Path):
            return l.label()
        return []

    def _apply_binary_boolean_op(
            self,
            l: int | float | str | bool | list[Any],
            r: int | float | str | bool | list[Any],
            combine_op: Callable[[Any, Any], Any],
            test_op: Callable[[Any, Any], Any],
            required_type: Type | None,
            coercer_fallback: CoercerFallback
    ):
        def _coerce_eval_insert(ret, l_, r_):
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
            # Append
            if l_ is None or r_ is None:
                ret.append(None)
            else:
                ret.append(test_op(l_, r_))

        if isinstance(l, list) and isinstance(r, list):  # list vs list - what happens depends on mode
            ret = []
            for l_, r_ in combine_op(l, r):
                _coerce_eval_insert(ret, l_, r_)
            return coercer_fallback.coerce(ret)
        elif isinstance(l, list): # for each comparison regardless of mode
            ret = []
            for l_ in l:
                _coerce_eval_insert(ret, l_, r)
            return coercer_fallback.coerce(ret)
        elif isinstance(r, list):  # for each comparison regardless of mode
            ret = []
            for r_ in r:
                _coerce_eval_insert(ret, l, r_)
            return coercer_fallback.coerce(ret)
        else:  # single comparison regardless of mode
            ret = []
            _coerce_eval_insert(ret, l, r)
            ret = coercer_fallback.coerce(ret)
            return ret[0] if ret else []

    def visitExprComparison(self, ctx: XplorePathGrammarParser.ExprComparisonContext):
        if ctx.coerceFallback():
            coercer_fallback = self.visit(ctx.coerceFallback())
        else:
            coercer_fallback = DefaultCoercerFallback(False)
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
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, required_type, coercer_fallback)  # noqa
        agg_op, ret = self._boolean_op_aggregator(ctx.relOp(), ret)
        ret = agg_op(ret)
        return ret

    def visitExprOr(self, ctx: XplorePathGrammarParser.ExprAndContext):
        if ctx.coerceFallback():
            coercer_fallback = self.visit(ctx.coerceFallback())
        else:
            coercer_fallback = DefaultCoercerFallback(False)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = lambda _l, _r: _l or _r
        combine_op = self._boolean_op_combiner(ctx.orOp())
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, bool, coercer_fallback)  # noqa
        agg_op, ret = self._boolean_op_aggregator(ctx.orOp(), ret)
        ret = agg_op(ret)
        return ret

    def visitExprAnd(self, ctx: XplorePathGrammarParser.ExprAndContext):
        if ctx.coerceFallback():
            coercer_fallback = self.visit(ctx.coerceFallback())
        else:
            coercer_fallback = DefaultCoercerFallback(False)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = lambda _l, _r: _l and _r
        combine_op = self._boolean_op_combiner(ctx.andOp())
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, bool, coercer_fallback)  # noqa
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
            ret = coerce_to_list(ret)
            agg_op = all
        elif ctx.KW_SEQUENCE():  # keep as-is
            agg_op = lambda x: x
        else:  # if ctx.KW_ANY or no agg was explicitly specified (in which case it should default to ANY)
            ret = coerce_to_list(ret)
            agg_op = any
        return agg_op, ret

    def visitExprWrap(self, ctx: XplorePathGrammarParser.ExprWrapContext):
        entities = self.visit(ctx.expr())
        if ctx.filter_():
            entities = self._apply_filter(entities, ctx.filter_())
        return entities

    def visitExprWrapForceList(self, ctx: XplorePathGrammarParser.ExprWrapForceListContext):
        entities = []
        if ctx.expr():
            entities = coerce_to_list(self.visit(ctx.expr()))
            if ctx.filter_():
                entities = self._apply_filter(entities, ctx.filter_())
        return entities

    def visitPathFromRoot(self, ctx: XplorePathGrammarParser.PathFromRootContext):
        try:
            self.context.save_entities(new_paths=PrimeMode.PRIME_WITH_ROOT)
            return self.visit(ctx.relPath())
        finally:
            self.context.restore_entities()

    def visitPathRootExact(self, ctx: XplorePathGrammarParser.PathRootExactContext):
        try:
            self.context.save_entities(new_paths=PrimeMode.PRIME_WITH_ROOT)
            return self.context.entities[:]
        finally:
            self.context.restore_entities()

    def visitPathFromAny(self, ctx: XplorePathGrammarParser.PathFromAnyContext):
        try:
            self.context.save_entities(new_paths=PrimeMode.PRIME_WITH_ROOT)
            root = self.context.entities[0]
            self.context.entities = [root] + root.all_descendants()
            return [root] + self.visit(ctx.relPath())
        finally:
            self.context.restore_entities()

    def visitPathFromRelative(self, ctx: XplorePathGrammarParser.PathFromRelativeContext):
        try:
            self.context.save_entities(new_paths=PrimeMode.PRIME_WITH_SELF)
            return self.visit(ctx.relPath())
        finally:
            self.context.restore_entities()

    def visitPathSelf(self, ctx: XplorePathGrammarParser.PathSelfContext):
        return self.context.entities[:]

    def visitPathParent(self, ctx: XplorePathGrammarParser.PathParentContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                parent_path = e.parent()
                if parent_path is not None:
                    new_paths.append(parent_path)
        return new_paths

    def visitRelPathChain(self, ctx: XplorePathGrammarParser.RelPathChainContext):
        # TODO: Pushing / popping state not required?
        try:
            self.context.save_entities(PrimeMode.PRIME_WITH_SELF)
            new_paths = []
            if ctx.SLASH():
                left_contexts = self.visit(ctx.relPath(0))
                for left_path in left_contexts:
                    self.context.save_entities([left_path])
                    right_contexts = self.visit(ctx.relPath(1))
                    for right_path in right_contexts:
                        new_paths.append(right_path)
                    self.context.restore_entities()
            elif ctx.SS():
                left_contexts = []
                for e in self.visit(ctx.relPath(0)):
                    left_contexts.append(e)
                    left_contexts += e.all_descendants()
                for left_path in left_contexts:
                    self.context.save_entities([left_path])
                    right_contexts = self.visit(ctx.relPath(1))
                    for right_path in right_contexts:
                        new_paths.append(right_path)
                    self.context.restore_entities()
            else:
                raise ValueError('Unexpected')
            return new_paths
        finally:
            self.context.restore_entities()

    def visitRelPathStep(self, ctx: XplorePathGrammarParser.RelPathStepContext):
        if ctx.forwardStep():
            ret = self.visit(ctx.forwardStep())
        elif ctx.reverseStep():
            ret = self.visit(ctx.reverseStep())
        else:
            raise ValueError('Unexpected')
        return ret

    def visitReverseStepParent(self, ctx: XplorePathGrammarParser.ReverseStepParentContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                parent_path = e.parent()
                if parent_path is not None:
                    new_paths.append(parent_path)
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepAncestor(self, ctx: XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.all_ancestors()
        new_paths = new_paths[::-1]
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepPreceding(self, ctx: XplorePathGrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.preceding()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepPrecedingSibling(self, ctx: XplorePathGrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.preceding_sibling()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepAncestorOrSelf(self, ctx: XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths.append(e)
                new_paths += e.all_ancestors()
        new_paths = new_paths[::-1]
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepDirectParent(self, ctx: XplorePathGrammarParser.ReverseStepDirectParentContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                parent_path = e.parent()
                if parent_path is not None:
                    new_paths.append(parent_path)
        return new_paths

    def visitForwardStepChild(self, ctx: XplorePathGrammarParser.ForwardStepChildContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.all_children()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDescendant(self, ctx: XplorePathGrammarParser.ForwardStepDescendantContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.all_descendants()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepSelf(self, ctx: XplorePathGrammarParser.ForwardStepSelfContext):
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDescendantOrSelf(self, ctx: XplorePathGrammarParser.ForwardStepDescendantOrSelfContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths.append(e)
                new_paths += e.all_descendants()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepFollowingSibling(self, ctx: XplorePathGrammarParser.ForwardStepFollowingSiblingContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.following_sibling()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepFollowing(self, ctx: XplorePathGrammarParser.ForwardStepFollowingContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.following()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepValue(self, ctx: XplorePathGrammarParser.ForwardStepValueContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.all_children()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDirectSelf(self, ctx: XplorePathGrammarParser.ForwardStepDirectSelfContext):
        return self.context.entities[:]  # Return existing

    def _walk_down(self, result: Any):
        to_matcher = lambda v: v if isinstance(v, Matcher) else StrictMatcher(v)
        matchers = []
        if isinstance(result, list):
            for v in result:
                if isinstance(v, Path):
                    v = v.value()
                matchers.append(to_matcher(v))
        else:
            matchers.append(to_matcher(result))
        # test
        combined_matcher = CombinedMatcher(matchers)
        ret = []
        for e in self.context:
            if isinstance(e, Path):
                label = e.label()
            else:
                label = e
            if combined_matcher.match(label):
                ret.append(e)
        return ret

    def _apply_filter(self, entities: list[EntityType], ctx: XplorePathGrammarParser.FilterContext):
        self.context.save_entities(PrimeMode.PRIME_WITH_EMPTY)
        try:
            ret = []
            for idx, e in enumerate(entities):
                self.context.reset_entities([e])
                result = self.visit(ctx.expr())
                # /a/b[bool] - return if true
                # /a/b[int]  - return if coerces to true (non-zero + not nan)
                # /a/b[str]  - return if coerces to true (non-empty)
                # /a/b[list] - return if any coerce to true? (in original xpath it returns true if non-empty)
                if (type(result) == bool and result == True) \
                        or (type(result) == list and any(coerce_single_value(v, bool) for v in result)) \
                        or (type(result) in {float, int} and result == idx) \
                        or (type(result) == str and result == coerce_single_value(e, str)):
                    ret.append(e)
            return ret
        finally:
            self.context.restore_entities()

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
        elif ctx.BooleanLiteral():
            return ctx.getText() == 'true'
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
            return DiscardCoercerFallback()
        elif ctx.KW_FAIL():
            return FailCoerecerFallback()
        elif ctx.expr():
            res = self.visit(ctx.expr())
            if type(res) == list:
                if len(res) == 0:
                    return DiscardCoercerFallback()
                else:
                    res = res[0]
            return DefaultCoercerFallback(res)
        raise ValueError('Unexpected')


def evaluate(
        root: EntityType,
        expr: str,
        variables: dict[str, Any] | None = None
) -> list[Any] | Any:
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
        'whitespace_remove': WhitespaceRemoveInvocable()
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
            root: EntityType,
            expr: str
    ):
        return evaluate(root, expr, self.variables)


def _test(root_obj, expr):
    return _test_with_path(PythonObjectPath.create_root_path(root_obj), expr)


def _test_with_fs_path(dir, expr):
    print(f'---- res for {expr}')
    fs_path = FileSystemPath.create_root_path(
        dir,
        FileSystemPathContext(
            cache_notifier=lambda notice_type, real_path: print(f'{notice_type}: {real_path}')
        )
    )
    ret = Evaluator().evaluate(fs_path, expr)
    if isinstance(ret, list):
        for v in ret:
            print(f'  {v}')
        return ret
    else:
        print(f'  {ret}')

def _test_with_path(p, expr):
    print(f'---- res for {expr}')
    ret = Evaluator().evaluate(p, expr)
    if isinstance(ret, list):
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
    # _test_with_fs_path('~/Downloads', "($frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'))[. >= 5]")  # doesn't work, should filter to >= 5 counts
    # _test_with_fs_path('~/Downloads', "$whitespace_collapse(['hello    world', 'hello world', 'helloworld'])")
    # _test_with_fs_path('~/Downloads', "$whitespace_remove(['hello    world', 'hello world', 'helloworld'])")
    # _test_with_fs_path('~/Downloads', "$whitespace_strip([' hello world ', ' hello world', 'hello world '])")
