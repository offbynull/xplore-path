// FORKED FROM https://github.com/antlr/grammars-v4/tree/master/xpath/xpath31 ON Dec15 2024 and heavily modified/refactored
grammar XplorePathGrammar;


//LEXER
TILDE      : '~';
BANG       : '!';
AT         : '@';
CB         : ']';
CC         : '}';
COLON      : ':';
COLONCOLON : '::';
COMMA      : ',';
CP         : ')';
D          : '.';
DD         : '..';
DOLLAR     : '$';
EQ         : '=';
GE         : '>=';
GG         : '>>';
GT         : '>';
LE         : '<=';
LL         : '<<';
LT         : '<';
MINUS      : '-';
NE         : '!=';
OB         : '[';
OC         : '{';
OP         : '(';
P          : '|';
PP         : '||';
PLUS       : '+';
QM         : '?';
SLASH      : '/';
SS         : '//';
STAR       : '*';

KW_ANCESTOR               : 'ancestor';
KW_ANCESTOR_OR_SELF       : 'ancestor-or-self';
KW_AND                    : 'and';
KW_CHILD                  : 'child';
KW_DESCENDANT             : 'descendant';
KW_DESCENDANT_OR_SELF     : 'descendant-or-self';
KW_DIV                    : 'div';
KW_EXCEPT                 : 'except';
KW_FOLLOWING              : 'following';
KW_FOLLOWING_SIBLING      : 'following-sibling';
KW_IDIV                   : 'idiv';
KW_IN                     : 'in';
KW_INTERSECT              : 'intersect';
KW_MOD                    : 'mod';
KW_OR                     : 'or';
KW_PARENT                 : 'parent';
KW_PRECEDING              : 'preceding';
KW_PRECEDING_SIBLING      : 'preceding-sibling';
KW_SELF                   : 'self';
KW_UNION                  : 'union';
KW_ANY                    : 'any';
KW_ALL                    : 'all';
KW_ZIP                    : 'zip';
KW_PRODUCT                : 'product';
KW_EXPAND                 : 'expand';
KW_SEQUENCE               : 'sequence';
KW_ON                     : 'on';
KW_ERROR                  : 'error';
KW_DISCARD                : 'discard';
KW_FAIL                   : 'fail';
KW_NAN                    : 'nan';
KW_INF                    : 'inf';
KW_LABEL                  : 'label';
KW_POSITION               : 'position';
KW_LEFT                   : 'left';
KW_RIGHT                  : 'right';
KW_INNER                  : 'inner';
KW_JOIN                   : 'join';
KW_CONCATENATE            : 'concat';
KW_TRUE                   : 'true';
KW_FALSE                  : 'false';
KW_NOT                    : 'not';
KW_NULL                   : 'null';

