import itertools
import math
from enum import Enum
from typing import Any

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from xplore_path.XplorePathGrammarLexer import XplorePathGrammarLexer
from xplore_path.XplorePathGrammarParser import XplorePathGrammarParser
from xplore_path.XplorePathGrammarVisitor import XplorePathGrammarVisitor
from xplore_path.collection import Collection
from xplore_path.collection_utils import CombineMode, combine_transform_aggregate, AggregateMode
from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.collections_.single_value_collection import SingleValueCollection
from xplore_path.entity import Entity
from xplore_path.fallback_mode import FallbackMode
from xplore_path.fallback_modes.default_fallback_mode import DefaultFallbackMode
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.fallback_modes.error_fallback_mode import ErrorFallbackMode
from xplore_path.invocable import Invocable
from xplore_path.invocables.count_invocable import CountInvocable
from xplore_path.invocables.distinct_invocable import DistinctInvocable
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.invocables.regex_extract_invocable import RegexExtractInvocable
from xplore_path.invocables.whitespace_collapse_invocable import WhitespaceCollapseInvocable
from xplore_path.invocables.whitespace_remove_invocable import WhitespaceRemoveInvocable
from xplore_path.invocables.whitespace_strip_invocable import WhitespaceStripInvocable
from xplore_path.matcher import Matcher
from xplore_path.matchers.combined_matcher import CombinedMatcher
from xplore_path.matchers.fuzzy_matcher import FuzzyMatcher
from xplore_path.matchers.glob_matcher import GlobMatcher
from xplore_path.matchers.ignore_case_matcher import IgnoreCaseMatcher
from xplore_path.matchers.numeric_range_matcher import NumericRangeMatcher
from xplore_path.matchers.regex_matcher import RegexMatcher
from xplore_path.matchers.strict_matcher import StrictMatcher
from xplore_path.matchers.wildcard_matcher import WildcardMatcher
from xplore_path.null import Null
from xplore_path.path import Path, ParentBlock
from xplore_path.paths.filesystem.context import FileSystemContext
from xplore_path.paths.filesystem.filesystem_path import FileSystemPath
from xplore_path.paths.mirror.mirror_path import MirrorPath
from xplore_path.paths.python_object.python_object_path import PythonObjectPath
from xplore_path.paths.simple.simple_path import SimplePath
from xplore_path.raise_parse_error_listener import RaiseParseErrorListener


class CollectionResetMode(Enum):
    RESET_WITH_ROOT = 'RESET_WITH_ROOT'
    RESET_WITH_SELF = 'RESET_WITH_SELF'
    RESET_WITH_EMPTY = 'RESET_WITH_EMPTY'


class RootResetMode(Enum):
    RESET_WITH_SELF = 'RESET_WITH_SELF'


class _EvaluatorVisitorContext:
    def __init__(
            self,
            root: Path
    ):
        self._root = root
        self._collection = SequenceCollection.from_unpacked([root])
        self._save_stack = []
        self._variables = {}

    def __post_init__(self):
        if self._root.full_label() != []:
            raise ValueError('Root path in context not root path')

    def reset_collection(self, collection: CollectionResetMode | Collection):
        if isinstance(collection, Collection):
            self._collection = collection
        elif collection == CollectionResetMode.RESET_WITH_ROOT:
            self._collection = SequenceCollection.from_unpacked([self._root])
        elif collection == CollectionResetMode.RESET_WITH_SELF:
            self._collection = self._collection  # Normally it'd be a copy of the self._collection, but Collection should be immutable
        elif collection == CollectionResetMode.RESET_WITH_EMPTY:
            self._collection = SequenceCollection.empty()
        else:
            raise ValueError('This should never happen')

    def save(self, new_collection: CollectionResetMode | Collection, new_root: RootResetMode | Any = RootResetMode.RESET_WITH_SELF):
        self._save_stack.append((self._collection, self._root))
        if new_root != RootResetMode.RESET_WITH_SELF:
            self._root = new_root
        self.reset_collection(new_collection)

    def restore(self) -> None:
        self._collection, self._root = self._save_stack.pop()

    @property
    def root(self) -> Path:
        return self._root

    @property
    def collection(self) -> Collection:
        return self._collection
    
    def get_variable(self, name: str, default: Collection) -> Collection:
        return self._variables.get(name, default)
    
    def set_variable(self, name: str, value: Collection) -> None:
        self._variables[name] = value

    @staticmethod
    def prime(
            root_: Path | Any,
            variables_: dict[str, Collection]
    ):
        ret = _EvaluatorVisitorContext(root_)
        for k, v in variables_.items():
            ret.set_variable(k, v)
        return ret


