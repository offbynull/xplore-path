# Generated from XPath31Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .XPath31GrammarParser import XPath31GrammarParser
else:
    from XPath31GrammarParser import XPath31GrammarParser

# This class defines a complete listener for a parse tree produced by XPath31GrammarParser.
class XPath31GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by XPath31GrammarParser#xpath.
    def enterXpath(self, ctx:XPath31GrammarParser.XpathContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#xpath.
    def exitXpath(self, ctx:XPath31GrammarParser.XpathContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprBoolAggregate.
    def enterExprBoolAggregate(self, ctx:XPath31GrammarParser.ExprBoolAggregateContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprBoolAggregate.
    def exitExprBoolAggregate(self, ctx:XPath31GrammarParser.ExprBoolAggregateContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprSetIntersect.
    def enterExprSetIntersect(self, ctx:XPath31GrammarParser.ExprSetIntersectContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprSetIntersect.
    def exitExprSetIntersect(self, ctx:XPath31GrammarParser.ExprSetIntersectContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprComparison.
    def enterExprComparison(self, ctx:XPath31GrammarParser.ExprComparisonContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprComparison.
    def exitExprComparison(self, ctx:XPath31GrammarParser.ExprComparisonContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprMatcher.
    def enterExprMatcher(self, ctx:XPath31GrammarParser.ExprMatcherContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprMatcher.
    def exitExprMatcher(self, ctx:XPath31GrammarParser.ExprMatcherContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprConcatenate.
    def enterExprConcatenate(self, ctx:XPath31GrammarParser.ExprConcatenateContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprConcatenate.
    def exitExprConcatenate(self, ctx:XPath31GrammarParser.ExprConcatenateContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprAdditive.
    def enterExprAdditive(self, ctx:XPath31GrammarParser.ExprAdditiveContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprAdditive.
    def exitExprAdditive(self, ctx:XPath31GrammarParser.ExprAdditiveContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprAnd.
    def enterExprAnd(self, ctx:XPath31GrammarParser.ExprAndContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprAnd.
    def exitExprAnd(self, ctx:XPath31GrammarParser.ExprAndContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprWrapForceList.
    def enterExprWrapForceList(self, ctx:XPath31GrammarParser.ExprWrapForceListContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprWrapForceList.
    def exitExprWrapForceList(self, ctx:XPath31GrammarParser.ExprWrapForceListContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprWrap.
    def enterExprWrap(self, ctx:XPath31GrammarParser.ExprWrapContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprWrap.
    def exitExprWrap(self, ctx:XPath31GrammarParser.ExprWrapContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprOr.
    def enterExprOr(self, ctx:XPath31GrammarParser.ExprOrContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprOr.
    def exitExprOr(self, ctx:XPath31GrammarParser.ExprOrContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprMultiplicative.
    def enterExprMultiplicative(self, ctx:XPath31GrammarParser.ExprMultiplicativeContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprMultiplicative.
    def exitExprMultiplicative(self, ctx:XPath31GrammarParser.ExprMultiplicativeContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprUnary.
    def enterExprUnary(self, ctx:XPath31GrammarParser.ExprUnaryContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprUnary.
    def exitExprUnary(self, ctx:XPath31GrammarParser.ExprUnaryContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprSetUnion.
    def enterExprSetUnion(self, ctx:XPath31GrammarParser.ExprSetUnionContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprSetUnion.
    def exitExprSetUnion(self, ctx:XPath31GrammarParser.ExprSetUnionContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprLiteral.
    def enterExprLiteral(self, ctx:XPath31GrammarParser.ExprLiteralContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprLiteral.
    def exitExprLiteral(self, ctx:XPath31GrammarParser.ExprLiteralContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprRange.
    def enterExprRange(self, ctx:XPath31GrammarParser.ExprRangeContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprRange.
    def exitExprRange(self, ctx:XPath31GrammarParser.ExprRangeContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprPath.
    def enterExprPath(self, ctx:XPath31GrammarParser.ExprPathContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprPath.
    def exitExprPath(self, ctx:XPath31GrammarParser.ExprPathContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ExprVariable.
    def enterExprVariable(self, ctx:XPath31GrammarParser.ExprVariableContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ExprVariable.
    def exitExprVariable(self, ctx:XPath31GrammarParser.ExprVariableContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#relop.
    def enterRelop(self, ctx:XPath31GrammarParser.RelopContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#relop.
    def exitRelop(self, ctx:XPath31GrammarParser.RelopContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#mulop.
    def enterMulop(self, ctx:XPath31GrammarParser.MulopContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#mulop.
    def exitMulop(self, ctx:XPath31GrammarParser.MulopContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#addop.
    def enterAddop(self, ctx:XPath31GrammarParser.AddopContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#addop.
    def exitAddop(self, ctx:XPath31GrammarParser.AddopContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#PathFromRoot.
    def enterPathFromRoot(self, ctx:XPath31GrammarParser.PathFromRootContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#PathFromRoot.
    def exitPathFromRoot(self, ctx:XPath31GrammarParser.PathFromRootContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#PathRootExact.
    def enterPathRootExact(self, ctx:XPath31GrammarParser.PathRootExactContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#PathRootExact.
    def exitPathRootExact(self, ctx:XPath31GrammarParser.PathRootExactContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#PathFromAny.
    def enterPathFromAny(self, ctx:XPath31GrammarParser.PathFromAnyContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#PathFromAny.
    def exitPathFromAny(self, ctx:XPath31GrammarParser.PathFromAnyContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#PathFromRelative.
    def enterPathFromRelative(self, ctx:XPath31GrammarParser.PathFromRelativeContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#PathFromRelative.
    def exitPathFromRelative(self, ctx:XPath31GrammarParser.PathFromRelativeContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#PathSelf.
    def enterPathSelf(self, ctx:XPath31GrammarParser.PathSelfContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#PathSelf.
    def exitPathSelf(self, ctx:XPath31GrammarParser.PathSelfContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#PathParent.
    def enterPathParent(self, ctx:XPath31GrammarParser.PathParentContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#PathParent.
    def exitPathParent(self, ctx:XPath31GrammarParser.PathParentContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#RelPathStep.
    def enterRelPathStep(self, ctx:XPath31GrammarParser.RelPathStepContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#RelPathStep.
    def exitRelPathStep(self, ctx:XPath31GrammarParser.RelPathStepContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#RelPathChain.
    def enterRelPathChain(self, ctx:XPath31GrammarParser.RelPathChainContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#RelPathChain.
    def exitRelPathChain(self, ctx:XPath31GrammarParser.RelPathChainContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ForwardStepChild.
    def enterForwardStepChild(self, ctx:XPath31GrammarParser.ForwardStepChildContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ForwardStepChild.
    def exitForwardStepChild(self, ctx:XPath31GrammarParser.ForwardStepChildContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ForwardStepDescendant.
    def enterForwardStepDescendant(self, ctx:XPath31GrammarParser.ForwardStepDescendantContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ForwardStepDescendant.
    def exitForwardStepDescendant(self, ctx:XPath31GrammarParser.ForwardStepDescendantContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ForwardStepSelf.
    def enterForwardStepSelf(self, ctx:XPath31GrammarParser.ForwardStepSelfContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ForwardStepSelf.
    def exitForwardStepSelf(self, ctx:XPath31GrammarParser.ForwardStepSelfContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ForwardStepDescendantOrSelf.
    def enterForwardStepDescendantOrSelf(self, ctx:XPath31GrammarParser.ForwardStepDescendantOrSelfContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ForwardStepDescendantOrSelf.
    def exitForwardStepDescendantOrSelf(self, ctx:XPath31GrammarParser.ForwardStepDescendantOrSelfContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ForwardStepFollowingSibling.
    def enterForwardStepFollowingSibling(self, ctx:XPath31GrammarParser.ForwardStepFollowingSiblingContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ForwardStepFollowingSibling.
    def exitForwardStepFollowingSibling(self, ctx:XPath31GrammarParser.ForwardStepFollowingSiblingContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ForwardStepFollowing.
    def enterForwardStepFollowing(self, ctx:XPath31GrammarParser.ForwardStepFollowingContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ForwardStepFollowing.
    def exitForwardStepFollowing(self, ctx:XPath31GrammarParser.ForwardStepFollowingContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ForwardStepValue.
    def enterForwardStepValue(self, ctx:XPath31GrammarParser.ForwardStepValueContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ForwardStepValue.
    def exitForwardStepValue(self, ctx:XPath31GrammarParser.ForwardStepValueContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ForwardStepDirectSelf.
    def enterForwardStepDirectSelf(self, ctx:XPath31GrammarParser.ForwardStepDirectSelfContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ForwardStepDirectSelf.
    def exitForwardStepDirectSelf(self, ctx:XPath31GrammarParser.ForwardStepDirectSelfContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ReverseStepParent.
    def enterReverseStepParent(self, ctx:XPath31GrammarParser.ReverseStepParentContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ReverseStepParent.
    def exitReverseStepParent(self, ctx:XPath31GrammarParser.ReverseStepParentContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ReverseStepAncestor.
    def enterReverseStepAncestor(self, ctx:XPath31GrammarParser.ReverseStepAncestorContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ReverseStepAncestor.
    def exitReverseStepAncestor(self, ctx:XPath31GrammarParser.ReverseStepAncestorContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ReverseStepPrecedingSibling.
    def enterReverseStepPrecedingSibling(self, ctx:XPath31GrammarParser.ReverseStepPrecedingSiblingContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ReverseStepPrecedingSibling.
    def exitReverseStepPrecedingSibling(self, ctx:XPath31GrammarParser.ReverseStepPrecedingSiblingContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ReverseStepPreceding.
    def enterReverseStepPreceding(self, ctx:XPath31GrammarParser.ReverseStepPrecedingContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ReverseStepPreceding.
    def exitReverseStepPreceding(self, ctx:XPath31GrammarParser.ReverseStepPrecedingContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ReverseStepAncestorOrSelf.
    def enterReverseStepAncestorOrSelf(self, ctx:XPath31GrammarParser.ReverseStepAncestorOrSelfContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ReverseStepAncestorOrSelf.
    def exitReverseStepAncestorOrSelf(self, ctx:XPath31GrammarParser.ReverseStepAncestorOrSelfContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#ReverseStepDirectParent.
    def enterReverseStepDirectParent(self, ctx:XPath31GrammarParser.ReverseStepDirectParentContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#ReverseStepDirectParent.
    def exitReverseStepDirectParent(self, ctx:XPath31GrammarParser.ReverseStepDirectParentContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#argumentlist.
    def enterArgumentlist(self, ctx:XPath31GrammarParser.ArgumentlistContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#argumentlist.
    def exitArgumentlist(self, ctx:XPath31GrammarParser.ArgumentlistContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#argument.
    def enterArgument(self, ctx:XPath31GrammarParser.ArgumentContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#argument.
    def exitArgument(self, ctx:XPath31GrammarParser.ArgumentContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#predicate.
    def enterPredicate(self, ctx:XPath31GrammarParser.PredicateContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#predicate.
    def exitPredicate(self, ctx:XPath31GrammarParser.PredicateContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#literal.
    def enterLiteral(self, ctx:XPath31GrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#literal.
    def exitLiteral(self, ctx:XPath31GrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#MatcherStrict.
    def enterMatcherStrict(self, ctx:XPath31GrammarParser.MatcherStrictContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#MatcherStrict.
    def exitMatcherStrict(self, ctx:XPath31GrammarParser.MatcherStrictContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#MatcherRegex.
    def enterMatcherRegex(self, ctx:XPath31GrammarParser.MatcherRegexContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#MatcherRegex.
    def exitMatcherRegex(self, ctx:XPath31GrammarParser.MatcherRegexContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#MatcherGlob.
    def enterMatcherGlob(self, ctx:XPath31GrammarParser.MatcherGlobContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#MatcherGlob.
    def exitMatcherGlob(self, ctx:XPath31GrammarParser.MatcherGlobContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#MatcherFuzzy.
    def enterMatcherFuzzy(self, ctx:XPath31GrammarParser.MatcherFuzzyContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#MatcherFuzzy.
    def exitMatcherFuzzy(self, ctx:XPath31GrammarParser.MatcherFuzzyContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#MatcherWildcard.
    def enterMatcherWildcard(self, ctx:XPath31GrammarParser.MatcherWildcardContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#MatcherWildcard.
    def exitMatcherWildcard(self, ctx:XPath31GrammarParser.MatcherWildcardContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#coerecefallback.
    def enterCoerecefallback(self, ctx:XPath31GrammarParser.CoerecefallbackContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#coerecefallback.
    def exitCoerecefallback(self, ctx:XPath31GrammarParser.CoerecefallbackContext):
        pass


    # Enter a parse tree produced by XPath31GrammarParser#varref.
    def enterVarref(self, ctx:XPath31GrammarParser.VarrefContext):
        pass

    # Exit a parse tree produced by XPath31GrammarParser#varref.
    def exitVarref(self, ctx:XPath31GrammarParser.VarrefContext):
        pass



del XPath31GrammarParser