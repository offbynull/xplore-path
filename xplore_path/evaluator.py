import math
from dataclasses import dataclass
from enum import Enum
from itertools import product
from typing import Any, Callable, Type

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from xplore_path.XPath31GrammarLexer import XPath31GrammarLexer
from xplore_path.XPath31GrammarParser import XPath31GrammarParser
from xplore_path.XPath31GrammarVisitor import XPath31GrammarVisitor
from xplore_path.paths.filesystem_path import FileSystemPath
from xplore_path.path.path import Path
from xplore_path.paths.python_object_path import PythonObjectPath
from xplore_path.coercer_fallback.coercer_fallback import CoercerFallback
from xplore_path.coercer_fallbacks.default_coercer_fallback import DefaultCoercerFallback
from xplore_path.coercer_fallbacks.discard_coercer_fallback import DiscardCoercerFallback
from xplore_path.coercer_fallbacks.fail_coercer_fallback import FailCoerecerFallback
from xplore_path.coercions import coerce_single_value, coerce_to_list, coerce_for_set_operation
from xplore_path.label_matcher.label_matcher import LabelMatcher
from xplore_path.label_matchers.combined_label_matcher import CombinedLabelMatcher
from xplore_path.label_matchers.fuzzy_label_matcher import FuzzyLabelMatcher
from xplore_path.label_matchers.glob_label_matcher import GlobLabelMatcher
from xplore_path.label_matchers.regex_label_matcher import RegexLabelMatcher
from xplore_path.label_matchers.strict_label_matcher import StrictLabelMatcher
from xplore_path.label_matchers.wildcard_label_matcher import WildcardLabelMatcher
from xplore_path.raise_parse_error_listener import RaiseParseErrorListener


class PrimeMode(Enum):
    PRIME_WITH_ROOT = 'PRIME_WITH_ROOT'
    PRIME_WITH_SELF = 'PRIME_WITH_SELF'
    PRIME_WITH_EMPTY = 'PRIME_WITH_EMPTY'

EntityType = Path | int | float | str | bool | LabelMatcher

@dataclass
class Context:
    original_root: Path
    entities: list[EntityType]
    entities_save_stack: list[list[EntityType]]

    def __post_init__(self):
        if self.original_root.full_label() != [None]:
            raise ValueError('Root path in context not root path')

    def __add__(self, other):
        return Context(self.original_root, self.entities + other.entities, [])

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
    def prime(root_: EntityType):
        return Context(
            original_root=root_,
            entities=[root_],
            entities_save_stack=[]
        )







