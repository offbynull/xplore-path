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
from xplore_path.node import Node, ParentBlock
from xplore_path.nodes.mirror.mirror_node import MirrorNode
from xplore_path.nodes.simple.simple_node import SimpleNode
from xplore_path.raise_parse_error_listener import RaiseParseErrorListener


class _CollectionResetMode(Enum):
    RESET_WITH_ROOT = 'RESET_WITH_ROOT'
    RESET_WITH_SELF = 'RESET_WITH_SELF'
    RESET_WITH_EMPTY = 'RESET_WITH_EMPTY'


class _RootResetMode(Enum):
    RESET_WITH_SELF = 'RESET_WITH_SELF'


class _EvaluatorVisitorContext:
    def __init__(
            self,
            root: Node
    ):
        self._root = root
        self._collection = SequenceCollection.from_unpacked([root])
        self._save_stack = []
        self._variables = {}

    def __post_init__(self):
        if self._root.full_label() != []:
            raise ValueError('Root node is not root')

    def reset_collection(self, collection: _CollectionResetMode | Collection):
        if isinstance(collection, Collection):
            self._collection = collection
        elif collection == _CollectionResetMode.RESET_WITH_ROOT:
            self._collection = SequenceCollection.from_unpacked([self._root])
        elif collection == _CollectionResetMode.RESET_WITH_SELF:
            ... # It's asking to be reset to a "copy" what it already is, but Collection is immutable so this is a no-op
        elif collection == _CollectionResetMode.RESET_WITH_EMPTY:
            self._collection = SequenceCollection.empty()
        else:
            raise ValueError('This should never happen')

    def save(
            self,
            new_collection: _CollectionResetMode | Collection,
            new_root: _RootResetMode | Any = _RootResetMode.RESET_WITH_SELF
    ):
        self._save_stack.append((self._collection, self._root))
        if new_root != _RootResetMode.RESET_WITH_SELF:
            self._root = new_root
        self.reset_collection(new_collection)

    def restore(self) -> None:
        self._collection, self._root = self._save_stack.pop()

    @property
    def root(self) -> Node:
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
            root_: Node,
            variables_: dict[str, Collection]
    ):
        ret = _EvaluatorVisitorContext(root_)
        for k, v in variables_.items():
            ret.set_variable(k, v)
        return ret


