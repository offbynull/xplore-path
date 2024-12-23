from dataclasses import dataclass
from enum import Enum
from typing import Any

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





class PathEvaluatorVisitor(XPath31GrammarVisitor):
    def __init__(self, root: Any):
        self.root = root
        self.context = Context.prime(root)
        self.context_save_stack = []

    def visitExprPath(self, ctx: XPath31GrammarParser.ExprPathContext):
        return self.visit(ctx.path())

    def visitExprConcatenate(self, ctx: XPath31GrammarParser.ExprConcatenateContext):
        l_paths = self.visit(ctx.expr(0))
        r_paths = self.visit(ctx.expr(1))
        return l_paths + r_paths

    def visitExprSetUnion(self, ctx: XPath31GrammarParser.ExprSetUnionContext):
        l_paths = self.visit(ctx.expr(0))
        r_paths = self.visit(ctx.expr(1))
        collapsed_paths = {p.label(): p for p in l_paths} | {p.label(): p for p in r_paths}
        return list(collapsed_paths.values())

    def visitExprSetIntersect(self, ctx: XPath31GrammarParser.ExprSetIntersectContext):
        l_paths = self.visit(ctx.expr(0))
        r_paths = self.visit(ctx.expr(1))
        collapsed_paths = {p.label(): p for p in l_paths} & {p.label(): p for p in r_paths}
        return list(collapsed_paths.values())

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

    def visitNodeTestLiteral(self, ctx: XPath31GrammarParser.NodeTestLiteralContext):
        name = self.visit(ctx.literal())
        return self._label_test([name])

    def visitNodeTestExact(self, ctx: XPath31GrammarParser.NodeTestExactContext):
        name = ctx.eqname().getText()
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

    def visitNodeTestVarRef(self, ctx: XPath31GrammarParser.NodeTestVarRefContext):
        raise ValueError('Variables unsupported')

    def visitNodeTestWildcard(self, ctx: XPath31GrammarParser.NodeTestWildcardContext):
        return self.context.paths[:]  # Return existing

    def visitNodeTestLookupSubExpression(self, ctx: XPath31GrammarParser.NodeTestLookupSubExpressionContext):
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

    def visitNodeTestUnionMany(self, ctx: XPath31GrammarParser.NodeTestUnionManyContext):
        res = []
        for n in ctx.nodetest():
            res += self.visit(n)
        return res

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
    input_stream = InputStream(expr)
    lexer = XPath31GrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = XPath31GrammarParser(token_stream)

    tree = parser.path()

    visitor = PathEvaluatorVisitor(root)
    ret = tree.accept(visitor)

    print(f'---- res for {expr}')
    for v in ret:
        print(f'  {v.last()}')
    return ret


if __name__ == '__main__':
    root = { 'a': { 'b': { 'c': 1, 'd': 2, 'e': -1, 'f': -2 } }, 'y': 3, 'z': 4, 'ptrs': { 'd_ptr': 'd', 'f_ptr': 'f' } }

    test(root, '/')
    test(root, '/*')
    test(root, '/a')
    test(root, '/a/b')
    test(root, '/a/*')
    test(root, '/a/b/c')
    test(root, '/a/b/d')
    test(root, '/a/b/*')
    test(root, '/a/b/following::*')
    test(root, '/a/b/following::z')
    test(root, '/a/b/d/following-sibling::*')
    test(root, '/a/b/d/following-sibling::f')
    test(root, '/a/descendant-or-self::*')
    test(root, '/a/descendant-or-self::d')
    test(root, '/a/descendant::*')
    test(root, '/a/descendant::d')
    test(root, '/a/b/self::*')
    test(root, '/a/b/self::d')
    test(root, '/a/b/self::b')
    test(root, '/a/b/child::*')
    test(root, '/a/b/child::d')

    test(root, '/a/b/..')
    test(root, '/a/b/e/ancestor-or-self::*')
    test(root, '/a/b/e/ancestor-or-self::a')
    test(root, '/y/preceding::*')
    test(root, '/y/preceding::b')
    test(root, '/y/preceding-sibling::*')
    test(root, '/y/preceding-sibling::b')
    test(root, '/a/b/e/parent::*')
    test(root, '/a/b/e/parent::d')
    test(root, '/a/b/e/parent::b')

    test(root, '/a/"b"')  # Test literal in path
    test(root, '/a/"b"/./d')   # Test dot in path
    test(root, '/a/b/(/ptrs/*)')  # Test looking up another path to walk forward
    test(root, '/a/b/[d,f]')  # Test looking up many

    test(root, '/a/b[./d]')  # Predicate - check for child
    test(root, '/a/b[./x]')  # Predicate - check for child (missing)
    test(root, '/a/b/*[2]')  # Predicate - position test
