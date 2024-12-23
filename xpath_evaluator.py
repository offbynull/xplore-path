from dataclasses import dataclass
from enum import Enum
from typing import Any, Hashable, Literal, Callable

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from XPath31GrammarLexer import XPath31GrammarLexer
from XPath31GrammarParser import XPath31GrammarParser
from XPath31GrammarVisitor import XPath31GrammarVisitor
from path import Path, PathElement


class PrimeMode(Enum):
    PRIME_WITH_ROOT = 'PRIME_WITH_ROOT'
    PRIME_WITH_SELF = 'PRIME_WITH_SELF'
    PRIME_WITH_EMPTY = 'PRIME_WITH_EMPTY'


@dataclass
class Context:
    original_root: Any
    paths: list[Path]
    state_stack: list[list[Path]]

    def __add__(self, other):
        return Context(self.original_root, self.paths + other.paths, [])

    def __contains__(self, item):
        return item in self.paths

    def __iter__(self):
        return iter(self.paths)

    def __getitem__(self, index):
        return self.paths[index]

    def reset_state(self, new_paths: PrimeMode | list[Path]):
        if isinstance(new_paths, list):
            self.paths = new_paths
        elif new_paths == PrimeMode.PRIME_WITH_ROOT:
            self.paths = [Path([PathElement(None, self.original_root)])]
        elif new_paths == PrimeMode.PRIME_WITH_SELF:
            self.paths = self.state_stack[-1][:]  # copy
        elif new_paths == PrimeMode.PRIME_WITH_EMPTY:
            self.paths = []
        else:
            raise ValueError('This should never happen')

    def push_state(self, new_paths: PrimeMode | list[Path]):
        self.state_stack.append(self.paths)
        self.reset_state(new_paths)

    def pop_state(self) -> list[Path]:
        current_paths = self.paths
        self.paths = self.state_stack.pop()
        return current_paths

    def add_path(self, path: Path):
        self.paths.append(path)

    @staticmethod
    def prime(root_: Any):
        return Context(
            original_root=root_,
            paths=[Path([PathElement(None, root_)])],
            state_stack=[]
        )





def _to_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return [value]

def _coerce_list_to_numbers(values: list[Any]) -> list[float | int]:
    ret = []
    for v in values:
        if isinstance(v, Path):
            v = v.last().value
        if isinstance(v, str):
            try:
                v = int(v)
            except (ValueError, TypeError):
                try:
                    v = float(v)
                except (ValueError, TypeError):
                    ...
        if isinstance(v, (float, int)):
            ret.append(v)
    return ret

def _coerece_to_set(value: list[Any]) -> dict[tuple[Literal['PATH', 'RAW'], Hashable], Any]:
    ret: dict[tuple[Literal['PATH', 'RAW'], Hashable], Any] = {}
    for v in value:
        if isinstance(v, Path):
            ret['PATH', tuple(v.label())] = v
        else:
            ret['RAW', v] = v
    return ret

def _coerece_to_number(value: Any) -> int | float | None:
    if isinstance(value, list) and len(value) == 1:
        value = value[0]
        if isinstance(value, (int, float)):
            return value
        if isinstance(value, str):
            try:
                return int(value)
            except (ValueError, TypeError):
                try:
                    return float(value)
                except (ValueError, TypeError):
                    ...
    elif isinstance(value, str):
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                ...
    elif isinstance(value, (float, int)):
        return value
    return None


