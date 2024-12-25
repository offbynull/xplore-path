# Generated from XPath31Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .XPath31GrammarParser import XPath31GrammarParser
else:
    from XPath31GrammarParser import XPath31GrammarParser

# This class defines a complete generic visitor for a parse tree produced by XPath31GrammarParser.

class XPath31GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XPath31GrammarParser#xpath.
    def visitXpath(self, ctx:XPath31GrammarParser.XpathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprBoolAggregate.
    def visitExprBoolAggregate(self, ctx:XPath31GrammarParser.ExprBoolAggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprSetIntersect.
    def visitExprSetIntersect(self, ctx:XPath31GrammarParser.ExprSetIntersectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprComparison.
    def visitExprComparison(self, ctx:XPath31GrammarParser.ExprComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprMatcher.
    def visitExprMatcher(self, ctx:XPath31GrammarParser.ExprMatcherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprConcatenate.
    def visitExprConcatenate(self, ctx:XPath31GrammarParser.ExprConcatenateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprAdditive.
    def visitExprAdditive(self, ctx:XPath31GrammarParser.ExprAdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprAnd.
    def visitExprAnd(self, ctx:XPath31GrammarParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprWrapForceList.
    def visitExprWrapForceList(self, ctx:XPath31GrammarParser.ExprWrapForceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprWrap.
    def visitExprWrap(self, ctx:XPath31GrammarParser.ExprWrapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprOr.
    def visitExprOr(self, ctx:XPath31GrammarParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprMultiplicative.
    def visitExprMultiplicative(self, ctx:XPath31GrammarParser.ExprMultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprUnary.
    def visitExprUnary(self, ctx:XPath31GrammarParser.ExprUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprSetUnion.
    def visitExprSetUnion(self, ctx:XPath31GrammarParser.ExprSetUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprLiteral.
    def visitExprLiteral(self, ctx:XPath31GrammarParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprRange.
    def visitExprRange(self, ctx:XPath31GrammarParser.ExprRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprPath.
    def visitExprPath(self, ctx:XPath31GrammarParser.ExprPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprVariable.
    def visitExprVariable(self, ctx:XPath31GrammarParser.ExprVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#relop.
    def visitRelop(self, ctx:XPath31GrammarParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#mulop.
    def visitMulop(self, ctx:XPath31GrammarParser.MulopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#addop.
    def visitAddop(self, ctx:XPath31GrammarParser.AddopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathFromRoot.
    def visitPathFromRoot(self, ctx:XPath31GrammarParser.PathFromRootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathRootExact.
    def visitPathRootExact(self, ctx:XPath31GrammarParser.PathRootExactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathFromAny.
    def visitPathFromAny(self, ctx:XPath31GrammarParser.PathFromAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathFromRelative.
    def visitPathFromRelative(self, ctx:XPath31GrammarParser.PathFromRelativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathSelf.
    def visitPathSelf(self, ctx:XPath31GrammarParser.PathSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathParent.
    def visitPathParent(self, ctx:XPath31GrammarParser.PathParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#RelPathStep.
    def visitRelPathStep(self, ctx:XPath31GrammarParser.RelPathStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#RelPathChain.
    def visitRelPathChain(self, ctx:XPath31GrammarParser.RelPathChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ForwardStepChild.
    def visitForwardStepChild(self, ctx:XPath31GrammarParser.ForwardStepChildContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ForwardStepDescendant.
    def visitForwardStepDescendant(self, ctx:XPath31GrammarParser.ForwardStepDescendantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ForwardStepSelf.
    def visitForwardStepSelf(self, ctx:XPath31GrammarParser.ForwardStepSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ForwardStepDescendantOrSelf.
    def visitForwardStepDescendantOrSelf(self, ctx:XPath31GrammarParser.ForwardStepDescendantOrSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ForwardStepFollowingSibling.
    def visitForwardStepFollowingSibling(self, ctx:XPath31GrammarParser.ForwardStepFollowingSiblingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ForwardStepFollowing.
    def visitForwardStepFollowing(self, ctx:XPath31GrammarParser.ForwardStepFollowingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ForwardStepValue.
    def visitForwardStepValue(self, ctx:XPath31GrammarParser.ForwardStepValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ForwardStepDirectSelf.
    def visitForwardStepDirectSelf(self, ctx:XPath31GrammarParser.ForwardStepDirectSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ReverseStepParent.
    def visitReverseStepParent(self, ctx:XPath31GrammarParser.ReverseStepParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ReverseStepAncestor.
    def visitReverseStepAncestor(self, ctx:XPath31GrammarParser.ReverseStepAncestorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ReverseStepPrecedingSibling.
    def visitReverseStepPrecedingSibling(self, ctx:XPath31GrammarParser.ReverseStepPrecedingSiblingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ReverseStepPreceding.
    def visitReverseStepPreceding(self, ctx:XPath31GrammarParser.ReverseStepPrecedingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ReverseStepAncestorOrSelf.
    def visitReverseStepAncestorOrSelf(self, ctx:XPath31GrammarParser.ReverseStepAncestorOrSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ReverseStepDirectParent.
    def visitReverseStepDirectParent(self, ctx:XPath31GrammarParser.ReverseStepDirectParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#argumentlist.
    def visitArgumentlist(self, ctx:XPath31GrammarParser.ArgumentlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#argument.
    def visitArgument(self, ctx:XPath31GrammarParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#predicate.
    def visitPredicate(self, ctx:XPath31GrammarParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#literal.
    def visitLiteral(self, ctx:XPath31GrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#MatcherStrict.
    def visitMatcherStrict(self, ctx:XPath31GrammarParser.MatcherStrictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#MatcherRegex.
    def visitMatcherRegex(self, ctx:XPath31GrammarParser.MatcherRegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#MatcherGlob.
    def visitMatcherGlob(self, ctx:XPath31GrammarParser.MatcherGlobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#MatcherFuzzy.
    def visitMatcherFuzzy(self, ctx:XPath31GrammarParser.MatcherFuzzyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#MatcherWildcard.
    def visitMatcherWildcard(self, ctx:XPath31GrammarParser.MatcherWildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#coerecefallback.
    def visitCoerecefallback(self, ctx:XPath31GrammarParser.CoerecefallbackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#varref.
    def visitVarref(self, ctx:XPath31GrammarParser.VarrefContext):
        return self.visitChildren(ctx)



del XPath31GrammarParser