RegexMatcher      : 'r' FragStringLiteral;
GlobMatcher       : 'g' FragStringLiteral;
StrictMatcher     : 's' FragStringLiteral;
FuzzyMatcher      : 'f' FragStringLiteral;
IgnoreCaseMatcher : 'i' FragStringLiteral;
IntegerLiteral    : FragDigits;
DecimalLiteral    : '.' FragDigits | FragDigits '.' [0-9]*;
DoubleLiteral     : ('.' FragDigits | FragDigits ('.' [0-9]*)?) [eE] [+-]? FragDigits;
StringLiteral     : FragStringLiteral;
fragment FragStringLiteral : '"' (~["] | FragEscapeQuot)* '"' | '\'' (~['] | FragEscapeApos)* '\'';
fragment FragEscapeQuot : '""';
fragment FragEscapeApos : '\'\'';
Name   : FragNameStartChar FragNameChar*;
fragment FragDigits      : [0-9]+;
// https://www.w3.org/TR/REC-xml-names/#NT-QName
fragment FragNameStartChar:
    'A' ..'Z'
    | '_'
    | 'a' ..'z'
    | '\u00C0' ..'\u00D6'
    | '\u00D8' ..'\u00F6'
    | '\u00F8' ..'\u02FF'
    | '\u0370' ..'\u037D'
    | '\u037F' ..'\u1FFF'
    | '\u200C' ..'\u200D'
    | '\u2070' ..'\u218F'
    | '\u2C00' ..'\u2FEF'
    | '\u3001' ..'\uD7FF'
    | '\uF900' ..'\uFDCF'
    | '\uFDF0' ..'\uFFFD'
    | '\u{10000}' ..'\u{EFFFF}'
;
fragment FragNameChar:
    FragNameStartChar
    | '-'
    | '.'
    | '0' ..'9'
    | '\u00B7'
    | '\u0300' ..'\u036F'
    | '\u203F' ..'\u2040'
;

Whitespace: ('\u000d' | '\u000a' | '\u0020' | '\u0009')+ -> skip;


//PARSER
xplorePath
    : expr EOF
    ;

// TODO: Having "coerceFallback?" at the end of expr's recursive alternatives introduces an ambiguity. For example,
//       think of the expression "5+4*3 on error discard" . There are two possible places where "coerceFallback"s
//       can be applied - which of the two "coerceFallback" does it get it assigned to?
//
//                   INTERPRETATION 1                                              INTERPRETATION 2
//
//            5 + 4 * 3 on error discard                                         5 + 4 * 3 on error discard
//               '----------------------' inner expr                 inner expr     '-----'
//           '--------------------------' outer expr                 outer expr '---------------------------'
expr: exprJoin;

exprJoin
    : exprJoin joinOp exprSetIntersect joinCond                 # ExprJoinHit
    | exprSetIntersect                                          # ExprJoinForward
    ;
exprSetIntersect
    : exprSetIntersect (KW_INTERSECT | KW_EXCEPT) exprSetUnion  # ExprSetIntersectHit
    | exprSetUnion                                              # ExprSetIntersectForward
    ;
exprSetUnion
    : exprSetUnion (KW_UNION | P) exprOr                        # ExprSetUnionHit
    | exprOr                                                    # ExprSetUnionForward
    ;
exprOr
    : exprOr orOp exprAnd coerceFallback?                       # ExprOrHit
    | exprAnd                                                   # ExprOrForward
    ;
exprAnd
    : exprAnd andOp exprNot coerceFallback?                     # ExprAndHit
    | exprNot                                                   # ExprAndForward
    ;
exprNot
    : notOp exprNot coerceFallback?                             # ExprNotHit
    | exprComparison                                            # ExprNotForward
    ;
exprComparison
    : exprComparison relOp exprAdditive coerceFallback?         # ExprComparisonHit
    | exprAdditive                                              # ExprComparisonForward
    ;
exprAdditive
    : exprAdditive addOp exprMultiplicative coerceFallback?     # ExprAdditiveHit
    | exprMultiplicative                                        # ExprAdditiveForward
    ;
exprMultiplicative
    : exprMultiplicative mulOp exprUnary coerceFallback?        # ExprMultiplicativeHit
    | exprUnary                                                 # ExprMultiplicativeForward
    ;
exprUnary
    : (MINUS | PLUS) exprUnary coerceFallback?                  # ExprUnaryNegateHit
    | KW_LABEL exprUnary                                        # ExprUnaryLabelHit
    | KW_POSITION exprUnary                                     # ExprUnaryPositionHit
    | KW_ANY exprUnary coerceFallback?                          # ExprUnaryAnyAggregateHit
    | KW_ALL exprUnary coerceFallback?                          # ExprUnaryAllAggregateHit
    | exprPathOrAtomic                                          # ExprUnaryForward
    ;
exprPathOrAtomic
    : path                                                      # ExprPath        // REMINDER: Don't do "path filter? ..." - it'll cause ambiguity because each path element ends with "filter?" - so if there's a filter after the last element, it doesn't know which rule it should apply to (the element's filter or this rule's filter)
    | path argumentList filter?                                 # ExprPathInvoke  // REMINDER: Don't do "path filter? ..." - it'll cause ambiguity because each path element ends with "filter?" - so if there's a filter after the last element, it doesn't know which rule it should apply to (the element's filter or this rule's filter)
    | atomic                                                    # ExprAtomic
    ;

atomic
    : wrapOrVar                                           # ExprWrapOrVar
    | matcher                                             # ExprMatcher
    | literal                                             # ExprLiteral
    ;

wrapOrVar
    : wrap filter?                                        # ExprWrap
    | wrap filter? argumentList filter?                   # ExprWrapInvoke
    | varRef filter?                                      # ExprVariable
    | varRef filter? argumentList filter?                 # ExprVariableInvoke
    ;

wrap
    : OP expr CP                                           # ExprWrapSingle
    | OP expr COMMA CP                                     # ExprWrapSingleAsList
    | OP expr COMMA expr (COMMA expr)* COMMA? CP           # ExprWrapConcatenateList
    | OP CP                                                # ExprEmptyList
    ;

argumentList
    : OP (expr (COMMA expr)*)? CP
    ;

coerceFallback
    : KW_ON KW_ERROR (KW_DISCARD | KW_FAIL | expr)
    ;

filter
    : OB expr CB
    ;

varRef
    : DOLLAR (Name | IntegerLiteral | StringLiteral)
    ;

joinOp
    : (KW_LEFT | KW_RIGHT | KW_INNER)? KW_JOIN
    ;

joinCond
    : KW_ON filter
    ;

relOp
    : (KW_ZIP | KW_PRODUCT)? (KW_ANY | KW_ALL | KW_SEQUENCE)? (EQ | NE | LT | LE | GT | GE | LL | GG)
    ;

mulOp
    : (KW_ZIP | KW_PRODUCT)? (STAR | KW_DIV | KW_IDIV | KW_MOD)
    ;

addOp
    : (KW_ZIP | KW_PRODUCT)? (PLUS | MINUS | PP)
    ;

notOp
    : KW_EXPAND? KW_NOT
    ;

andOp
    : KW_EXPAND? (KW_ZIP | KW_PRODUCT)? (KW_ANY | KW_ALL | KW_SEQUENCE)? KW_AND
    ;

orOp
    : KW_EXPAND? (KW_ZIP | KW_PRODUCT)? (KW_ANY | KW_ALL | KW_SEQUENCE)? KW_OR
    ;

path
    : pathAbsolute | pathRelative
    ;

pathAbsolute
    : (SLASH filter? pathInner?)
    | (SS pathInner)
    ;

pathRelative
    : ((D | DD) filter? pathAbsolute?)
    | (wrapOrVar pathAbsolute)
    ;

pathInner
    : step (pathSeperator step)*
    ;

pathSeperator
    : SLASH | SS | QM
    ;

step
    : (reverseStep | forwardStep) filter?
    ;

forwardStep
    : KW_CHILD COLONCOLON atomic               # ForwardStepChild
    | KW_DESCENDANT COLONCOLON atomic          # ForwardStepDescendant
    | KW_SELF COLONCOLON atomic                # ForwardStepSelf
    | KW_DESCENDANT_OR_SELF COLONCOLON atomic  # ForwardStepDescendantOrSelf
    | KW_FOLLOWING_SIBLING COLONCOLON atomic   # ForwardStepFollowingSibling
    | KW_FOLLOWING COLONCOLON atomic           # ForwardStepFollowing
    | D                                        # ForwardStepDirectSelf
    | atomic                                   # ForwardStepValue
    ;

reverseStep
    : KW_PARENT COLONCOLON atomic             # ReverseStepParent
    | KW_ANCESTOR COLONCOLON atomic           # ReverseStepAncestor
    | KW_PRECEDING_SIBLING COLONCOLON atomic  # ReverseStepPrecedingSibling
    | KW_PRECEDING COLONCOLON atomic          # ReverseStepPreceding
    | KW_ANCESTOR_OR_SELF COLONCOLON atomic   # ReverseStepAncestorOrSelf
    | DD                                      # ReverseStepDirectParent
    ;

literal
    : IntegerLiteral
    | DecimalLiteral
    | DoubleLiteral
    | StringLiteral
    | (KW_TRUE | KW_FALSE)
    | KW_NAN
    | KW_INF
    | Name
    | KW_NULL
    ;

matcher
    : StrictMatcher        # MatcherStrict
    | RegexMatcher         # MatcherRegex
    | GlobMatcher          # MatcherGlob
    | FuzzyMatcher         # MatcherFuzzy
    | IgnoreCaseMatcher    # MatcherCaseInsensitive
    | numericRangeMatcher  # MatcherNumericRange
    | STAR                 # MatcherWildcard
    ;

numericRangeMatcher
    : TILDE numericRangeMatcherLiteral COLON numericRangeMatcherLiteral                      # NumericRangeMatcherInclusive
    | TILDE (OP | OB) numericRangeMatcherLiteral COLON numericRangeMatcherLiteral (CP | CB)  # NumericRangeMatcherBounded
    | TILDE numericRangeMatcherLiteral (AT numericRangeMatcherLiteral)?                      # NumericRangeMatcherTolerance
    ;

numericRangeMatcherLiteral
    : MINUS? (IntegerLiteral | DecimalLiteral | DoubleLiteral | KW_INF)
    ;
