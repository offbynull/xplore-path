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


    # Visit a parse tree produced by XPath31GrammarParser#ExprSetIntersect.
    def visitExprSetIntersect(self, ctx:XPath31GrammarParser.ExprSetIntersectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprComparison.
    def visitExprComparison(self, ctx:XPath31GrammarParser.ExprComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprFor.
    def visitExprFor(self, ctx:XPath31GrammarParser.ExprForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprCastable.
    def visitExprCastable(self, ctx:XPath31GrammarParser.ExprCastableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprConcatenate.
    def visitExprConcatenate(self, ctx:XPath31GrammarParser.ExprConcatenateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprStringConcat.
    def visitExprStringConcat(self, ctx:XPath31GrammarParser.ExprStringConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprAdditive.
    def visitExprAdditive(self, ctx:XPath31GrammarParser.ExprAdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprAnd.
    def visitExprAnd(self, ctx:XPath31GrammarParser.ExprAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprQuantified.
    def visitExprQuantified(self, ctx:XPath31GrammarParser.ExprQuantifiedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprTreat.
    def visitExprTreat(self, ctx:XPath31GrammarParser.ExprTreatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprWrap.
    def visitExprWrap(self, ctx:XPath31GrammarParser.ExprWrapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprLet.
    def visitExprLet(self, ctx:XPath31GrammarParser.ExprLetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprOr.
    def visitExprOr(self, ctx:XPath31GrammarParser.ExprOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprCast.
    def visitExprCast(self, ctx:XPath31GrammarParser.ExprCastContext):
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


    # Visit a parse tree produced by XPath31GrammarParser#ExprInstanceOf.
    def visitExprInstanceOf(self, ctx:XPath31GrammarParser.ExprInstanceOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprRange.
    def visitExprRange(self, ctx:XPath31GrammarParser.ExprRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprIf.
    def visitExprIf(self, ctx:XPath31GrammarParser.ExprIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprPath.
    def visitExprPath(self, ctx:XPath31GrammarParser.ExprPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprSimpleMap.
    def visitExprSimpleMap(self, ctx:XPath31GrammarParser.ExprSimpleMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#ExprArrow.
    def visitExprArrow(self, ctx:XPath31GrammarParser.ExprArrowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#for.
    def visitFor(self, ctx:XPath31GrammarParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#forbinding.
    def visitForbinding(self, ctx:XPath31GrammarParser.ForbindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#let.
    def visitLet(self, ctx:XPath31GrammarParser.LetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#letbinding.
    def visitLetbinding(self, ctx:XPath31GrammarParser.LetbindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#quantified.
    def visitQuantified(self, ctx:XPath31GrammarParser.QuantifiedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#quantifiedbinding.
    def visitQuantifiedbinding(self, ctx:XPath31GrammarParser.QuantifiedbindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#if.
    def visitIf(self, ctx:XPath31GrammarParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#comp.
    def visitComp(self, ctx:XPath31GrammarParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathRootContext.
    def visitPathRootContext(self, ctx:XPath31GrammarParser.PathRootContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathRootExactContext.
    def visitPathRootExactContext(self, ctx:XPath31GrammarParser.PathRootExactContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathAnyContext.
    def visitPathAnyContext(self, ctx:XPath31GrammarParser.PathAnyContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#PathRelativeContext.
    def visitPathRelativeContext(self, ctx:XPath31GrammarParser.PathRelativeContextContext):
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


    # Visit a parse tree produced by XPath31GrammarParser#NodeTestExact.
    def visitNodeTestExact(self, ctx:XPath31GrammarParser.NodeTestExactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#NodeTestLiteral.
    def visitNodeTestLiteral(self, ctx:XPath31GrammarParser.NodeTestLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#NodeTestVarRef.
    def visitNodeTestVarRef(self, ctx:XPath31GrammarParser.NodeTestVarRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#NodeTestWildcard.
    def visitNodeTestWildcard(self, ctx:XPath31GrammarParser.NodeTestWildcardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#NodeTestLookupSubExpression.
    def visitNodeTestLookupSubExpression(self, ctx:XPath31GrammarParser.NodeTestLookupSubExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#NodeTestUnionMany.
    def visitNodeTestUnionMany(self, ctx:XPath31GrammarParser.NodeTestUnionManyContext):
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


    # Visit a parse tree produced by XPath31GrammarParser#arrowfunctionspecifier.
    def visitArrowfunctionspecifier(self, ctx:XPath31GrammarParser.ArrowfunctionspecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#literal.
    def visitLiteral(self, ctx:XPath31GrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#varref.
    def visitVarref(self, ctx:XPath31GrammarParser.VarrefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#varname.
    def visitVarname(self, ctx:XPath31GrammarParser.VarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#parenthesizedexpr.
    def visitParenthesizedexpr(self, ctx:XPath31GrammarParser.ParenthesizedexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#singletype.
    def visitSingletype(self, ctx:XPath31GrammarParser.SingletypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#sequencetype.
    def visitSequencetype(self, ctx:XPath31GrammarParser.SequencetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#occurrenceindicator.
    def visitOccurrenceindicator(self, ctx:XPath31GrammarParser.OccurrenceindicatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#itemtype.
    def visitItemtype(self, ctx:XPath31GrammarParser.ItemtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#atomicoruniontype.
    def visitAtomicoruniontype(self, ctx:XPath31GrammarParser.AtomicoruniontypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#typename_.
    def visitTypename_(self, ctx:XPath31GrammarParser.Typename_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#functiontest.
    def visitFunctiontest(self, ctx:XPath31GrammarParser.FunctiontestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#anyfunctiontest.
    def visitAnyfunctiontest(self, ctx:XPath31GrammarParser.AnyfunctiontestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#typedfunctiontest.
    def visitTypedfunctiontest(self, ctx:XPath31GrammarParser.TypedfunctiontestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#maptest.
    def visitMaptest(self, ctx:XPath31GrammarParser.MaptestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#anymaptest.
    def visitAnymaptest(self, ctx:XPath31GrammarParser.AnymaptestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#typedmaptest.
    def visitTypedmaptest(self, ctx:XPath31GrammarParser.TypedmaptestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#arraytest.
    def visitArraytest(self, ctx:XPath31GrammarParser.ArraytestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#anyarraytest.
    def visitAnyarraytest(self, ctx:XPath31GrammarParser.AnyarraytestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#typedarraytest.
    def visitTypedarraytest(self, ctx:XPath31GrammarParser.TypedarraytestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#parenthesizeditemtype.
    def visitParenthesizeditemtype(self, ctx:XPath31GrammarParser.ParenthesizeditemtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XPath31GrammarParser#eqname.
    def visitEqname(self, ctx:XPath31GrammarParser.EqnameContext):
        return self.visitChildren(ctx)



del XPath31GrammarParser