class PathEvaluatorVisitor(XPath31GrammarVisitor):
    def __init__(self, root: Any):
        self.root = root
        self.context = Context.prime(root)
        self.context_save_stack = []

    def visitExprPath(self, ctx: XPath31GrammarParser.ExprPathContext):
        return self.visit(ctx.path())

    def visitExprLiteral(self, ctx: XPath31GrammarParser.ExprLiteralContext):
        return self.visit(ctx.literal())

    def visitExprVariable(self, ctx: XPath31GrammarParser.ExprVariableContext):
        raise ValueError('Variables not supported yet')

    def visitExprSimpleMap(self, ctx: XPath31GrammarParser.ExprSimpleMapContext):
        raise ValueError('Not supported')

    def visitExprUnary(self, ctx: XPath31GrammarParser.ExprUnaryContext):
        ret = []
        for p in self.context.paths:
            self.context.push_state([p])
            try:
                inner_res = self.visit(ctx.expr())
                if ctx.MINUS() is not None:
                    inner_res = _coerce_list_to_numbers(inner_res)
                    for v in inner_res:
                        ret.append(-v)
                else:
                    ret += inner_res
            finally:
                self.context.pop_state()
        return ret

    def visitExprConcatenate(self, ctx: XPath31GrammarParser.ExprConcatenateContext):
        l_paths = self.visit(ctx.expr(0))
        r_paths = self.visit(ctx.expr(1))
        return _to_list(l_paths) + _to_list(r_paths)

    def visitExprSetIntersect(self, ctx: XPath31GrammarParser.ExprSetIntersectContext):
        l_paths = _coerece_to_set(self.visit(ctx.expr(0)))
        r_paths = _coerece_to_set(self.visit(ctx.expr(1)))
        intersected_paths = l_paths.keys() & r_paths.keys()
        return list(l_paths[p] for p in intersected_paths)

    def visitExprSetUnion(self, ctx: XPath31GrammarParser.ExprSetUnionContext):
        l_paths = _coerece_to_set(self.visit(ctx.expr(0)))
        r_paths = _coerece_to_set(self.visit(ctx.expr(1)))
        unioned = l_paths | r_paths
        return list(unioned.values())

    def _apply_binary_op(
            self,
            l: int | float | str | list[Any],
            r: int | float | str | list[Any],
            op: Callable[[Any, Any], Any]
    ):
        if isinstance(l, (int, float, str)) and isinstance(r, (int, float, str)):
            return op(l, r)
        elif isinstance(l, (int, float, str)) and isinstance(r, list):
            r_paths = _coerce_list_to_numbers(r)
            return [op(l, r) for r in r_paths]
        elif isinstance(l, list) and isinstance(r, (int, float, str)):
            l_paths = _coerce_list_to_numbers(l)
            return [op(l, r) for l in l_paths]
        elif isinstance(l, list) and isinstance(r, list):
            l_paths = _coerce_list_to_numbers(l)
            r_paths = _coerce_list_to_numbers(r)
            return [op(l, r) for l, r in zip(l_paths, r_paths)]
        raise ValueError('Unexpected data type')

    def visitExprMultiplicative(self, ctx: XPath31GrammarParser.ExprMultiplicativeContext):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if ctx.STAR() is not None:
            return self._apply_binary_op(l, r, lambda _l, _r: _l * _r)
        elif ctx.KW_DIV() is not None:
            return self._apply_binary_op(l, r, lambda _l, _r: _l / _r)
        elif ctx.KW_IDIV() is not None:
            return self._apply_binary_op(l, r, lambda _l, _r: _l // _r)
        elif ctx.KW_MOD() is not None:
            return self._apply_binary_op(l, r, lambda _l, _r: _l % _r)
        raise ValueError('Unexpected')

    def visitExprAdditive(self, ctx: XPath31GrammarParser.ExprAdditiveContext):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if ctx.PLUS() is not None:
            return self._apply_binary_op(l, r, lambda _l, _r: _l + _r)
        elif ctx.MINUS() is not None:
            return self._apply_binary_op(l, r, lambda _l, _r: _l - _r)
        raise ValueError('Unexpected')

    def visitExprRange(self, ctx: XPath31GrammarParser.ExprRangeContext):
        l = _coerece_to_number(self.visit(ctx.expr(0)))
        r = _coerece_to_number(self.visit(ctx.expr(1)))
        if isinstance(l, float) and l.is_integer():
            l = int(l)
        if isinstance(r, float) and r.is_integer():
            r = int(r)
        if isinstance(l, int) and isinstance(r, int):
            return [v for v in range(l, r+1)]
        return []

    def visitExprComparison(self, ctx: XPath31GrammarParser.ExprComparisonContext):
        FILL ME IN
        FILL ME IN
        FILL ME IN
        FILL ME IN
        FILL ME IN

    def visitExprWrap(self, ctx: XPath31GrammarParser.ExprWrapContext):
        return self.visit(ctx.expr())

    def visitExprWrapForceList(self, ctx: XPath31GrammarParser.ExprWrapForceListContext):
        return _to_list(self.visit(ctx.expr()))

    def visitPathRootContext(self, ctx: XPath31GrammarParser.PathRootContextContext):
        try:
            self.context.push_state(new_paths=PrimeMode.PRIME_WITH_ROOT)
            return self.visit(ctx.relpath())
        finally:
            self.context.pop_state()

    def visitPathRootExactContext(self, ctx: XPath31GrammarParser.PathRootExactContextContext):
        try:
            self.context.push_state(new_paths=PrimeMode.PRIME_WITH_ROOT)
            return self.context.paths[:]
        finally:
            self.context.pop_state()

    def visitPathAnyContext(self, ctx: XPath31GrammarParser.PathAnyContextContext):
        try:
            self.context.push_state(new_paths=PrimeMode.PRIME_WITH_ROOT)
            self.context.paths = self.context.paths[0].all_descendants()
            return self.visit(ctx.relpath())
        finally:
            self.context.pop_state()

    def visitPathRelativeContext(self, ctx: XPath31GrammarParser.PathRelativeContextContext):
        try:
            self.context.push_state(new_paths=PrimeMode.PRIME_WITH_SELF)
            return self.visit(ctx.relpath())
        finally:
            self.context.pop_state()

    def visitRelPathChain(self, ctx: XPath31GrammarParser.RelPathChainContext):
        # TODO: Pushing / popping state not required?
        try:
            self.context.push_state(PrimeMode.PRIME_WITH_SELF)
            new_paths = []
            if ctx.SLASH() is not None:
                left_contexts = self.visit(ctx.relpath(0))
                for left_path in left_contexts:
                    self.context.push_state(PrimeMode.PRIME_WITH_EMPTY)
                    self.context.add_path(left_path)
                    right_contexts = self.visit(ctx.relpath(1))
                    for right_path in right_contexts:
                        new_paths.append(right_path)
                    self.context.pop_state()
            elif ctx.SS() is not None:
                raise ValueError('IMPLEMENT ME')
            else:
                raise ValueError('Unexpected')
            return new_paths
        finally:
            self.context.pop_state()

    def visitRelPathStep(self, ctx: XPath31GrammarParser.RelPathStepContext):
        if ctx.forwardstep() is not None:
            ret = self.visit(ctx.forwardstep())
        elif ctx.reversestep() is not None:
            ret = self.visit(ctx.reversestep())
        else:
            raise ValueError('Unexpected')

        for p in ctx.predicate():
            self.context.push_state(ret)
            try:
                ret = self.visit(p)
            finally:
                self.context.pop_state()

        for p in ctx.argumentlist():
            raise ValueError('IMPLEMENT ME')

        return ret

    def visitReverseStepParent(self, ctx: XPath31GrammarParser.ReverseStepParentContext):
        new_paths = []
        for path in self.context:
            parent_path = path.parent()
            if parent_path is not None:
                new_paths.append(parent_path)
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitReverseStepAncestor(self, ctx: XPath31GrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for path in self.context:
            new_paths += path.all_ancestors()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitReverseStepPreceding(self, ctx: XPath31GrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for path in self.context:
            new_paths += path.preceding()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitReverseStepPrecedingSibling(self, ctx: XPath31GrammarParser.ReverseStepPrecedingContext):
        new_paths = []
        for path in self.context:
            new_paths += path.preceding_sibling()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitReverseStepAncestorOrSelf(self, ctx: XPath31GrammarParser.ReverseStepAncestorOrSelfContext):
        new_paths = []
        for path in self.context:
            new_paths.append(path)
            new_paths += path.all_ancestors()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitReverseStepDirectParent(self, ctx: XPath31GrammarParser.ReverseStepDirectParentContext):
        new_paths = []
        for path in self.context:
            parent_path = path.parent()
            if parent_path is not None:
                new_paths.append(parent_path)
        return new_paths

    def visitForwardStepChild(self, ctx: XPath31GrammarParser.ForwardStepChildContext):
        new_paths = []
        for path in self.context:
            new_paths += path.all_children()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitForwardStepDescendant(self, ctx: XPath31GrammarParser.ForwardStepDescendantContext):
        new_paths = []
        for path in self.context:
            new_paths += path.all_descendants()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitForwardStepSelf(self, ctx: XPath31GrammarParser.ForwardStepSelfContext):
        return self.visit(ctx.nodetest())

    def visitForwardStepDescendantOrSelf(self, ctx: XPath31GrammarParser.ForwardStepDescendantOrSelfContext):
        new_paths = []
        for path in self.context:
            new_paths.append(path)
            new_paths += path.all_descendants()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitForwardStepFollowingSibling(self, ctx: XPath31GrammarParser.ForwardStepFollowingSiblingContext):
        new_paths = []
        for path in self.context:
            new_paths += path.following_sibling()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitForwardStepFollowing(self, ctx: XPath31GrammarParser.ForwardStepFollowingContext):
        new_paths = []
        for path in self.context:
            new_paths += path.following()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitForwardStepValue(self, ctx: XPath31GrammarParser.ForwardStepValueContext):
        new_paths = []
        for p in self.context.paths:
            new_paths += p.all_children()
        self.context.reset_state(new_paths)
        return self.visit(ctx.nodetest())

    def visitForwardStepDirectSelf(self, ctx: XPath31GrammarParser.ForwardStepDirectSelfContext):
        return self.context.paths[:]  # Return existing

    def visitNodeTestExact(self, ctx: XPath31GrammarParser.NodeTestExactContext):
        name = ctx.Name().getText()
        return self._label_test([name])

    def _label_test(self, name: list[Any]) -> list[Path]:
        ret = []
        for path in self.context:
            label = path.last().label
            if label in name:  # Direct match?
                ret.append(path)
            elif isinstance(label, int) and isinstance(name, float) and \
                    name.is_integer() and label == int(name):  # int vs float - match?
                ret.append(path)
            elif isinstance(label, float) and isinstance(name, int) and \
                    label.is_integer() and int(label) == name:  # float vs int - match?
                ret.append(path)
            else:  # Coerce to string - match?
                try:
                    label_as_str = str(label)
                    name_as_str = str(name)
                    if label_as_str == name_as_str:
                        ret.append(path)
                except (ValueError, TypeError):
                    ...  # do nothing
        return ret

    def visitNodeTestWildcard(self, ctx: XPath31GrammarParser.NodeTestWildcardContext):
        return self.context.paths[:]  # Return existing

    def visitNodeTestExpr(self, ctx: XPath31GrammarParser.NodeTestExprContext):
        self.context.push_state(PrimeMode.PRIME_WITH_SELF)
        try:
            result = self.visit(ctx.expr())
            if isinstance(result, list):
                result = [p.last().value for p in result]  # assume list of paths, get last value
            else:
                result = [result]
            return self._label_test(result)
        finally:
            self.context.pop_state()

    def visitPredicate(self, ctx: XPath31GrammarParser.PredicateContext):
        orig_paths = self.context.paths
        self.context.push_state(PrimeMode.PRIME_WITH_EMPTY)
        try:
            ret = []
            for p in orig_paths:
                self.context.reset_state([p])
                result = self.visit(ctx.expr())
                if (isinstance(result, bool) and result == True) \
                        or (isinstance(result, int) and result == p.position_in_parent()) \
                        or (isinstance(result, (list, str)) and len(result) > 0):
                    ret.append(p)
            return ret
        finally:
            self.context.pop_state()

    def visitLiteral(self, ctx: XPath31GrammarParser.LiteralContext):
        if ctx.IntegerLiteral() is not None:
            return int(ctx.getText())
        elif ctx.DecimalLiteral() is not None:
            return float(ctx.getText())
        elif ctx.DoubleLiteral() is not None:
            return float(ctx.getText())
        elif ctx.StringLiteral() is not None:
            text = ctx.getText()
            mode = text[0]
            text_decoded = text[1:-1]
            if mode == '"':
                text_decoded = text_decoded.replace('""', '"')
            elif mode == '\'':
                text_decoded = text_decoded.replace('\'\'', '\'')
            else:
                raise ValueError('Unexpected')
            return text_decoded
        raise ValueError('Unexpected')


def test(root, expr):
    print(f'---- res for {expr}')
    input_stream = InputStream(expr)
    lexer = XPath31GrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = XPath31GrammarParser(token_stream)

    tree = parser.expr()

    visitor = PathEvaluatorVisitor(root)
    ret = tree.accept(visitor)

    if isinstance(ret, list):
        for v in ret:
            if isinstance(v, Path):
                print(f'  {v.last()}')
            else:
                print(f'  {v}')
        return ret
    else:
        print(f'  {ret}')


if __name__ == '__main__':
    root = { 'a': { 'b': { 'c': 1, 'd': 2, 'e': -1, 'f': -2 } }, 'y': 3, 'z': 4, 'ptrs': { 'd_ptr': 'd', 'f_ptr': 'f' } }

    # test(root, '/')
    # test(root, '/*')
    # test(root, '/a')
    # test(root, '/a/b')
    # test(root, '/a/*')
    # test(root, '/a/b/c')
    # test(root, '/a/b/d')
    # test(root, '/a/b/*')
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
    # test(root, '/a/b/*[. = /ptrs/*]')  # Test looking up another path to walk forward

    test(root, '-/a/b/*')
    test(root, '-/*')

    test(root, '/a/b/* , /a/b/*')
    test(root, '/a/b/* , /y')

    test(root, '/a/b/* intersect /a/b/*')
    test(root, '/a/b/* intersect (/a/b/c, /a/b/e)')
    test(root, '/a/b/* intersect /y')

    test(root, '/a/b/* union /a/b/*')
    test(root, '/a/b/* union (/a/b/c, /a/b/e)')
    test(root, '/a/b/* union /y')

    test(root, '/a/b/* + /a/b/*')
    test(root, '/a/b/* + 1')
    test(root, '/a/b/* + [1]')  # right is now a sequence - meaning only first elem is added
    test(root, '/a/b/* + [1,2]')  # right is now a sequence - meaning only first elem is added
    test(root, '5+4')

    test(root, '5 to 7')
    test(root, '5.0 to 7')
    test(root, '5 to 7.0')
    test(root, '5.0 to 7.0')
    test(root, '5 to 5')
    test(root, '5 to 4')

    # THESE DONT WORK YET
    # test(root, '/a/b[./d]')  # Predicate - check for child
    # test(root, '/a/b[./x]')  # Predicate - check for child (missing)
    # test(root, '/a/b/*[2]')  # Predicate - position test
