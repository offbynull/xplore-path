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
KW_FALSE                   : 'false';

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

expr
    : (KW_ANY | KW_ALL) expr coerceFallback?            # ExprBoolAggregate
    | expr joinOp expr joinCond                         # ExprJoin
    | expr (KW_INTERSECT | KW_EXCEPT) expr              # ExprSetIntersect
    | expr (KW_UNION | P) expr                          # ExprSetUnion
    | KW_LABEL expr                                     # ExprExtractLabel
    | KW_POSITION expr                                  # ExprExtractPosition
    | expr orOp expr coerceFallback?                    # ExprOr
    | expr andOp expr coerceFallback?                   # ExprAnd
    | expr relOp expr coerceFallback?                   # ExprComparison
    | expr addOp expr coerceFallback?                   # ExprAdditive
    | expr mulOp expr coerceFallback?                   # ExprMultiplicative
    | atomicOrEncapsulate                               # ExprAtomicOrEncapsulate
    ;

// Why isn't atomicOrEncapsulate directly tied embedded within expr? It was, and the ExprUnary alternative was defined
// as "(MINUS | PLUS) expr". This worked fine except that when you did something like -1-1, it evaluated as -(1-1)
// instead of (-1)-1. The later evaluation is the correct evaluation order, and that's what happens now with this
// current grammar.
atomicOrEncapsulate
    : (MINUS | PLUS) atomicOrEncapsulate coerceFallback?  # ExprUnary
    | wrap filter?                                        # ExprWrap
    | atomicOrEncapsulate argumentList coerceFallback?    # ExprFunctionCall
    | matcher                                             # ExprMatcher
    | varRef                                              # ExprVariable
    | literal                                             # ExprLiteral
    | path filter?                                        # ExprPath
    ;

wrap
    : OP expr CP                                          # ExprWrapSingle
    | OP expr COMMA CP                                    # ExprWrapSingleAsList
    | OP expr COMMA expr (COMMA expr)* COMMA? CP          # ExprWrapConcatenateList
    | OP CP                                               # ExprEmptyList
    ;

argumentList
    : OP (expr (COMMA expr)*)? CP  // BUG: COMMA also being utilized in expr, multiple params misinterpeted as wrapped list
    ;

filter
    : OB expr CB
    ;

joinOp
    : (KW_LEFT | KW_RIGHT | KW_INNER)? KW_JOIN
    ;

joinCond
    : KW_ON filter
    ;

relOp
    : (KW_ZIP | KW_PRODUCT)? (KW_ANY | KW_ALL | KW_SEQUENCE)? (EQ | NE | LT | LE | GT | GE | LL | GG)
    | (KW_SEQUENCE | KW_ANY | KW_ALL)? (KW_ZIP | KW_PRODUCT)? (EQ | NE | LT | LE | GT | GE | LL | GG)
    ;

mulOp
    : (KW_ZIP | KW_PRODUCT)? (STAR | KW_DIV | KW_IDIV | KW_MOD)
    ;

addOp
    : (KW_ZIP | KW_PRODUCT)? (PLUS | MINUS | PP)
    ;

andOp
    : (KW_ZIP | KW_PRODUCT)? (KW_ANY | KW_ALL | KW_SEQUENCE)? KW_AND
    ;

orOp
    : (KW_ZIP | KW_PRODUCT)? (KW_ANY | KW_ALL | KW_SEQUENCE)? KW_OR
    ;

path
    : SLASH filter?                # PathAtRoot
    | SLASH filter? relPath        # PathFromRoot
    | SS filter? relPath           # PathFromRootAny
    | D filter?                    # PathAtSelf
    | D filter? SLASH relPath      # PathFromSelf
    | D filter? SS relPath         # PathFromSelfAny
    | DD filter?                   # PathAtParent
    | DD filter? SLASH relPath     # PathFromParent
    | DD filter? SS relPath        # PathFromParentAny
    | wrap filter? SLASH relPath   # PathFromNested
    | wrap filter? SS relPath      # PathFromNestedAny
    ;

relPath
    : relPath (SLASH | SS) relPath         # RelPathChain
    | (reverseStep | forwardStep) filter?  # RelPathStep
    ;

forwardStep
    : KW_CHILD COLONCOLON atomicOrEncapsulate               # ForwardStepChild
    | KW_DESCENDANT COLONCOLON atomicOrEncapsulate          # ForwardStepDescendant
    | KW_SELF COLONCOLON atomicOrEncapsulate                # ForwardStepSelf
    | KW_DESCENDANT_OR_SELF COLONCOLON atomicOrEncapsulate  # ForwardStepDescendantOrSelf
    | KW_FOLLOWING_SIBLING COLONCOLON atomicOrEncapsulate   # ForwardStepFollowingSibling
    | KW_FOLLOWING COLONCOLON atomicOrEncapsulate           # ForwardStepFollowing
    | D                                                     # ForwardStepDirectSelf
    | atomicOrEncapsulate                                   # ForwardStepValue
    ;

reverseStep
    : KW_PARENT COLONCOLON atomicOrEncapsulate             # ReverseStepParent
    | KW_ANCESTOR COLONCOLON atomicOrEncapsulate           # ReverseStepAncestor
    | KW_PRECEDING_SIBLING COLONCOLON atomicOrEncapsulate  # ReverseStepPrecedingSibling
    | KW_PRECEDING COLONCOLON atomicOrEncapsulate          # ReverseStepPreceding
    | KW_ANCESTOR_OR_SELF COLONCOLON atomicOrEncapsulate   # ReverseStepAncestorOrSelf
    | DD                                                   # ReverseStepDirectParent
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

coerceFallback
    : KW_ON KW_ERROR (KW_DISCARD | KW_FAIL | expr)
    ;

varRef
    : DOLLAR (Name | IntegerLiteral | StringLiteral)
    ;
