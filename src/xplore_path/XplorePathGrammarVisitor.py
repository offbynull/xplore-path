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


    # Visit a parse tree produced by XplorePathGrammarParser#expr.
    def visitExpr(self, ctx:XplorePathGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprJoinForward.
    def visitExprJoinForward(self, ctx:XplorePathGrammarParser.ExprJoinForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprJoinHit.
    def visitExprJoinHit(self, ctx:XplorePathGrammarParser.ExprJoinHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprSetIntersectHit.
    def visitExprSetIntersectHit(self, ctx:XplorePathGrammarParser.ExprSetIntersectHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprSetIntersectForward.
    def visitExprSetIntersectForward(self, ctx:XplorePathGrammarParser.ExprSetIntersectForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprSetUnionForward.
    def visitExprSetUnionForward(self, ctx:XplorePathGrammarParser.ExprSetUnionForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprSetUnionHit.
    def visitExprSetUnionHit(self, ctx:XplorePathGrammarParser.ExprSetUnionHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprOrForward.
    def visitExprOrForward(self, ctx:XplorePathGrammarParser.ExprOrForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprOrHit.
    def visitExprOrHit(self, ctx:XplorePathGrammarParser.ExprOrHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprAndHit.
    def visitExprAndHit(self, ctx:XplorePathGrammarParser.ExprAndHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprAndForward.
    def visitExprAndForward(self, ctx:XplorePathGrammarParser.ExprAndForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprNotHit.
    def visitExprNotHit(self, ctx:XplorePathGrammarParser.ExprNotHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprNotForward.
    def visitExprNotForward(self, ctx:XplorePathGrammarParser.ExprNotForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprComparisonForward.
    def visitExprComparisonForward(self, ctx:XplorePathGrammarParser.ExprComparisonForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprComparisonHit.
    def visitExprComparisonHit(self, ctx:XplorePathGrammarParser.ExprComparisonHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprAdditiveForward.
    def visitExprAdditiveForward(self, ctx:XplorePathGrammarParser.ExprAdditiveForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprAdditiveHit.
    def visitExprAdditiveHit(self, ctx:XplorePathGrammarParser.ExprAdditiveHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprMultiplicativeForward.
    def visitExprMultiplicativeForward(self, ctx:XplorePathGrammarParser.ExprMultiplicativeForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprMultiplicativeHit.
    def visitExprMultiplicativeHit(self, ctx:XplorePathGrammarParser.ExprMultiplicativeHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprUnaryNegateHit.
    def visitExprUnaryNegateHit(self, ctx:XplorePathGrammarParser.ExprUnaryNegateHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprUnaryLabelHit.
    def visitExprUnaryLabelHit(self, ctx:XplorePathGrammarParser.ExprUnaryLabelHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprUnaryPositionHit.
    def visitExprUnaryPositionHit(self, ctx:XplorePathGrammarParser.ExprUnaryPositionHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprUnaryAnyAggregateHit.
    def visitExprUnaryAnyAggregateHit(self, ctx:XplorePathGrammarParser.ExprUnaryAnyAggregateHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprUnaryAllAggregateHit.
    def visitExprUnaryAllAggregateHit(self, ctx:XplorePathGrammarParser.ExprUnaryAllAggregateHitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprUnaryForward.
    def visitExprUnaryForward(self, ctx:XplorePathGrammarParser.ExprUnaryForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprPath.
    def visitExprPath(self, ctx:XplorePathGrammarParser.ExprPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprPathInvoke.
    def visitExprPathInvoke(self, ctx:XplorePathGrammarParser.ExprPathInvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprAtomic.
    def visitExprAtomic(self, ctx:XplorePathGrammarParser.ExprAtomicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprWrapOrVar.
    def visitExprWrapOrVar(self, ctx:XplorePathGrammarParser.ExprWrapOrVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprMatcher.
    def visitExprMatcher(self, ctx:XplorePathGrammarParser.ExprMatcherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprLiteral.
    def visitExprLiteral(self, ctx:XplorePathGrammarParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprWrap.
    def visitExprWrap(self, ctx:XplorePathGrammarParser.ExprWrapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprWrapInvoke.
    def visitExprWrapInvoke(self, ctx:XplorePathGrammarParser.ExprWrapInvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprVariable.
    def visitExprVariable(self, ctx:XplorePathGrammarParser.ExprVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#ExprVariableInvoke.
    def visitExprVariableInvoke(self, ctx:XplorePathGrammarParser.ExprVariableInvokeContext):
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


    # Visit a parse tree produced by XplorePathGrammarParser#coerceFallback.
    def visitCoerceFallback(self, ctx:XplorePathGrammarParser.CoerceFallbackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#filter.
    def visitFilter(self, ctx:XplorePathGrammarParser.FilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#varRef.
    def visitVarRef(self, ctx:XplorePathGrammarParser.VarRefContext):
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


    # Visit a parse tree produced by XplorePathGrammarParser#notOp.
    def visitNotOp(self, ctx:XplorePathGrammarParser.NotOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#andOp.
    def visitAndOp(self, ctx:XplorePathGrammarParser.AndOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#orOp.
    def visitOrOp(self, ctx:XplorePathGrammarParser.OrOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#path.
    def visitPath(self, ctx:XplorePathGrammarParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#pathAbsolute.
    def visitPathAbsolute(self, ctx:XplorePathGrammarParser.PathAbsoluteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#pathRelative.
    def visitPathRelative(self, ctx:XplorePathGrammarParser.PathRelativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#pathInner.
    def visitPathInner(self, ctx:XplorePathGrammarParser.PathInnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#pathSeperator.
    def visitPathSeperator(self, ctx:XplorePathGrammarParser.PathSeperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XplorePathGrammarParser#step.
    def visitStep(self, ctx:XplorePathGrammarParser.StepContext):
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



del XplorePathGrammarParser