class _EvaluatorVisitor(XplorePathGrammarVisitor):
    def __init__(
            self,
            root: Node,
            variables: dict[str, Collection]
    ):
        self.context = _EvaluatorVisitorContext.prime(root, variables)

    def visitXplorePath(self, ctx: XplorePathGrammarParser.XplorePathContext):
        return self.visit(ctx.expr())

    # TODO: Deeply inefficient - rework this to properly index before joining based on the condition. For example, if
    #       condition is == and both operands are known to be hashable, then create hash table and use that for quick
    #       lookup. Likewise, if relational operator (e.g. > or <=) and operands support sorting, sort and lookup using
    #       binary search.
    #
    #       Maybe, instead of passing around lists of Nodes (and singular values), create a Sequence class that holds
    #       these values. The Sequence class can generate an index (e.g. hash or sorted) based on the values within the
    #       sequence.
    def visitExprJoinHit(self, ctx: XplorePathGrammarParser.ExprJoinHitContext):
        def _create_join_obj(parent, parent_idx, l_item, r_item):
            test_node = SimpleNode(ParentBlock(parent, parent_idx, 'joined'), None)
            if isinstance(l_item, Node):
                l_node = SimpleNode(ParentBlock(test_node, 0, 'l'), None)
                l_node.add_child(
                    MirrorNode(l_item, ParentBlock(l_node, 0, l_item.label()))
                )
            else:
                l_node = SimpleNode(ParentBlock(test_node, 0, 'l'), l_item)
            l_node.seal()
            test_node.add_child(l_node)
            if isinstance(r_item, Node):
                r_node = SimpleNode(ParentBlock(test_node, 1, 'r'), None)
                r_node.add_child(
                    MirrorNode(r_item, ParentBlock(r_node, 0, r_item.label()))
                )
            else:
                r_node = SimpleNode(ParentBlock(test_node, 1, 'r'), r_item)
            r_node.seal()
            test_node.add_child(r_node)
            test_node.seal()
            return test_node

        def _create_join_obj_left_only(parent, parent_idx, l_item):
            test_node = SimpleNode(ParentBlock(parent, parent_idx, 'joined'), None)
            if isinstance(l_item, Node):
                l_node = SimpleNode(ParentBlock(test_node, 0, 'l'), None)
                l_node.add_child(
                    MirrorNode(l_item, ParentBlock(l_node, 0, l_item.label()))
                )
            else:
                l_node = SimpleNode(ParentBlock(test_node, 0, 'l'), l_item)
            l_node.seal()
            test_node.add_child(l_node)
            test_node.seal()
            return test_node

        def _create_join_obj_right_only(parent, parent_idx, r_item):
            test_node = SimpleNode(ParentBlock(parent, parent_idx, 'joined'), None)
            if isinstance(r_item, Node):
                r_node = SimpleNode(ParentBlock(test_node, 0, 'r'), None)
                r_node.add_child(
                    MirrorNode(r_item, ParentBlock(r_node, 0, r_item.label()))
                )
            else:
                r_node = SimpleNode(ParentBlock(test_node, 0, 'r'), r_item)
            r_node.seal()
            test_node.add_child(r_node)
            test_node.seal()
            return test_node

        l = self.visit(ctx.exprJoin())
        r = self.visit(ctx.exprSetIntersect())
        root_node = SimpleNode(None, None)
        root_node_next_child_idx = 0
        if ctx.joinOp().KW_INNER():
            for l_ in l.unpack:
                for r_ in r.unpack:
                    test_node = _create_join_obj(root_node, root_node_next_child_idx, l_, r_)
                    collection = SequenceCollection.from_unpacked([test_node])
                    self.context.save(collection)
                    try:
                        collection = self._apply_filter(collection, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if collection:
                        root_node.add_child(test_node)
                        root_node_next_child_idx += 1
        elif ctx.joinOp().KW_RIGHT():
            for r_ in r.unpack:
                joined = False
                for l_ in l.unpack:
                    test_node = _create_join_obj(root_node, root_node_next_child_idx, l_, r_)
                    collection = SequenceCollection.from_unpacked([test_node])
                    self.context.save(collection)
                    try:
                        collection = self._apply_filter(collection, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if collection:
                        root_node.add_child(test_node)
                        root_node_next_child_idx += 1
                        joined = True
                if not joined:
                    r_node = _create_join_obj_right_only(root_node, root_node_next_child_idx, r_)
                    root_node.add_child(r_node)
                    root_node_next_child_idx += 1
        else:  # if KW_LEFT not set explicitly, assume KW_LEFT
            for l_ in l.unpack:
                joined = False
                for r_ in r.unpack:
                    test_node = _create_join_obj(root_node, root_node_next_child_idx, l_, r_)
                    collection = SequenceCollection.from_unpacked([test_node])
                    self.context.save(collection)
                    try:
                        collection = self._apply_filter(collection, ctx.joinCond().filter_())
                    finally:
                        self.context.restore()
                    if collection:
                        root_node.add_child(test_node)
                        root_node_next_child_idx += 1
                        joined = True
                if not joined:
                    l_node = _create_join_obj_left_only(root_node, root_node_next_child_idx, l_)
                    root_node.add_child(l_node)
                    root_node_next_child_idx += 1
        root_node.seal()
        return SequenceCollection.from_unpacked([root_node] + root_node.descendants())

    def visitExprSetIntersectHit(self, ctx: XplorePathGrammarParser.ExprSetIntersectHitContext):
        l = self.visit(ctx.exprSetIntersect()).to_set()
        r = self.visit(ctx.exprSetUnion()).to_set()
        if ctx.KW_INTERSECT():
            result_keys = l.keys() & r.keys()
        elif ctx.KW_EXCEPT():
            result_keys = l.keys() - r.keys()
        else:
            raise ValueError('Unexpected')
        return SequenceCollection.from_entities(l[p] for p in result_keys)

    def visitExprSetUnionHit(self, ctx: XplorePathGrammarParser.ExprSetUnionHitContext):
        l = self.visit(ctx.exprSetUnion()).to_set()
        r = self.visit(ctx.exprOr()).to_set()
        result = l | r
        return SequenceCollection.from_entities(result.values())

    def visitExprOrHit(self, ctx: XplorePathGrammarParser.ExprOrHitContext):
        lhs = self.visit(ctx.exprOr())
        rhs = self.visit(ctx.exprAnd())
        if ctx.orOp().KW_EXPAND() is None:
            lhs = self._collapseSequenceCollectionToBoolSingleValueCollection(lhs)
            rhs = self._collapseSequenceCollectionToBoolSingleValueCollection(rhs)
        op = lambda lv, rv: lv or rv
        op_required_type = bool
        return combine_transform_aggregate(
            lhs=lhs,
            rhs=rhs,
            combine_mode=self._to_boolean_combine_mode(ctx.orOp()),
            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(l_, r_, op, op_required_type),
            transform_fallback_mode=self._to_fallback_mode(ctx, DefaultFallbackMode(False)),
            aggregate_mode=self._to_aggregate_mode(ctx.orOp())
        )

    def visitExprAndHit(self, ctx: XplorePathGrammarParser.ExprAndHitContext):
        lhs = self.visit(ctx.exprAnd())
        rhs = self.visit(ctx.exprNot())
        if ctx.andOp().KW_EXPAND() is None:
            lhs = self._collapseSequenceCollectionToBoolSingleValueCollection(lhs)
            rhs = self._collapseSequenceCollectionToBoolSingleValueCollection(rhs)
        op = lambda lv, rv: lv and rv
        op_required_type = bool
        return combine_transform_aggregate(
            lhs=lhs,
            rhs=rhs,
            combine_mode=self._to_boolean_combine_mode(ctx.andOp()),
            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(l_, r_, op, op_required_type),
            transform_fallback_mode=self._to_fallback_mode(ctx, DefaultFallbackMode(False)),
            aggregate_mode=self._to_aggregate_mode(ctx.andOp())
        )

    def visitExprNotHit(self, ctx: XplorePathGrammarParser.ExprNotHitContext):
        fallback_mode = self._to_fallback_mode(ctx, DiscardFallbackMode())
        r = self.visit(ctx.exprNot())
        if ctx.notOp().KW_EXPAND() is None:
            r = self._collapseSequenceCollectionToBoolSingleValueCollection(r)
        r = r.transform(lambda _, e: e.coerce(bool), fallback_mode)
        r = r.transform(lambda _, e: Entity(not e.value), fallback_mode)
        return r

    # For boolean operations (AND/OR/NOT), an operand that's a SequenceCollection should get treated as a bool (True for
    # non-empty) - this is the default xpath behavior.
    def _collapseSequenceCollectionToBoolSingleValueCollection(self, c: Collection) -> Collection:
        if isinstance(c, SingleValueCollection):
            return c
        elif isinstance(c, SequenceCollection):
            return SingleValueCollection(bool(c))
        else:
            raise ValueError()

    def visitExprComparisonHit(self, ctx: XplorePathGrammarParser.ExprComparisonHitContext):
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
            lhs=self.visit(ctx.exprComparison()),
            rhs=self.visit(ctx.exprAdditive()),
            combine_mode=self._to_boolean_combine_mode(ctx.relOp()),
            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(l_, r_, op, op_required_type),
            transform_fallback_mode=self._to_fallback_mode(ctx, DefaultFallbackMode(False)),
            aggregate_mode=self._to_aggregate_mode(ctx.relOp())
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

    def visitExprAdditiveHit(self, ctx: XplorePathGrammarParser.ExprAdditiveHitContext):
        lhs = self.visit(ctx.exprAdditive())
        rhs = self.visit(ctx.exprMultiplicative())
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

    def visitExprMultiplicativeHit(self, ctx: XplorePathGrammarParser.ExprMultiplicativeHitContext):
        lhs = self.visit(ctx.exprMultiplicative())
        rhs = self.visit(ctx.exprUnary())
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

    def visitExprUnaryNegateHit(self, ctx: XplorePathGrammarParser.ExprUnaryNegateHitContext):
        if ctx.coerceFallback():
            fallback = self.visit(ctx.coerceFallback())
        else:
            fallback = DiscardFallbackMode()
        inner = self.visit(ctx.exprUnary())
        if ctx.MINUS():
            inner = inner.transform(lambda _, e: e.coerce(float), fallback)
            inner = inner.transform_unpacked(lambda _, v: -v, ErrorFallbackMode())
            return inner
        elif ctx.PLUS():
            return inner  # Keep it as-is -- not required to do any manipulation here
        raise ValueError('Unexpected')

    def visitExprUnaryLabelHit(self, ctx: XplorePathGrammarParser.ExprUnaryLabelHitContext):
        ret = self.visit(ctx.exprUnary())
        ret = ret.filter_unpacked(lambda _, v: isinstance(v, Node))
        ret = ret.transform_unpacked(lambda _, v: v.label(), ErrorFallbackMode())
        return ret

    def visitExprUnaryPositionHit(self, ctx: XplorePathGrammarParser.ExprUnaryPositionHitContext):
        ret = self.visit(ctx.exprUnary())
        ret = ret.filter_unpacked(lambda _, v: isinstance(v, Node))
        ret = ret.transform_unpacked(lambda _, v: v.position(), ErrorFallbackMode())
        return ret

    def visitExprUnaryAnyAggregateHit(self, ctx: XplorePathGrammarParser.ExprUnaryAnyAggregateHitContext):
        fallback_mode = self._to_fallback_mode(ctx, DefaultFallbackMode(False))
        r = self.visit(ctx.exprUnary())
        r = r.transform(lambda _, e: e.coerce(bool), fallback_mode)
        return any(r.unpack)

    def visitExprUnaryAllAggregateHit(self, ctx: XplorePathGrammarParser.ExprUnaryAllAggregateHitContext):
        fallback_mode = self._to_fallback_mode(ctx, DefaultFallbackMode(False))
        r = self.visit(ctx.exprUnary())
        r = r.transform(lambda _, e: e.coerce(bool), fallback_mode)
        return all(r.unpack)

    def _to_fallback_mode(self, ctx, default: FallbackMode) -> FallbackMode:
        if ctx.coerceFallback():
            return self.visit(ctx.coerceFallback())
        return default

    def visitExprPath(self, ctx: XplorePathGrammarParser.ExprPathContext):
        collection = self.visit(ctx.path())
        return collection

    def visitExprPathInvoke(self, ctx: XplorePathGrammarParser.ExprPathInvokeContext):
        ret = self.visit(ctx.path())
        ret = self._invoke(ret, ctx.argumentList(), ctx.filter_())
        return ret

    def visitExprAtomic(self, ctx: XplorePathGrammarParser.ExprAtomicContext):
        return self.visit(ctx.atomic())

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
        return SequenceCollection.from_entities(
            itertools.chain(*collection),
            order_nodes=False,
            deduplicate_nodes=False
        )  # concatenation never dedupes/orders paths

    def visitExprEmptyList(self, ctx: XplorePathGrammarParser.ExprEmptyListContext):
        return SequenceCollection.empty()

    def visitPath(self, ctx: XplorePathGrammarParser.PathContext):
        self.context.save(new_collection=_CollectionResetMode.RESET_WITH_SELF)
        try:
            if ctx.pathAbsolute():
                self.context.reset_collection(_CollectionResetMode.RESET_WITH_ROOT)
                return self.visit(ctx.pathAbsolute())
            elif ctx.pathRelative():
                return self.visit(ctx.pathRelative())
            else:
                raise ValueError('Unexpected')
        finally:
            self.context.restore()

    def visitPathAbsolute(self, ctx: XplorePathGrammarParser.PathAbsoluteContext):
        self.context.save(new_collection=_CollectionResetMode.RESET_WITH_SELF)
        try:
            # Get top-level nodes
            if ctx.SLASH():
                collection = self.context.collection
            elif ctx.SS():
                root = next(iter(self.context.collection.unpack))
                collection = SequenceCollection.from_unpacked([root] + root.descendants())
                collection = self._apply_filter(collection, ctx.filter_())
            else:
                raise ValueError('Unexpected')
            # Filter top-level nodes
            collection = self._apply_filter(collection, ctx.filter_())
            # Walk into top-level nodes
            if ctx.pathInner():
                self.context.reset_collection(collection)
                collection = self.visit(ctx.pathInner())
            return collection
        finally:
            self.context.restore()

    def visitPathRelative(self, ctx: XplorePathGrammarParser.PathRelativeContext):
        self.context.save(new_collection=_CollectionResetMode.RESET_WITH_SELF)
        try:
            # Get top-level nodes
            if ctx.D():
                collection = self.context.collection
            elif ctx.DD():
                collection = [e.parent() for e in self.context.collection.unpack]
                collection = [e for e in collection if type(e) != Null]
                collection = SequenceCollection.from_unpacked(collection)
            elif ctx.wrapOrVar():
                collection = self.visit(ctx.wrapOrVar())
                collection = [e for e in collection.unpack if isinstance(e, Node)]
                collection = SequenceCollection.from_unpacked(collection)
            else:
                raise ValueError('Unexpected')
            # Filter top-level nodes
            collection = self._apply_filter(collection, ctx.filter_())
            # Walk into top-level nodes
            if ctx.pathAbsolute():
                self.context.reset_collection(collection)
                collection = self.visit(ctx.pathAbsolute())
            return collection
        finally:
            self.context.restore()

    def visitPathInner(self, ctx: XplorePathGrammarParser.PathInnerContext):
        # TODO: Pushing / popping state not required?
        try:
            self.context.save(_CollectionResetMode.RESET_WITH_SELF)
            collection = self.visit(ctx.step(0))
            child_cnt = ctx.getChildCount()
            child_idx = 1
            while child_idx < child_cnt:
                separator = ctx.getChild(child_idx)
                if separator.SS():
                    collection_with_descendants = []
                    for p in collection.unpack:
                        collection_with_descendants.append(p)
                        collection_with_descendants += p.descendants()
                    collection = SequenceCollection.from_unpacked(collection_with_descendants)
                elif separator.SLASH():
                    ...
                else:
                    raise ValueError('Unexpected')
                self.context.reset_collection(collection)
                step = ctx.getChild(child_idx + 1)
                collection = self.visit(step)
                child_idx += 2
            return collection
        finally:
            self.context.restore()

    def visitStep(self, ctx: XplorePathGrammarParser.StepContext):
        if ctx.forwardStep():
            ret = self.visit(ctx.forwardStep())
        elif ctx.reverseStep():
            ret = self.visit(ctx.reverseStep())
        else:
            raise ValueError('Unexpected')
        ret = self._apply_filter(ret, ctx.filter_())
        return ret

    def visitReverseStepParent(self, ctx: XplorePathGrammarParser.ReverseStepParentContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                parent_node = e.parent()
                if type(parent_node) != Null:
                    new_nodes.append(parent_node)
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitReverseStepAncestor(self, ctx: XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes += e.ancestors()
        new_nodes = new_nodes[::-1]
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitReverseStepPreceding(self, ctx: XplorePathGrammarParser.ReverseStepPrecedingContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes += e.preceding()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitReverseStepPrecedingSibling(self, ctx: XplorePathGrammarParser.ReverseStepPrecedingContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes += e.preceding_sibling()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitReverseStepAncestorOrSelf(self, ctx: XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes.append(e)
                new_nodes += e.ancestors()
        new_nodes = new_nodes[::-1]
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitReverseStepDirectParent(self, ctx: XplorePathGrammarParser.ReverseStepDirectParentContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                parent_node = e.parent()
                if type(parent_node) != Null:
                    new_nodes.append(parent_node)
        return SequenceCollection.from_unpacked(new_nodes)

    def visitForwardStepChild(self, ctx: XplorePathGrammarParser.ForwardStepChildContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes += e.children()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitForwardStepDescendant(self, ctx: XplorePathGrammarParser.ForwardStepDescendantContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes += e.descendants()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitForwardStepSelf(self, ctx: XplorePathGrammarParser.ForwardStepSelfContext):
        return self._walk_down(self.visit(ctx.atomic()))

    def visitForwardStepDescendantOrSelf(self, ctx: XplorePathGrammarParser.ForwardStepDescendantOrSelfContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes.append(e)
                new_nodes += e.descendants()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitForwardStepFollowingSibling(self, ctx: XplorePathGrammarParser.ForwardStepFollowingSiblingContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes += e.following_sibling()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitForwardStepFollowing(self, ctx: XplorePathGrammarParser.ForwardStepFollowingContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes += e.following()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitForwardStepValue(self, ctx: XplorePathGrammarParser.ForwardStepValueContext):
        new_nodes = []
        for e in self.context.collection.unpack:
            if isinstance(e, Node):
                new_nodes += e.children()
        self.context.reset_collection(SequenceCollection.from_unpacked(new_nodes))
        return self._walk_down(self.visit(ctx.atomic()))

    def visitForwardStepDirectSelf(self, ctx: XplorePathGrammarParser.ForwardStepDirectSelfContext):
        return self.context.collection  # Return existing

    def _walk_down(self, collection: Collection):
        to_matcher = lambda v: v if isinstance(v, Matcher) else StrictMatcher(v)
        matchers = []
        for v in collection.unpack:
            if isinstance(v, Node):
                v = v.value()
                if v is None:
                    continue  # node has no value -- this is different from having a Null value
            matchers.append(to_matcher(v))
        # test
        combined_matcher = CombinedMatcher(matchers)
        ret = []
        for v in self.context.collection.unpack:
            if isinstance(v, Node):
                label = v.label()
            else:
                label = v
            if combined_matcher.match(label):
                ret.append(v)
        return SequenceCollection.from_unpacked(ret)

    def _apply_filter(self, collection: Collection, ctx: XplorePathGrammarParser.FilterContext | None):
        if ctx is None:
            return collection

        # If filter evaluates to number or NumericRangeMatcher, extract by index
        # ----------------------------------------------------------------------
        try:
            self.context.save(collection)
            filter_res_exp = self.visit(ctx.expr())
            # /a/b[int] - Return if index in the filter_res_exp set matches int.
            if isinstance(filter_res_exp, SingleValueCollection) \
                    and type(filter_res_exp.single.value) in {float, int}:
                return collection.filter(lambda idx, _: filter_res_exp.single.value == idx)
            # /a/b[NumericRangeMatcher] - Return if index in the filter_res_exp set is in range
            elif isinstance(filter_res_exp, SingleValueCollection) \
                    and type(filter_res_exp.single.value) == NumericRangeMatcher:
                return collection.filter(lambda idx, _: filter_res_exp.single.value.match(idx))
        finally:
            self.context.restore()

        # If filter evaluates to number or NumericRangeMatcher, apply filtering logic on each child
        # -----------------------------------------------------------------------------------------
        # Explicitly get root for use in transformer(). This is done in case root changes by the time lazy evaluation
        # takes place (e.g. this used to happen when _apply_filter() was invoked by the joining logic, and may
        # potentially happen again). But, doing this adds confusion / complexity. The simplest thing to do would be to
        # avoid lazy evaluation entirely? Ultimately, the results get sorted before they're returned such that they're
        # in document-order and duplicates are removed (see SequenceCollection class), so lazy evaluation has no real
        # benefit? Unless that sorting/deduplication requirement is removed?
        root = self.context.root

        def transformer(idx: int, e: Entity) -> Entity | None:
            self.context.save(SequenceCollection.from_entities([e]), root)
            try:
                filter_res_exp = self.visit(ctx.expr())
                # /a/b[bool] - Return if true.
                if isinstance(filter_res_exp, SingleValueCollection) \
                        and type(filter_res_exp.single.value) == bool \
                        and filter_res_exp.single.value == True:
                    return e
                # /a/b[list] - Return if non-empty (e.g. filter_res_exp was a list of nodes looking for children, and
                #              some were found: /a/b[./c])
                elif isinstance(filter_res_exp, SequenceCollection) and filter_res_exp:
                    return e
                # (a,b,c)[matcher] - If list of non-nodes, matcher should match against value directly
                elif isinstance(filter_res_exp, SingleValueCollection) \
                        and isinstance(filter_res_exp.single.value, Matcher) \
                        and not isinstance(e.value, Node) and filter_res_exp.single.value.match(e.value):
                    return e
                # /a/b[matcher] - If a node, return if has child with name matching label. Assuming that the
                #                 NumericRangeMatcher test above didn't match, it might match now.
                elif isinstance(filter_res_exp, SingleValueCollection) \
                        and isinstance(filter_res_exp.single.value, Matcher) \
                        and isinstance(e.value, Node) \
                        and any(filter_res_exp.single.value.match(c.label()) for c in e.value.children()):
                    return e
                # /a/b[str] - Return if child exists matching str (coerced to match if possible).
                elif isinstance(filter_res_exp, SingleValueCollection) \
                        and type(filter_res_exp.single.value) in {str} \
                        and isinstance(e.value, Node) \
                        and combine_transform_aggregate(
                            lhs=SequenceCollection.from_unpacked(c.label() for c in e.value.children()),
                            rhs=filter_res_exp,
                            combine_mode=CombineMode.PRODUCT,
                            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(
                                l=l_,
                                r=r_,
                                test_op=lambda l__, r__: l__ == r__,
                                required_type=None
                            ),
                            transform_fallback_mode=DiscardFallbackMode(),
                            aggregate_mode=AggregateMode.ANY
                        ).single.value:
                    return e
                # (a,b,c)[any] - Return any values match (coerced to match if possible)
                elif isinstance(filter_res_exp, SingleValueCollection) \
                        and not isinstance(e.value, Node) \
                        and combine_transform_aggregate(
                            lhs=SingleValueCollection(e),
                            rhs=filter_res_exp,
                            combine_mode=CombineMode.PRODUCT,
                            transformer=lambda _, l_, __, r_: Entity.apply_binary_boolean_op(
                                l=l_,
                                r=r_,
                                test_op=lambda l__, r__: l__ == r__,
                                required_type=None
                            ),
                            transform_fallback_mode=DiscardFallbackMode(),
                            aggregate_mode=AggregateMode.ANY
                        ).single.value:
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


class Evaluator:
    """
    Expression evaluator.
    """
    DEFAULT_VARIABLES = {
        'distinct': SingleValueCollection(DistinctInvocable()),
        'count': SingleValueCollection(CountInvocable()),
        'frequency_count': SingleValueCollection(FrequencyCountInvocable()),
        'whitespace_collapse': SingleValueCollection(WhitespaceCollapseInvocable()),
        'whitespace_strip': SingleValueCollection(WhitespaceStripInvocable()),
        'whitespace_remove': SingleValueCollection(WhitespaceRemoveInvocable()),
        'regex_extract': SingleValueCollection(RegexExtractInvocable())
    }
    """Default variables, providing commonly needed functions / data."""

    def __init__(
            self,
            variables: dict[str, Collection] | None = None
    ):
        """
        Construct an ``Evaluator`` instance.

        :param variables: Variables available to expressions being evaluated. If ``None``, uses default
            ``Evaluator.DEFAULT_VARIABLES``.
        """
        if variables is None:
            variables = Evaluator.DEFAULT_VARIABLES.copy()
        self.variables = variables

    def evaluate(
            self,
            root: Node,
            expr: str
    ) -> Collection:
        """
        Evaluate expression. The expression (``expr``) is evaluated relative to the root node of a hierarchy (``root``),
        where the evaluation typically traverses/searches that hierarchy in some way.

        Example::

            # Convert nested Python collections into a hierarchy of nodes
            root = PythonObjectPath.create_root_path(
                {
                    'a': {
                        b': {
                            'c': 1,
                            'e': -1,
                        }
                    },
                    'y': [3, 'hi', 5.0],
                    'z': {
                        'd_ptr': 'd',
                        'f_ptr': 'f'
                    }
                }
            )
            # Search through nodes for any labelled b that also has a child labelled c
            ret = Evaluator().evaluate(root, '//b[./c]')

        :param root: Root node of hierarchy.
        :param expr: Expression to evaluate.
        :return: Result of evaluated expression.
        :raises ParseException: If ``expr`` has invalid syntax.
        :raises Exception: If ``expr`` causes evaluation to enter into an unexpected state (rare, but may happen).
        """
        input_stream = InputStream(expr)
        lexer = XplorePathGrammarLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(RaiseParseErrorListener())
        token_stream = CommonTokenStream(lexer)
        parser = XplorePathGrammarParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(RaiseParseErrorListener())
        tree = parser.xplorePath()
        visitor = _EvaluatorVisitor(root, self.variables)
        return tree.accept(visitor)


# from xplore_path.nodes.filesystem.context import FileSystemContext
# from xplore_path.nodes.filesystem.filesystem_node import FileSystemNode
# from xplore_path.nodes.python_object.python_object_node import PythonObjectNode
#
#
# def _test_with_obj(root_obj, expr):
#     print(f'---- res for {expr}')
#     node = PythonObjectNode.create_root_path(root_obj)
#     ret = Evaluator().evaluate(node, expr)
#     if isinstance(ret, SequenceCollection):
#         for v in ret:
#             print(f'  {v}')
#         return ret
#     else:
#         print(f'  {ret}')
#
#
# def _test_with_fs(dir_, expr):
#     print(f'---- res for {expr}')
#     fs_node = FileSystemNode.create_root_path(
#         dir_,
#         FileSystemContext(
#             cache_notifier=lambda notice_type, real_path: print(f'{notice_type}: {real_path}')
#         )
#     )
#     ret = Evaluator().evaluate(fs_node, expr)
#     if isinstance(ret, SequenceCollection):
#         for v in ret:
#             print(f'  {v}')
#         return ret
#     else:
#         print(f'  {ret}')
#
#
# if __name__ == '__main__':
#     ...
#     # _test_with_fs('~', '/*')
#     # _test_with_fs('~', '/test.json//*')
#     # _test_with_fs('~', '/test.json/address/city')
#     # _test_with_fs('~', '/test.xml//*')
#     # _test_with_fs('~', '/test.html//*')
#     # _test_with_fs('~/Downloads', '/pycharm-community-2024.3.1.tar.gz/*')
#     # _test_with_fs('~/Downloads', "/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/*/'Unnamed: 2'")
#     # _test_with_fs('~/Downloads', "/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'//*")
#     # _test_with_fs('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies//*")
#     # _test_with_fs('~/Downloads', "2025 - (/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/*/'Unnamed: 2')")
#     # _test_with_fs('~', '/test.yaml//*')
#     # _test_with_fs('~', '/test.csv/*/Name')
#     # _test_with_fs('~', '/test.csv/*/Name[. = "John Doe"]')
#     # _test_with_fs('~', '/test.csv/*')
#     # _test_with_fs('~', '/test.csv/*[./Name = f"John Do"]')
#     # _test_with_fs('~', '/test.csv/*[f"John Do" = ./Name]')
#     # _test_with_fs('~', '/test.csv/*[r"J.*" = ./Name]')
#     # _test_with_fs('~', '(/test.csv/*)[./Name/r"J.*"]')
#
#     # _test_with_fs('~', '/Downloads/*')
#     # _test_with_fs('~', '/Downloads/"parabilis.zip"/*')
#     # _test_with_fs('~', '/Downloads/"parabilis.zip"/parabilis/*')
#     # _test_with_fs('~', '/Downloads/"parabilis.zip"/parabilis/".idea"/*')
#     # _test_with_fs('~', '/Downloads/"parabilis.zip"/parabilis/".idea"/modules.xml//*')
#
#     # _test_with_fs('~/Downloads', "2025 - (/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/*/'Unnamed: 2')")
#     # _test_with_fs('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 2'")
#     # _test_with_fs('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/*[./'Unnamed: 2' = (2025 - (/Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/*/'Unnamed: 2'))]")
#     # _test_with_fs('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/* inner join /Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/* on [./1/'Unnamed: 2' = (2025 - ./2/'Unnamed: 2')]")  # Shows up as [None]: None  because value is none, but data is there under children
#     # _test_with_fs('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/* left join /Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/* on [./1/'Unnamed: 2' = (2025 - ./2/'Unnamed: 2')]")  # Shows up as [None]: None  because value is none, but data is there under children
#     # _test_with_fs('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/* right join /Healthcare-Insurance-Sample-Data.xlsx/'Healthcare Insurance'/* on [./1/'Unnamed: 2' = (2025 - ./2/'Unnamed: 2')]")  # Shows up as [None]: None  because value is none, but data is there under children
#     # _test_with_fs('~/Downloads', "/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'")
#     # _test_with_fs('~/Downloads', "$count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3')")
#     # _test_with_fs('~/Downloads', "$distinct(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3')")
#     # _test_with_fs('~/Downloads', "$frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3')")
#     # _test_with_fs('~/Downloads', "($frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'))/*")
#     # _test_with_fs('~/Downloads', "($frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'))//*")
#     # _test_with_fs('~/Downloads', "$distinct($regex_extract(/mouse_assays.zip/*/0/GO_Term, '\d{7}'))")
#     # _test_with_fs('~/Downloads', "/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']/*")
#     # _test_with_fs('~/Downloads', "$regex_extract(/goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*']/*, '\\d{7}')")
#     # _test_with_fs('~/Downloads', "$distinct(/mouse_assays.zip/*/0/GO_Term) inner join /goslim_mouse.json/graphs//*[./meta/definition/val = g'*neuro*'] on [$regex_extract(//l, '\\d{7}') = $regex_extract(//r//id, '\\d{7}')]")
#     # _test_with_fs('~/Downloads', "//*")
#     # _test_with_fs('~/Downloads', "/mouse_assays.zip/Mouse_Assay_001.csv/*[./*=Well]")
#     # _test_with_fs('~/Downloads', "/mouse_assays.zip/Mouse_Assay_001.csv/*[.//*=Well]")
#     # _test_with_fs('~/Downloads', "($frequency_count(/Netflix-Movies-Sample-Data.xlsx/Movies/*/'Unnamed: 3'))[. >= 5]")  # doesn't work, should filter to >= 5 counts
#     # _test_with_fs('~/Downloads', "$whitespace_collapse(['hello    world', 'hello world', 'helloworld'])")
#     # _test_with_fs('~/Downloads', "$whitespace_remove(['hello    world', 'hello world', 'helloworld'])")
#     # _test_with_fs('~/Downloads', "/uniprotkb_mouse_601_to_800_seqlen.json/results/*/genes[.//geneName/value = 'Zmat1']//geneName/value")
#
#     _test_with_fs('./', "/repl//*/body//Import/*[0]")
#     # _test_with_fs('./', "/repl//*/body//Import//*[0]")
#     # _test_with_fs('./', "/repl//*/body//Import//*[1]")
#     # _test_with_fs('./', "/repl//*/body//Import//*[2]")
#     # _test_with_fs('./', "/repl//*/body//Import//*[3]")
#     # _test_with_fs('./', "/repl//*/body//Import//*[4]")
#     # _test_with_fs('./', "/repl//*/body//Import//*")
#
#     # _test_with_obj({}}, '$regex_extract((hello, yellow, mellow), "low?")')
