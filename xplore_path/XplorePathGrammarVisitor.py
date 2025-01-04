# Generated from XplorePathGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .XplorePathGrammarParser import XplorePathGrammarParser
else:
    from XplorePathGrammarParser import XplorePathGrammarParser

# This class defines a complete generic visitor for a parse tree produced by XplorePathGrammarParser.

class XplorePathGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XplorePathGrammarParser#xplorePath.
    def visitXplorePath(self, ctx:XplorePathGrammarParser.XplorePathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprAnd.
    def visitExprAnd(self, ctx:XplorePathGrammarParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprBoolAggregate.
    def visitExprBoolAggregate(self, ctx:XplorePathGrammarParser.ExprBoolAggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprAtomicOrEncapsulate.
    def visitExprAtomicOrEncapsulate(self, ctx:XplorePathGrammarParser.ExprAtomicOrEncapsulateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprSetIntersect.
    def visitExprSetIntersect(self, ctx:XplorePathGrammarParser.ExprSetIntersectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprComparison.
    def visitExprComparison(self, ctx:XplorePathGrammarParser.ExprComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprExtractLabel.
    def visitExprExtractLabel(self, ctx:XplorePathGrammarParser.ExprExtractLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprExtractPosition.
    def visitExprExtractPosition(self, ctx:XplorePathGrammarParser.ExprExtractPositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprOr.
    def visitExprOr(self, ctx:XplorePathGrammarParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprMultiplicative.
    def visitExprMultiplicative(self, ctx:XplorePathGrammarParser.ExprMultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprSetUnion.
    def visitExprSetUnion(self, ctx:XplorePathGrammarParser.ExprSetUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprJoin.
    def visitExprJoin(self, ctx:XplorePathGrammarParser.ExprJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprAdditive.
    def visitExprAdditive(self, ctx:XplorePathGrammarParser.ExprAdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprMatcher.
    def visitExprMatcher(self, ctx:XplorePathGrammarParser.ExprMatcherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprFunctionCall.
    def visitExprFunctionCall(self, ctx:XplorePathGrammarParser.ExprFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprWrap.
    def visitExprWrap(self, ctx:XplorePathGrammarParser.ExprWrapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprUnary.
    def visitExprUnary(self, ctx:XplorePathGrammarParser.ExprUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprLiteral.
    def visitExprLiteral(self, ctx:XplorePathGrammarParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprPath.
    def visitExprPath(self, ctx:XplorePathGrammarParser.ExprPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprVariable.
    def visitExprVariable(self, ctx:XplorePathGrammarParser.ExprVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprWrapSingle.
    def visitExprWrapSingle(self, ctx:XplorePathGrammarParser.ExprWrapSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprWrapSingleAsList.
    def visitExprWrapSingleAsList(self, ctx:XplorePathGrammarParser.ExprWrapSingleAsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprWrapConcatenateList.
    def visitExprWrapConcatenateList(self, ctx:XplorePathGrammarParser.ExprWrapConcatenateListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprEmptyList.
    def visitExprEmptyList(self, ctx:XplorePathGrammarParser.ExprEmptyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#argumentList.
    def visitArgumentList(self, ctx:XplorePathGrammarParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#filter.
    def visitFilter(self, ctx:XplorePathGrammarParser.FilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#joinOp.
    def visitJoinOp(self, ctx:XplorePathGrammarParser.JoinOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#joinCond.
    def visitJoinCond(self, ctx:XplorePathGrammarParser.JoinCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#relOp.
    def visitRelOp(self, ctx:XplorePathGrammarParser.RelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#mulOp.
    def visitMulOp(self, ctx:XplorePathGrammarParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#addOp.
    def visitAddOp(self, ctx:XplorePathGrammarParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#andOp.
    def visitAndOp(self, ctx:XplorePathGrammarParser.AndOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#orOp.
    def visitOrOp(self, ctx:XplorePathGrammarParser.OrOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathAtRoot.
    def visitPathAtRoot(self, ctx:XplorePathGrammarParser.PathAtRootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathFromRoot.
    def visitPathFromRoot(self, ctx:XplorePathGrammarParser.PathFromRootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathFromRootAny.
    def visitPathFromRootAny(self, ctx:XplorePathGrammarParser.PathFromRootAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathAtSelf.
    def visitPathAtSelf(self, ctx:XplorePathGrammarParser.PathAtSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathFromSelf.
    def visitPathFromSelf(self, ctx:XplorePathGrammarParser.PathFromSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathFromSelfAny.
    def visitPathFromSelfAny(self, ctx:XplorePathGrammarParser.PathFromSelfAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathAtParent.
    def visitPathAtParent(self, ctx:XplorePathGrammarParser.PathAtParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathFromParent.
    def visitPathFromParent(self, ctx:XplorePathGrammarParser.PathFromParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathFromParentAny.
    def visitPathFromParentAny(self, ctx:XplorePathGrammarParser.PathFromParentAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathFromNested.
    def visitPathFromNested(self, ctx:XplorePathGrammarParser.PathFromNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#PathFromNestedAny.
    def visitPathFromNestedAny(self, ctx:XplorePathGrammarParser.PathFromNestedAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#RelPathStep.
    def visitRelPathStep(self, ctx:XplorePathGrammarParser.RelPathStepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#RelPathChain.
    def visitRelPathChain(self, ctx:XplorePathGrammarParser.RelPathChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ForwardStepChild.
    def visitForwardStepChild(self, ctx:XplorePathGrammarParser.ForwardStepChildContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ForwardStepDescendant.
    def visitForwardStepDescendant(self, ctx:XplorePathGrammarParser.ForwardStepDescendantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ForwardStepSelf.
    def visitForwardStepSelf(self, ctx:XplorePathGrammarParser.ForwardStepSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ForwardStepDescendantOrSelf.
    def visitForwardStepDescendantOrSelf(self, ctx:XplorePathGrammarParser.ForwardStepDescendantOrSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ForwardStepFollowingSibling.
    def visitForwardStepFollowingSibling(self, ctx:XplorePathGrammarParser.ForwardStepFollowingSiblingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ForwardStepFollowing.
    def visitForwardStepFollowing(self, ctx:XplorePathGrammarParser.ForwardStepFollowingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ForwardStepDirectSelf.
    def visitForwardStepDirectSelf(self, ctx:XplorePathGrammarParser.ForwardStepDirectSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ForwardStepValue.
    def visitForwardStepValue(self, ctx:XplorePathGrammarParser.ForwardStepValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ReverseStepParent.
    def visitReverseStepParent(self, ctx:XplorePathGrammarParser.ReverseStepParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ReverseStepAncestor.
    def visitReverseStepAncestor(self, ctx:XplorePathGrammarParser.ReverseStepAncestorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ReverseStepPrecedingSibling.
    def visitReverseStepPrecedingSibling(self, ctx:XplorePathGrammarParser.ReverseStepPrecedingSiblingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ReverseStepPreceding.
    def visitReverseStepPreceding(self, ctx:XplorePathGrammarParser.ReverseStepPrecedingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ReverseStepAncestorOrSelf.
    def visitReverseStepAncestorOrSelf(self, ctx:XplorePathGrammarParser.ReverseStepAncestorOrSelfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ReverseStepDirectParent.
    def visitReverseStepDirectParent(self, ctx:XplorePathGrammarParser.ReverseStepDirectParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#literal.
    def visitLiteral(self, ctx:XplorePathGrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#MatcherStrict.
    def visitMatcherStrict(self, ctx:XplorePathGrammarParser.MatcherStrictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#MatcherRegex.
    def visitMatcherRegex(self, ctx:XplorePathGrammarParser.MatcherRegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#MatcherGlob.
    def visitMatcherGlob(self, ctx:XplorePathGrammarParser.MatcherGlobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#MatcherFuzzy.
    def visitMatcherFuzzy(self, ctx:XplorePathGrammarParser.MatcherFuzzyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#MatcherCaseInsensitive.
    def visitMatcherCaseInsensitive(self, ctx:XplorePathGrammarParser.MatcherCaseInsensitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#MatcherNumericRange.
    def visitMatcherNumericRange(self, ctx:XplorePathGrammarParser.MatcherNumericRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#MatcherWildcard.
    def visitMatcherWildcard(self, ctx:XplorePathGrammarParser.MatcherWildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#NumericRangeMatcherInclusive.
    def visitNumericRangeMatcherInclusive(self, ctx:XplorePathGrammarParser.NumericRangeMatcherInclusiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#NumericRangeMatcherBounded.
    def visitNumericRangeMatcherBounded(self, ctx:XplorePathGrammarParser.NumericRangeMatcherBoundedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#NumericRangeMatcherTolerance.
    def visitNumericRangeMatcherTolerance(self, ctx:XplorePathGrammarParser.NumericRangeMatcherToleranceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#numericRangeMatcherLiteral.
    def visitNumericRangeMatcherLiteral(self, ctx:XplorePathGrammarParser.NumericRangeMatcherLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#coerceFallback.
    def visitCoerceFallback(self, ctx:XplorePathGrammarParser.CoerceFallbackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#varRef.
    def visitVarRef(self, ctx:XplorePathGrammarParser.VarRefContext):
        return self.visitChildren(ctx)



del XplorePathGrammarParser