class _EvaluatorVisitor(XplorePathGrammarVisitor):
    def __init__(
            self,
            root: Any,
            variables: dict[str, Collection]
    ):
        self.context = _EvaluatorVisitorContext.prime(root, variables)

    def visitXplorePath(self, ctx: XplorePathGrammarParser.XplorePathContext):
        return self.visit(ctx.expr())

    def visitExprPath(self, ctx: XplorePathGrammarParser.ExprPathContext):
        collection = self.visit(ctx.path())
        collection = self._apply_filter(collection, ctx.filter_())
        return collection

    def visitExprPathInvoke(self, ctx: XplorePathGrammarParser.ExprPathInvokeContext):
        ret = self.visit(ctx.path())
        ret = self._apply_filter(ret, ctx.filter_(0))
        ret = self._invoke(ret, ctx.argumentList(), ctx.filter_(1))
        return ret

    def visitExprLiteral(self, ctx: XplorePathGrammarParser.ExprLiteralContext):
        return self.visit(ctx.literal())

    def _get_var(self, ctx):
        if ctx.varRef().Name():
            name = ctx.varRef().Name().getText()
        elif ctx.varRef().IntegerLiteral():
            name = str(ctx.varRef().IntegerLiteral().getText())
        elif ctx.varRef().StringLiteral():
            name = self._decode_str(ctx.varRef().StringLiteral().getText())
        else:
            raise ValueError('Unexpected')
        return self.context.get_variable(name, SequenceCollection.empty())

    def visitExprVariable(self, ctx: XplorePathGrammarParser.ExprVariableContext):
        ret = self._get_var(ctx)
        ret = self._apply_filter(ret, ctx.filter_())
        return ret

    def visitExprVariableInvoke(self, ctx: XplorePathGrammarParser.ExprVariableInvokeContext):
        ret = self._get_var(ctx)
        ret = self._apply_filter(ret, ctx.filter_(0))
        ret = self._invoke(ret, ctx.argumentList(), ctx.filter_(1))
        return ret

    def visitExprUnary(self, ctx: XplorePathGrammarParser.ExprUnaryContext):
        if ctx.coerceFallback():
            fallback = self.visit(ctx.coerceFallback())
        else:
            fallback = DiscardFallbackMode()
        inner = self.visit(ctx.atomicOrEncapsulate())
        if ctx.MINUS():
            inner = inner.transform(lambda _, e: e.coerce(float), fallback)
            inner = inner.transform_unpacked(lambda _, v: -v, ErrorFallbackMode())
            return inner
        elif ctx.PLUS():
            return inner  # Keep it as-is -- not required to do any manipulation here
        raise ValueError('Unexpected')

    def visitExprAtomicOrEncapsulate(self, ctx: XplorePathGrammarParser.ExprAtomicOrEncapsulateContext):
        return self.visit(ctx.atomicOrEncapsulate())

    def _invoke(self, collection, arglist_ctx, result_filter_ctx):
        # if ctx.coerceFallback():
        #     fallback = self.visit(ctx.coerceFallback())
        # else:
        #     fallback = DiscardFallbackMode()
        fallback = DiscardFallbackMode()

        args = [self.visit(n) for n in arglist_ctx.expr()]
        ret = itertools.chain(*(e.invoke(args) for e in collection))  # explicitly flatten each invocation result
        ret = itertools.chain(*(fallback.evaluate(r) for r in ret))  # apply fallback
        ret = SequenceCollection.from_entities(ret)
        ret = self._apply_filter(ret, result_filter_ctx)
        return ret

    # TODO: Deeply inefficient - rework this to properly index before joining based on the condition. For example, if
    #       condition is == and both operands are known to be hashable, then create hash table and use that for quick
    #       lookup. Likewise, if relational operator (e.g. > or <=) and operands support sorting, sort and lookup using
    #       binary search.
    #
    #       Maybe, instead of passing around lists of Paths (and singular values), create a Sequence class that holds
    #       Maybe, instead of passing around lists of Paths (and singular values), create a Sequence class that holds
    #       these values. The Sequence class can generate an index (e.g. hash or sorted) based on the values within the
    #       sequence.
    def visitExprJoin(self, ctx: XplorePathGrammarParser.ExprJoinContext):
        def _create_join_obj(parent, parent_idx, l_item, r_item):
            test_path = SimplePath(ParentBlock(parent, parent_idx, 'joined'), None)
            if isinstance(l_item, Path):
                l_path = SimplePath(ParentBlock(test_path, 0, 'l'), None)
                l_path.add_child(
                    MirrorPath(l_item, ParentBlock(l_path, 0, l_item.label()))
                )
            else:
                l_path = SimplePath(ParentBlock(test_path, 0, 'l'), l_item)
            l_path.seal()
            test_path.add_child(l_path)
            if isinstance(r_item, Path):
                r_path = SimplePath(ParentBlock(test_path, 1, 'r'), None)
                r_path.add_child(
                    MirrorPath(r_item, ParentBlock(r_path, 0, r_item.label()))
                )
            else:
                r_path = SimplePath(ParentBlock(test_path, 1, 'r'), r_item)
            r_path.seal()
            test_path.add_child(r_path)
            test_path.seal()
            return test_path

        def _create_join_obj_left_only(parent, parent_idx, l_item):
            test_path = SimplePath(ParentBlock(parent, parent_idx, 'joined'), None)
            if isinstance(l_item, Path):
                l_path = SimplePath(ParentBlock(test_path, 0, 'l'), None)
                l_path.add_child(
                    MirrorPath(l_item, ParentBlock(l_path, 0, l_item.label()))
                )
            else:
                l_path = SimplePath(ParentBlock(test_path, 0, 'l'), l_item)
            l_path.seal()
            test_path.add_child(l_path)
            test_path.seal()
            return test_path

        def _create_join_obj_right_only(parent, parent_idx, r_item):
            test_path = SimplePath(ParentBlock(parent, parent_idx, 'joined'), None)
            if isinstance(r_item, Path):
                r_path = SimplePath(ParentBlock(test_path, 0, 'r'), None)
                r_path.add_child(
                    MirrorPath(r_item, ParentBlock(r_path, 0, r_item.label()))
                )
            else:
                r_path = SimplePath(ParentBlock(test_path, 0, 'r'), r_item)
            r_path.seal()
            test_path.add_child(r_path)
            test_path.seal()
            return test_path

        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        root_path = SimplePath(None, None)
        root_path_next_child_idx = 0
        if ctx.joinOp().KW_INNER():
            for l_ in l.unpack:
                for r_ in r.unpack:
                    test_path = _create_join_obj(root_path, root_path_next_child_idx, l_, r_)
                    collection = SequenceCollection.from_unpacked([test_path])
                    self.context.save(collection)
                    try:
                        collection = self._apply_filter(collection, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if collection:
                        root_path.add_child(test_path)
                        root_path_next_child_idx += 1
        elif ctx.joinOp().KW_RIGHT():
            for r_ in r.unpack:
                joined = False
                for l_ in l.unpack:
                    test_path = _create_join_obj(root_path, root_path_next_child_idx, l_, r_)
                    collection = SequenceCollection.from_unpacked([test_path])
                    self.context.save(collection)
                    try:
                        collection = self._apply_filter(collection, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if collection:
                        root_path.add_child(test_path)
                        root_path_next_child_idx += 1
                        joined = True
                if not joined:
                    r_path = _create_join_obj_right_only(root_path, root_path_next_child_idx, r_)
                    root_path.add_child(r_path)
                    root_path_next_child_idx += 1
        else:  # if KW_LEFT not set explicitly, assume KW_LEFT
            for l_ in l.unpack:
                joined = False
                for r_ in r.unpack:
                    test_path = _create_join_obj(root_path, root_path_next_child_idx, l_, r_)
                    collection = SequenceCollection.from_unpacked([test_path])
                    self.context.save(collection)
                    try:
                        collection = self._apply_filter(collection, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if collection:
                        root_path.add_child(test_path)
                        root_path_next_child_idx += 1
                        joined = True
                if not joined:
                    l_path = _create_join_obj_left_only(root_path, root_path_next_child_idx, l_)
                    root_path.add_child(l_path)
                    root_path_next_child_idx += 1
        root_path.seal()
        return SequenceCollection.from_unpacked([root_path] + root_path.all_descendants())

    def visitExprSetIntersect(self, ctx: XplorePathGrammarParser.ExprSetIntersectContext):
        l = self.visit(ctx.expr(0)).to_set()
        r = self.visit(ctx.expr(1)).to_set()
        if ctx.KW_INTERSECT():
            result_keys = l.keys() & r.keys()
        elif ctx.KW_EXCEPT():
            result_keys = l.keys() - r.keys()
        else:
            raise ValueError('Unexpected')
        return SequenceCollection.from_entities(l[p] for p in result_keys)

    def visitExprSetUnion(self, ctx: XplorePathGrammarParser.ExprSetUnionContext):
        l = self.visit(ctx.expr(0)).to_set()
        r = self.visit(ctx.expr(1)).to_set()
        result = l | r
        return SequenceCollection.from_entities(result.values())

    def visitExprBoolAggregate(self, ctx: XplorePathGrammarParser.ExprBoolAggregateContext):
        fallback_mode = self._to_fallback_mode(ctx, DefaultFallbackMode(False))
        if ctx.KW_ANY():
            op = any
        elif ctx.KW_ALL():
            op = all
        else:
            raise ValueError('Unexpected')
        r = self.visit(ctx.expr())
        r = r.transform(lambda _, e: e.coerce(bool), fallback_mode)
        return op(r.unpack)

    def visitExprMultiplicative(self, ctx: XplorePathGrammarParser.ExprMultiplicativeContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        if ctx.mulOp().STAR():
            op=lambda _l, _r: _l * _r
        elif ctx.mulOp().KW_DIV():
            op=lambda _l, _r: _l / _r
        elif ctx.mulOp().KW_IDIV():
            op=lambda _l, _r: _l // _r
        elif ctx.mulOp().KW_MOD():
            op=lambda _l, _r: _l % _r
        else:
            raise ValueError('Unexpected')
        op_required_type = float
        return combine_transform_aggregate(
            lhs=lhs,
            rhs=rhs,
            combine_mode=self._to_arithmetic_combine_mode(lhs, rhs, ctx.mulOp()),
            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(l_, r_, op, op_required_type),
            transform_fallback_mode=self._to_fallback_mode(ctx, DiscardFallbackMode()),
            aggregate_mode=AggregateMode.NONE
        )

    def visitExprAdditive(self, ctx: XplorePathGrammarParser.ExprAdditiveContext):
        lhs = self.visit(ctx.expr(0))
        rhs = self.visit(ctx.expr(1))
        if ctx.addOp().PLUS():
            op=lambda _l, _r: _l + _r
            op_required_type=float
        elif ctx.addOp().MINUS():
            op = lambda _l, _r: _l - _r
            op_required_type = float
        elif ctx.addOp().PP():
            op = lambda _l, _r: _l + _r
            op_required_type = str
        else:
            raise ValueError('Unexpected')
        return combine_transform_aggregate(
            lhs=lhs,
            rhs=rhs,
            combine_mode=self._to_arithmetic_combine_mode(lhs, rhs, ctx.addOp()),
            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(l_, r_, op, op_required_type),
            transform_fallback_mode=self._to_fallback_mode(ctx, DiscardFallbackMode()),
            aggregate_mode=AggregateMode.NONE
        )

    def _to_arithmetic_combine_mode(self, lhs, rhs, ctx) -> CombineMode:
        # default to zip if both are lists, otherwise use product as default - that's what xpath does
        if isinstance(lhs, SequenceCollection) and isinstance(rhs, SequenceCollection):
            ret = CombineMode.ZIP
        else:
            ret = CombineMode.PRODUCT
        if ctx.KW_ZIP():
            ret = CombineMode.ZIP
        elif ctx.KW_PRODUCT():
            ret = CombineMode.PRODUCT
        return ret

    def visitExprExtractLabel(self, ctx: XplorePathGrammarParser.ExprExtractLabelContext):
        ret = self.visit(ctx.expr())
        ret = ret.filter_unpacked(lambda _, v: isinstance(v, Path))
        ret = ret.transform_unpacked(lambda _, v: v.label(), ErrorFallbackMode())
        return ret

    def visitExprExtractPosition(self, ctx: XplorePathGrammarParser.ExprExtractPositionContext):
        ret = self.visit(ctx.expr())
        ret = ret.filter_unpacked(lambda _, v: isinstance(v, Path))
        ret = ret.transform_unpacked(lambda _, v: v.position(), ErrorFallbackMode())
        return ret

    def visitExprComparison(self, ctx: XplorePathGrammarParser.ExprComparisonContext):
        def _eq_op(_l, _r):
            if isinstance(_l, Matcher) and isinstance(_r, Matcher):
                return False
            if isinstance(_l, Invocable) and isinstance(_r, Invocable):
                return False
            if isinstance(_l, Matcher):
                return _l.match(_r)
            elif isinstance(_r, Matcher):
                return _r.match(_l)
            return _l == _r

        if ctx.relOp().EQ():
            op = _eq_op
            op_required_type = None
        elif ctx.relOp().NE():
            op = lambda _l, _r: not _eq_op(_l, _r)
            op_required_type = None
        elif ctx.relOp().LT():
            op = lambda _l, _r: _l < _r
            op_required_type = float
        elif ctx.relOp().LE():
            op = lambda _l, _r: _l <= _r
            op_required_type = float
        elif ctx.relOp().GT():
            op = lambda _l, _r: _l > _r
            op_required_type = float
        elif ctx.relOp().GE():
            op = lambda _l, _r: _l >= _r
            op_required_type = float
        elif ctx.relOp().LL():
            raise ValueError('Test if node A is before node B - unimplemented')
        elif ctx.relOp().GG():
            raise ValueError('Test if node A is after node B - unimplemented')
        else:
            raise ValueError('Unexpected')
        return combine_transform_aggregate(
            lhs=self.visit(ctx.expr(0)),
            rhs=self.visit(ctx.expr(1)),
            combine_mode=self._to_boolean_combine_mode(ctx.relOp()),
            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(l_, r_, op, op_required_type),
            transform_fallback_mode=self._to_fallback_mode(ctx, DefaultFallbackMode(False)),
            aggregate_mode=self._to_aggregate_mode(ctx.relOp())
        )

    def visitExprOr(self, ctx: XplorePathGrammarParser.ExprAndContext):
        op = lambda lv, rv: lv or rv
        op_required_type = bool
        return combine_transform_aggregate(
            lhs=self.visit(ctx.expr(0)),
            rhs=self.visit(ctx.expr(1)),
            combine_mode=self._to_boolean_combine_mode(ctx.orOp()),
            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(l_, r_, op, op_required_type),
            transform_fallback_mode=self._to_fallback_mode(ctx, DefaultFallbackMode(False)),
            aggregate_mode=self._to_aggregate_mode(ctx.orOp())
        )

    def visitExprAnd(self, ctx: XplorePathGrammarParser.ExprAndContext):
        op = lambda lv, rv: lv and rv
        op_required_type = bool
        return combine_transform_aggregate(
            lhs=self.visit(ctx.expr(0)),
            rhs=self.visit(ctx.expr(1)),
            combine_mode=self._to_boolean_combine_mode(ctx.andOp()),
            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(l_, r_, op, op_required_type),
            transform_fallback_mode=self._to_fallback_mode(ctx, DefaultFallbackMode(False)),
            aggregate_mode=self._to_aggregate_mode(ctx.andOp())
        )

    def _to_boolean_combine_mode(self, ctx) -> CombineMode:
        ret = CombineMode.PRODUCT  # default is product, override if set - product is default in xpath
        if ctx.KW_ZIP():
            ret = CombineMode.ZIP
        elif ctx.KW_PRODUCT():
            ret = CombineMode.PRODUCT
        return ret

    def _to_aggregate_mode(self, ctx) -> AggregateMode:
        if ctx.KW_ALL():
            return AggregateMode.ALL
        elif ctx.KW_SEQUENCE():  # keep as-is
            return AggregateMode.NONE
        else:  # if ctx.KW_ANY or no agg was explicitly specified (in which case it should default to ANY)
            return AggregateMode.ANY

    def _to_fallback_mode(self, ctx, default: FallbackMode) -> FallbackMode:
        if ctx.coerceFallback():
            return self.visit(ctx.coerceFallback())
        return default
    
    def visitExprWrapOrVar(self, ctx: XplorePathGrammarParser.ExprWrapOrVarContext):
        return self.visit(ctx.wrapOrVar())

    def visitExprWrap(self, ctx: XplorePathGrammarParser.ExprWrapContext):
        collection = self.visit(ctx.wrap())
        collection = self._apply_filter(collection, ctx.filter_())
        return collection

    def visitExprWrapInvoke(self, ctx: XplorePathGrammarParser.ExprWrapInvokeContext):
        collection = self.visit(ctx.wrap())
        collection = self._apply_filter(collection, ctx.filter_(0))
        collection = self._invoke(collection, ctx.argumentList(), ctx.filter_(1))
        return collection

    def visitExprWrapSingle(self, ctx: XplorePathGrammarParser.ExprWrapSingleContext):
        return self.visit(ctx.expr())

    def visitExprWrapSingleAsList(self, ctx: XplorePathGrammarParser.ExprWrapSingleAsListContext):
        return SequenceCollection.from_entities(self.visit(ctx.expr()))

    def visitExprWrapConcatenateList(self, ctx: XplorePathGrammarParser.ExprWrapConcatenateListContext):
        collection = []
        for e in ctx.expr():
            collection.append(self.visit(e))
        return SequenceCollection.from_entities(itertools.chain(*collection), order_paths=False, deduplicate_paths=False)  # concatenation never dedupes/orders paths

    def visitExprEmptyList(self, ctx: XplorePathGrammarParser.ExprEmptyListContext):
        return SequenceCollection.empty()

    def visitPathAtRoot(self, ctx: XplorePathGrammarParser.PathAtRootContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_ROOT)
            collection = self.context.collection
            collection = self._apply_filter(collection, ctx.filter_())
            return collection
        finally:
            self.context.restore()

    def visitPathFromRoot(self, ctx: XplorePathGrammarParser.PathFromRootContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_ROOT)
            collection = self.context.collection
            collection = self._apply_filter(collection, ctx.filter_())
            self.context.reset_collection(collection)  # will not include p, only descendants of p
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromRootAny(self, ctx: XplorePathGrammarParser.PathFromRootAnyContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_ROOT)
            root = next(iter(self.context.collection.unpack))
            collection = SequenceCollection.from_unpacked([root] + root.all_descendants())
            collection = self._apply_filter(collection, ctx.filter_())
            self.context.reset_collection(collection)
            return self.visit(ctx.relPath())  # BUG: //* must return in document order, use position_in_parent of each path in the output to sort?
        finally:
            self.context.restore()

    def visitPathAtSelf(self, ctx: XplorePathGrammarParser.PathAtSelfContext):
        return self.context.collection

    def visitPathFromSelf(self, ctx: XplorePathGrammarParser.PathFromSelfContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_SELF)
            collection = self.context.collection
            collection = self._apply_filter(collection, ctx.filter_())
            self.context.reset_collection(collection)
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromSelfAny(self, ctx: XplorePathGrammarParser.PathFromSelfAnyContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_SELF)
            collection = SequenceCollection.from_unpacked(
                itertools.chain(*([p] + p.all_descendants() for p in self.context.collection.unpack))
            )
            collection = self._apply_filter(collection, ctx.filter_())
            self.context.reset_collection(collection)  # will not include p, only descendants of p
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathAtParent(self, ctx: XplorePathGrammarParser.PathAtParentContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_SELF)
            collection = [e.parent() for e in self.context.collection.unpack]
            collection = [e for e in collection if type(e) != Null]
            collection = SequenceCollection.from_unpacked(collection)
            collection = self._apply_filter(collection, ctx.filter_())
            return collection
        finally:
            self.context.restore()

    def visitPathFromParent(self, ctx: XplorePathGrammarParser.PathFromParentContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_SELF)
            collection = [e.parent() for e in self.context.collection.unpack]
            collection = [e for e in collection if type(e) != Null]
            collection = SequenceCollection.from_unpacked(collection)
            collection = self._apply_filter(collection, ctx.filter_())
            self.context.reset_collection(collection)
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromParentAny(self, ctx: XplorePathGrammarParser.PathFromParentAnyContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_SELF)
            collection = [e.parent() for e in self.context.collection.unpack]
            collection = [e for e in collection if type(e) != Null]
            collection = SequenceCollection.from_unpacked(
                itertools.chain(*(p.all_descendants() for p in collection))
            )
            collection = self._apply_filter(collection, ctx.filter_())
            self.context.reset_collection(collection)  # will not include p's parent, only descendants of p's parent
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromNested(self, ctx: XplorePathGrammarParser.PathFromNestedContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_SELF)
            collection = self.visit(ctx.wrapOrVar())
            collection = [e for e in collection.unpack if isinstance(e, Path)]
            collection = SequenceCollection.from_unpacked(collection)
            self.context.reset_collection(collection)
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitPathFromNestedAny(self, ctx: XplorePathGrammarParser.PathFromNestedAnyContext):
        try:
            self.context.save(new_collection=CollectionResetMode.RESET_WITH_SELF)
            collection = self.visit(ctx.wrapOrVar())
            collection = [e for e in collection.unpack if isinstance(e, Path)]
            collection = SequenceCollection.from_unpacked(
                itertools.chain(*([p] + p.all_descendants() for p in collection))
            )
            self.context.reset_collection(collection)
            return self.visit(ctx.relPath())
        finally:
            self.context.restore()

    def visitRelPathChainChild(self, ctx: XplorePathGrammarParser.RelPathChainChildContext):
        # TODO: Pushing / popping state not required?
        try:
            self.context.save(CollectionResetMode.RESET_WITH_SELF)
            new_paths = []
            left_contexts = self.visit(ctx.relPath(0))
            for left_path in left_contexts.unpack:
                left_collection = SequenceCollection.from_unpacked([left_path])
                self.context.save(left_collection)
                right_contexts = self.visit(ctx.relPath(1))
                for right_path in right_contexts.unpack:
                    new_paths.append(right_path)
                self.context.restore()
            return SequenceCollection.from_unpacked(new_paths)
        finally:
            self.context.restore()

    def visitRelPathChainDescendant(self, ctx: XplorePathGrammarParser.RelPathChainDescendantContext):
        # TODO: Pushing / popping state not required?
        try:
            self.context.save(CollectionResetMode.RESET_WITH_SELF)
            new_paths = []
            left_contexts = []
            for p in self.visit(ctx.relPath(0)).unpack:
                left_contexts.append(p)
                left_contexts += p.all_descendants()
            for left_path in left_contexts:
                left_collection = SequenceCollection.from_unpacked([left_path])
                self.context.save(left_collection)
                right_contexts = self.visit(ctx.relPath(1))
                for right_path in right_contexts.unpack:
                    new_paths.append(right_path)
                self.context.restore()
            return SequenceCollection.from_unpacked(new_paths)
        finally:
            self.context.restore()

    def visitRelPathStep(self, ctx: XplorePathGrammarParser.RelPathStepContext):
        if ctx.forwardStep():
            ret = self.visit(ctx.forwardStep())
        elif ctx.reverseStep():
            ret = self.visit(ctx.reverseStep())
        else:
            raise ValueError('Unexpected')
        ret = self._apply_filter(ret, ctx.filter_())
        return ret

    def visitReverseStepParent(self, ctx: XplorePathGrammarParser.ReverseStepParentContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                parent_path = e.parent()
                if type(parent_path) != Null:
                    new_paths.append(parent_path)
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepAncestor(self, ctx: XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths += e.all_ancestors()
        new_paths = new_paths[::-1]
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepPreceding(self, ctx: XplorePathGrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths += e.preceding()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepPrecedingSibling(self, ctx: XplorePathGrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths += e.preceding_sibling()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepAncestorOrSelf(self, ctx: XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths.append(e)
                new_paths += e.all_ancestors()
        new_paths = new_paths[::-1]
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitReverseStepDirectParent(self, ctx: XplorePathGrammarParser.ReverseStepDirectParentContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                parent_path = e.parent()
                if type(parent_path) != Null:
                    new_paths.append(parent_path)
        return SequenceCollection.from_unpacked(new_paths)

    def visitForwardStepChild(self, ctx: XplorePathGrammarParser.ForwardStepChildContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths += e.all_children()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDescendant(self, ctx: XplorePathGrammarParser.ForwardStepDescendantContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths += e.all_descendants()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepSelf(self, ctx: XplorePathGrammarParser.ForwardStepSelfContext):
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDescendantOrSelf(self, ctx: XplorePathGrammarParser.ForwardStepDescendantOrSelfContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths.append(e)
                new_paths += e.all_descendants()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepFollowingSibling(self, ctx: XplorePathGrammarParser.ForwardStepFollowingSiblingContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths += e.following_sibling()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepFollowing(self, ctx: XplorePathGrammarParser.ForwardStepFollowingContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths += e.following()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepValue(self, ctx: XplorePathGrammarParser.ForwardStepValueContext):
        new_paths = []
        for e in self.context.collection.unpack:
            if isinstance(e, Path):
                new_paths += e.all_children()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_paths))
        return self._walk_down(self.visit(ctx.atomicOrEncapsulate()))

    def visitForwardStepDirectSelf(self, ctx: XplorePathGrammarParser.ForwardStepDirectSelfContext):
        return self.context.collection  # Return existing

    def _walk_down(self, collection: Collection):
        to_matcher = lambda v: v if isinstance(v, Matcher) else StrictMatcher(v)
        matchers = []
        for v in collection.unpack:
            if isinstance(v, Path):
                v = v.value()
                if v is None:
                    continue  # path has no value -- this is different from having a Null value
            matchers.append(to_matcher(v))
        # test
        combined_matcher = CombinedMatcher(matchers)
        ret = []
        for v in self.context.collection.unpack:
            if isinstance(v, Path):
                label = v.label()
            else:
                label = v
            if combined_matcher.match(label):
                ret.append(v)
        return SequenceCollection.from_unpacked(ret)

    def _apply_filter(self, collection: Collection, ctx: XplorePathGrammarParser.FilterContext | None):
        if ctx is None:
            return collection

        root = self.context.root  # explicitly get root for use in transformer, in case it changes by the time lazy evaluation takes place (it does when this is called by join condition)
                                  # -- simplest thing to do would be to not evaluate this lazily?
        def transformer(idx: int, e: Entity) -> Entity | None:
            self.context.save(SequenceCollection.from_entities([e]), root)
            try:
                result = self.visit(ctx.expr())
                if isinstance(result, SingleValueCollection) and type(result.single.value) == bool and result.single.value == True:  # /a/b[bool] - return if true
                    return e
                elif isinstance(result, SingleValueCollection) and type(result.single.value) in {float, int} and result.single.value == idx:  # /a/b[int] - return if index in the result set matches int
                    return e
                elif isinstance(result, SingleValueCollection) and type(result.single.value) == NumericRangeMatcher and result.single.value.match(idx):  # /a/b[numericrangematcher] - return if index in the result set is in range
                    return e
                elif isinstance(result, SequenceCollection) and result:  # /a/b[list] - return if non-empty (e.g. result was a list of paths looking for children, and some were found - e.g. /a/b[./c]
                    return e
                elif isinstance(result, SingleValueCollection) and isinstance(result.single.value, Matcher) and not isinstance(e.value, Path) \
                        and result.single.value.match(e.value):  # (a,b,c)[matcher] - if list of non paths, matcher should match against value directly
                    return e
                elif isinstance(result, SingleValueCollection) and isinstance(result.single.value, Matcher) and isinstance(e.value, Path) \
                        and any(result.single.value.match(c.label()) for c in e.value.all_children()):  # /a/b[matcher] - ir a path,  return if has child with name matching label, if numericrangematcher above didn't match, it might match now
                    return e
                elif isinstance(result, SingleValueCollection) and type(result.single.value) in {str, int} and isinstance(e.value, Path) and \
                        combine_transform_aggregate(
                            lhs=SequenceCollection.from_unpacked(c.label() for c in e.value.all_children()),
                            rhs=result,
                            combine_mode=CombineMode.PRODUCT,
                            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(
                                l=l_,
                                r=r_,
                                test_op=lambda l__, r__: l__ == r__,
                                required_type=None
                            ),
                            transform_fallback_mode=DiscardFallbackMode(),
                            aggregate_mode=AggregateMode.ANY
                        ).single.value:  # /a/b[str_or_int]  - return if has child with label (coerced to match if possible)
                            # you don't want to do /a/b[bool] because bool can get coerced to 0 - imagine /a/b[./c = some_val], if b is a list (labels with 0, 1, 2, 3, ...) and ./c = some_val evaluates to False, that False will coerce to int=0 for comparison and it'll always be True on first element?
                    return e
                elif isinstance(result, SingleValueCollection) and not isinstance(e.value, Path) and \
                        combine_transform_aggregate(
                            lhs=SingleValueCollection(e),
                            rhs=result,
                            combine_mode=CombineMode.PRODUCT,
                            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(
                                l=l_,
                                r=r_,
                                test_op=lambda l__, r__: l__ == r__,
                                required_type=None
                            ),
                            transform_fallback_mode=DiscardFallbackMode(),
                            aggregate_mode=AggregateMode.ANY
                        ).single.value:  # if not a path - return if values match (coerced to match if possible)
                    return e
                return None
            finally:
                self.context.restore()

        return collection.transform(transformer, DiscardFallbackMode())

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
            return SingleValueCollection(int(ctx.getText()))
        elif ctx.DecimalLiteral():
            return SingleValueCollection(float(ctx.getText()))
        elif ctx.DoubleLiteral():
            return SingleValueCollection(float(ctx.getText()))
        elif ctx.StringLiteral():
            return SingleValueCollection(self._decode_str(ctx.getText()))
        elif ctx.KW_TRUE():
            return SingleValueCollection(True)
        elif ctx.KW_FALSE():
            return SingleValueCollection(False)
        elif ctx.KW_NAN():
            return SingleValueCollection(math.nan)
        elif ctx.KW_INF():
            return SingleValueCollection(math.inf)
        elif ctx.Name():
            return SingleValueCollection(ctx.Name().getText())
        elif ctx.KW_NULL():
            return SingleValueCollection(Null())
        raise ValueError('Unexpected')

    def visitExprMatcher(self, ctx: XplorePathGrammarParser.ExprMatcherContext):
        return self.visit(ctx.matcher())

    def visitMatcherStrict(self, ctx: XplorePathGrammarParser.MatcherStrictContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return SingleValueCollection(StrictMatcher(pattern))

    def visitMatcherRegex(self, ctx: XplorePathGrammarParser.MatcherRegexContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return SingleValueCollection(RegexMatcher(pattern))

    def visitMatcherGlob(self, ctx: XplorePathGrammarParser.MatcherGlobContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return SingleValueCollection(GlobMatcher(pattern))

    def visitMatcherFuzzy(self, ctx: XplorePathGrammarParser.MatcherGlobContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return SingleValueCollection(FuzzyMatcher(pattern))

    def visitMatcherCaseInsensitive(self, ctx: XplorePathGrammarParser.MatcherCaseInsensitiveContext):
        pattern = self._decode_str(ctx.getText()[1:])
        return SingleValueCollection(IgnoreCaseMatcher(pattern))

    def visitMatcherNumericRange(self, ctx: XplorePathGrammarParser.MatcherNumericRangeContext):
        return SingleValueCollection(self.visit(ctx.numericRangeMatcher()))

    def visitMatcherWildcard(self, ctx: XplorePathGrammarParser.MatcherWildcardContext):
        return SingleValueCollection(WildcardMatcher())

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
            try:
                res = next(iter(res))
                return DefaultFallbackMode(res)
            except StopIteration:
                return DiscardFallbackMode()
        raise ValueError('Unexpected')


def evaluate(
        root: Any,
        expr: str,
        variables: dict[str, Collection] | None = None
) -> Collection:
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
        'distinct': SingleValueCollection(DistinctInvocable()),
        'count': SingleValueCollection(CountInvocable()),
        'frequency_count': SingleValueCollection(FrequencyCountInvocable()),
        'whitespace_collapse': SingleValueCollection(WhitespaceCollapseInvocable()),
        'whitespace_strip': SingleValueCollection(WhitespaceStripInvocable()),
        'whitespace_remove': SingleValueCollection(WhitespaceRemoveInvocable()),
        'regex_extract': SingleValueCollection(RegexExtractInvocable())
    }

    def __init__(
            self,
            variables: dict[str, Collection] | None = None
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


def _test_with_fs_path(dir_, expr):
    print(f'---- res for {expr}')
    fs_path = FileSystemPath.create_root_path(
        dir_,
        FileSystemContext(
            cache_notifier=lambda notice_type, real_path: print(f'{notice_type}: {real_path}')
        )
    )
    ret = Evaluator().evaluate(fs_path, expr)
    if isinstance(ret, SequenceCollection):
        for v in ret:
            print(f'  {v}')
        return ret
    else:
        print(f'  {ret}')

def _test_with_path(p, expr):
    print(f'---- res for {expr}')
    ret = Evaluator().evaluate(p, expr)
    if isinstance(ret, SequenceCollection):
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
    # _test_with_fs_path('~/Downloads', "$distinct($regex_extract(/mouse_assays.zip/*/0/GO_Term, '\d{7}'))")
    # _test_with_fs_path('~/Downloads', "/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']/*")
    # _test_with_fs_path('~/Downloads', "$regex_extract(/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']/*, '\\d{7}')")
    # _test_with_fs_path('~/Downloads', "$distinct(/mouse_assays.zip/*/0/GO_Term) inner join /goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*'] on [$regex_extract(//l, '\\d{7}') = $regex_extract(//r//id, '\\d{7}')]")
    # _test_with_fs_path('~/Downloads', "//*")
    # _test_with_fs_path('~/Downloads', "/mouse_assays.zip/Mouse_Assay_001.csv/*[./*=Well]")
    # _test_with_fs_path('~/Downloads', "/mouse_assays.zip/Mouse_Assay_001.csv/*[.//*=Well]")
    # _test_with_fs_path('~/Downloads', "($frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'))[. >= 5]")  # doesn't work, should filter to >= 5 counts
    # _test_with_fs_path('~/Downloads', "$whitespace_collapse(['hello    world', 'hello world', 'helloworld'])")
    # _test_with_fs_path('~/Downloads', "$whitespace_remove(['hello    world', 'hello world', 'helloworld'])")
    # _test_with_fs_path('~/Downloads', "/uniprotkb_mouse_601_to_800_seqlen.json/results/*/genes[.//geneName/value = 'Zmat1']//geneName/value")

    # _test(root, '$regex_extract((hello, yellow, mellow), "low?")')