class PathEvaluatorVisitor(XPath31GrammarVisitor):
    def __init__(self, root: Any):
        self.root = root
        self.context = Context.prime(root)
        self.context_save_stack = []

    def visitXplorepath(self, ctx: XPath31GrammarParser.XplorepathContext):
        return self.visit(ctx.expr())

    def visitExprPath(self, ctx: XPath31GrammarParser.ExprPathContext):
        entities = self.visit(ctx.path())
        if ctx.filter_():
            entities = self._apply_filter(entities, ctx.filter_())
        return entities

    def visitExprLiteral(self, ctx: XPath31GrammarParser.ExprLiteralContext):
        return self.visit(ctx.literal())

    def visitExprVariable(self, ctx: XPath31GrammarParser.ExprVariableContext):
        raise ValueError('Variables not supported yet')

    def visitExprUnary(self, ctx: XPath31GrammarParser.ExprUnaryContext):
        if ctx.coerecefallback():
            coercer_fallback = self.visit(ctx.coerecefallback())
        else:
            coercer_fallback = DiscardCoercerFallback()
        inner = self.visit(ctx.atomicorencapsulate())
        if ctx.MINUS() is not None:
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
        elif ctx.PLUS() is not None:
            return inner  # Keep it as-is -- not required to do any manipulation here

    def visitExprAtomicOrEncapsulate(self, ctx: XPath31GrammarParser.ExprAtomicOrEncapsulateContext):
        return self.visit(ctx.atomicorencapsulate())

    def visitExprConcatenate(self, ctx: XPath31GrammarParser.ExprConcatenateContext):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        return coerce_to_list(l) + coerce_to_list(r)

    def visitExprSetIntersect(self, ctx: XPath31GrammarParser.ExprSetIntersectContext):
        l = coerce_for_set_operation(self.visit(ctx.expr(0)))
        r = coerce_for_set_operation(self.visit(ctx.expr(1)))
        intersected = l.keys() & r.keys()
        return [l[p] for p in intersected]

    def visitExprSetUnion(self, ctx: XPath31GrammarParser.ExprSetUnionContext):
        l = coerce_for_set_operation(self.visit(ctx.expr(0)))
        r = coerce_for_set_operation(self.visit(ctx.expr(1)))
        unioned = l | r
        return list(unioned.values())

    def visitExprBoolAggregate(self, ctx: XPath31GrammarParser.ExprBoolAggregateContext):
        if ctx.coerecefallback():
            coercer_fallback = self.visit(ctx.coerecefallback())
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

    def _apply_binary_number_op(
            self,
            l: int | float | str | bool | list[Any],
            r: int | float | str | bool | list[Any],
            combine_op: Callable[[Any, Any], Any],
            op: Callable[[Any, Any], Any],
            coercer_fallback: CoercerFallback
    ):
        if isinstance(l, list) and isinstance(r, list):
            l = coercer_fallback.coerce([coerce_single_value(v, float) for v in l])
            r = coercer_fallback.coerce([coerce_single_value(v, float) for v in r])
            return [op(l_, r_) for l_, r_ in combine_op(l, r)]
        elif isinstance(l, list):
            l = coercer_fallback.coerce([coerce_single_value(v, float) for v in l])
            r = coercer_fallback.coerce([coerce_single_value(r, float)])
            return [op(l_, r_) for l_, r_ in combine_op(l, r)]
        elif isinstance(r, list):
            l = coercer_fallback.coerce([coerce_single_value(l, float)])
            r = coercer_fallback.coerce([coerce_single_value(v, float) for v in r])
            return [op(l_, r_) for l_, r_ in combine_op(l, r)]
        else:
            l = coercer_fallback.coerce([coerce_single_value(l, float)])
            r = coercer_fallback.coerce([coerce_single_value(r, float)])
            single_or_empty = [op(l_, r_) for l_, r_ in combine_op(l, r)]
            return single_or_empty[0] if single_or_empty else []

    def visitExprMultiplicative(self, ctx: XPath31GrammarParser.ExprMultiplicativeContext):
        if ctx.coerecefallback():
            coercer_fallback = self.visit(ctx.coerecefallback())
        else:
            coercer_fallback = DiscardCoercerFallback()
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        # default to zip if both are lists, otherwise use product as default - that's what xpath does
        combine_op = zip if type(l) == list and type(r) == list else product
        if ctx.mulop().KW_ZIP():
            combine_op = zip
        elif ctx.mulop().KW_PRODUCT():
            combine_op = product
        if ctx.mulop().STAR() is not None:
            return self._apply_binary_number_op(l, r, combine_op, lambda _l, _r: _l * _r, coercer_fallback)
        elif ctx.mulop().KW_DIV() is not None:
            return self._apply_binary_number_op(l, r, combine_op, lambda _l, _r: _l / _r, coercer_fallback)
        elif ctx.mulop().KW_IDIV() is not None:
            return self._apply_binary_number_op(l, r, combine_op, lambda _l, _r: _l // _r, coercer_fallback)
        elif ctx.mulop().KW_MOD() is not None:
            return self._apply_binary_number_op(l, r, combine_op, lambda _l, _r: _l % _r, coercer_fallback)
        raise ValueError('Unexpected')

    def visitExprAdditive(self, ctx: XPath31GrammarParser.ExprAdditiveContext):
        if ctx.coerecefallback():
            coercer_fallback = self.visit(ctx.coerecefallback())
        else:
            coercer_fallback = DiscardCoercerFallback()
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        # default to zip if both are lists, otherwise use product as default - that's what xpath does
        combine_op = zip if type(l) == list and type(r) == list else product
        if ctx.addop().KW_ZIP():
            combine_op = zip
        elif ctx.addop().KW_PRODUCT():
            combine_op = product
        if ctx.addop().PLUS() is not None:
            return self._apply_binary_number_op(l, r, combine_op, lambda _l, _r: _l + _r, coercer_fallback)
        elif ctx.addop().MINUS() is not None:
            return self._apply_binary_number_op(l, r, combine_op, lambda _l, _r: _l - _r, coercer_fallback)
        raise ValueError('Unexpected')

    def visitExprRange(self, ctx: XPath31GrammarParser.ExprRangeContext):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if type(l) is list and len(l) > 0:
            l = l[0]
        if type(r) is list and len(r) > 0:
            r = r[0]
        l = coerce_single_value(l, int)
        r = coerce_single_value(r, int)
        if l is None or r is None:
            return []
        return [v for v in range(l, r+1)]

    def visitExprExtractLabel(self, ctx: XPath31GrammarParser.ExprExtractLabelContext):
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

    def visitExprComparison(self, ctx: XPath31GrammarParser.ExprComparisonContext):
        if ctx.coerecefallback():
            coercer_fallback = self.visit(ctx.coerecefallback())
        else:
            coercer_fallback = DefaultCoercerFallback(False)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if ctx.relop().EQ():
            op = lambda _l, _r: _l == _r
            numerics_required = None
        elif ctx.relop().NE():
            op = lambda _l, _r: _l != _r
            numerics_required = None
        elif ctx.relop().LT():
            op = lambda _l, _r: _l < _r
            numerics_required = float
        elif ctx.relop().LE():
            op = lambda _l, _r: _l <= _r
            numerics_required = float
        elif ctx.relop().GT():
            op = lambda _l, _r: _l > _r
            numerics_required = float
        elif ctx.relop().GE():
            op = lambda _l, _r: _l >= _r
            numerics_required = float
        elif ctx.relop().LL():
            raise ValueError('Test if node A is before node B - unimplemented')
        elif ctx.relop().GG():
            raise ValueError('Test if node A is after node B - unimplemented')
        else:
            raise ValueError('Unexpected')
        combine_op = self._boolean_op_combiner(ctx.relop())
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, numerics_required, coercer_fallback)  # noqa
        agg_op, ret = self._boolean_op_aggregator(ctx.relop(), ret)
        ret = agg_op(ret)
        return ret

    def visitExprOr(self, ctx: XPath31GrammarParser.ExprAndContext):
        if ctx.coerecefallback():
            coercer_fallback = self.visit(ctx.coerecefallback())
        else:
            coercer_fallback = DefaultCoercerFallback(False)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = lambda _l, _r: _l or _r
        combine_op = self._boolean_op_combiner(ctx.orop())
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, bool, coercer_fallback)  # noqa
        agg_op, ret = self._boolean_op_aggregator(ctx.orop(), ret)
        ret = agg_op(ret)
        return ret

    def visitExprAnd(self, ctx: XPath31GrammarParser.ExprAndContext):
        if ctx.coerecefallback():
            coercer_fallback = self.visit(ctx.coerecefallback())
        else:
            coercer_fallback = DefaultCoercerFallback(False)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = lambda _l, _r: _l and _r
        combine_op = self._boolean_op_combiner(ctx.andop())
        ret = self._apply_binary_boolean_op(l, r, combine_op, op, bool, coercer_fallback)  # noqa
        agg_op, ret = self._boolean_op_aggregator(ctx.andop(), ret)
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

    def visitExprWrap(self, ctx: XPath31GrammarParser.ExprWrapContext):
        entities = self.visit(ctx.expr())
        if ctx.filter_():
            entities = self._apply_filter(entities, ctx.filter_())
        return entities

    def visitExprWrapForceList(self, ctx: XPath31GrammarParser.ExprWrapForceListContext):
        entities = []
        if ctx.expr():
            entities = coerce_to_list(self.visit(ctx.expr()))
            if ctx.filter_():
                entities = self._apply_filter(entities, ctx.filter_())
        return entities

    def visitPathFromRoot(self, ctx: XPath31GrammarParser.PathFromRootContext):
        try:
            self.context.save_entities(new_paths=PrimeMode.PRIME_WITH_ROOT)
            return self.visit(ctx.relpath())
        finally:
            self.context.restore_entities()

    def visitPathRootExact(self, ctx: XPath31GrammarParser.PathRootExactContext):
        try:
            self.context.save_entities(new_paths=PrimeMode.PRIME_WITH_ROOT)
            return self.context.entities[:]
        finally:
            self.context.restore_entities()

    def visitPathFromAny(self, ctx: XPath31GrammarParser.PathFromAnyContext):
        try:
            self.context.save_entities(new_paths=PrimeMode.PRIME_WITH_ROOT)
            self.context.entities = self.context.entities[0].all_descendants()
            return self.visit(ctx.relpath())
        finally:
            self.context.restore_entities()

    def visitPathFromRelative(self, ctx: XPath31GrammarParser.PathFromRelativeContext):
        try:
            self.context.save_entities(new_paths=PrimeMode.PRIME_WITH_SELF)
            return self.visit(ctx.relpath())
        finally:
            self.context.restore_entities()

    def visitPathSelf(self, ctx: XPath31GrammarParser.PathSelfContext):
        return self.context.entities[:]

    def visitPathParent(self, ctx: XPath31GrammarParser.PathParentContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                parent_path = e.parent()
                if parent_path is not None:
                    new_paths.append(parent_path)
        return new_paths

    def visitRelPathChain(self, ctx: XPath31GrammarParser.RelPathChainContext):
        # TODO: Pushing / popping state not required?
        try:
            self.context.save_entities(PrimeMode.PRIME_WITH_SELF)
            new_paths = []
            if ctx.SLASH() is not None:
                left_contexts = self.visit(ctx.relpath(0))
                for left_path in left_contexts:
                    self.context.save_entities([left_path])
                    right_contexts = self.visit(ctx.relpath(1))
                    for right_path in right_contexts:
                        new_paths.append(right_path)
                    self.context.restore_entities()
            elif ctx.SS() is not None:
                left_contexts = []
                for e in self.visit(ctx.relpath(0)):
                    left_contexts.append(e)
                    left_contexts += e.all_descendants()
                for left_path in left_contexts:
                    self.context.save_entities([left_path])
                    right_contexts = self.visit(ctx.relpath(1))
                    for right_path in right_contexts:
                        new_paths.append(right_path)
                    self.context.restore_entities()
            else:
                raise ValueError('Unexpected')
            return new_paths
        finally:
            self.context.restore_entities()

    def visitRelPathStep(self, ctx: XPath31GrammarParser.RelPathStepContext):
        if ctx.forwardstep() is not None:
            ret = self.visit(ctx.forwardstep())
        elif ctx.reversestep() is not None:
            ret = self.visit(ctx.reversestep())
        else:
            raise ValueError('Unexpected')
        if len(ctx.argumentlist()) > 0:
            raise ValueError('IMPLEMENT ME')
        return ret

    def visitReverseStepParent(self, ctx: XPath31GrammarParser.ReverseStepParentContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                parent_path = e.parent()
                if parent_path is not None:
                    new_paths.append(parent_path)
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitReverseStepAncestor(self, ctx: XPath31GrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.all_ancestors()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitReverseStepPreceding(self, ctx: XPath31GrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.preceding()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitReverseStepPrecedingSibling(self, ctx: XPath31GrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.preceding_sibling()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitReverseStepAncestorOrSelf(self, ctx: XPath31GrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths.append(e)
                new_paths += e.all_ancestors()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitReverseStepDirectParent(self, ctx: XPath31GrammarParser.ReverseStepDirectParentContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                parent_path = e.parent()
                if parent_path is not None:
                    new_paths.append(parent_path)
        return new_paths

    def visitForwardStepChild(self, ctx: XPath31GrammarParser.ForwardStepChildContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.all_children()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitForwardStepDescendant(self, ctx: XPath31GrammarParser.ForwardStepDescendantContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.all_descendants()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitForwardStepSelf(self, ctx: XPath31GrammarParser.ForwardStepSelfContext):
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitForwardStepDescendantOrSelf(self, ctx: XPath31GrammarParser.ForwardStepDescendantOrSelfContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths.append(e)
                new_paths += e.all_descendants()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitForwardStepFollowingSibling(self, ctx: XPath31GrammarParser.ForwardStepFollowingSiblingContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.following_sibling()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitForwardStepFollowing(self, ctx: XPath31GrammarParser.ForwardStepFollowingContext):
        new_paths = []
        for e in self.context:
            if isinstance(e, Path):
                new_paths += e.following()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitForwardStepValue(self, ctx: XPath31GrammarParser.ForwardStepValueContext):
        new_paths = []
        for e in self.context.entities:
            if isinstance(e, Path):
                new_paths += e.all_children()
        self.context.reset_entities(new_paths)
        return self._walk_down(self.visit(ctx.atomicorencapsulate()))

    def visitForwardStepDirectSelf(self, ctx: XPath31GrammarParser.ForwardStepDirectSelfContext):
        return self.context.entities[:]  # Return existing

    def _walk_down(self, result: Any):
        to_matcher = lambda v: v if isinstance(v, LabelMatcher) else StrictLabelMatcher(v)
        matchers = []
        if isinstance(result, list):
            for v in result:
                if isinstance(v, Path):
                    v = v.value()
                matchers.append(to_matcher(v))
        else:
            matchers.append(to_matcher(result))
        # test
        combined_matcher = CombinedLabelMatcher(matchers)
        ret = []
        for e in self.context:
            if isinstance(e, Path):
                label = e.label()
            else:
                label = e
            if combined_matcher.match(label):
                ret.append(e)
        return ret

    def _apply_filter(self, entities: list[EntityType], ctx: XPath31GrammarParser.FilterContext):
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

    def visitLiteral(self, ctx: XPath31GrammarParser.LiteralContext):
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

    def visitExprMatcher(self, ctx: XPath31GrammarParser.ExprMatcherContext):
        return self.visit(ctx.matcher())

    def visitMatcherStrict(self, ctx: XPath31GrammarParser.MatcherStrictContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return StrictLabelMatcher(pattern)

    def visitMatcherRegex(self, ctx: XPath31GrammarParser.MatcherRegexContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return RegexLabelMatcher(pattern)

    def visitMatcherGlob(self, ctx: XPath31GrammarParser.MatcherGlobContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return GlobLabelMatcher(pattern)

    def visitMatcherFuzzy(self, ctx: XPath31GrammarParser.MatcherGlobContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return FuzzyLabelMatcher(pattern)

    def visitMatcherWildcard(self, ctx: XPath31GrammarParser.MatcherWildcardContext):
        return WildcardLabelMatcher()

    def visitCoerecefallback(self, ctx: XPath31GrammarParser.CoerecefallbackContext):
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


def evaluate(root: EntityType, expr: str):
    input_stream = InputStream(expr)
    lexer = XPath31GrammarLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(RaiseParseErrorListener())
    token_stream = CommonTokenStream(lexer)
    parser = XPath31GrammarParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(RaiseParseErrorListener())
    tree = parser.xplorepath()
    visitor = PathEvaluatorVisitor(root)
    return tree.accept(visitor)


def _test(root_obj, expr):
    return _test_with_path(PythonObjectPath.create_root_path(root_obj), expr)


def _test_with_path(p, expr):
    print(f'---- res for {expr}')
    ret = evaluate(p, expr)
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

    # _test_with_path(FileSystemPath.create_root_path('~'), '/*')
    # _test_with_path(FileSystemPath.create_root_path('~'), '/test.json//*')
    # _test_with_path(FileSystemPath.create_root_path('~'), '/test.json/address/city')
    # _test_with_path(FileSystemPath.create_root_path('~'), '/test.xml//*')
    # _test_with_path(FileSystemPath.create_root_path('~'), '/test.yaml//*')
    # _test_with_path(FileSystemPath.create_root_path('~'), '/test.csv/*/Name')
    # _test_with_path(FileSystemPath.create_root_path('~'), '/test.csv/*/Name[. = "John Doe"]')
    # _test_with_path(FileSystemPath.create_root_path('~'), '/test.csv/*')
    _test_with_path(FileSystemPath.create_root_path('~'), '/test.csv/*[./Name = "John Doe"]')
    # _test_with_path(FileSystemPath.create_root_path('~'), '(/test.csv/*)[./Name/r"J.*"]')