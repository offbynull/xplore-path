// ORIGINALLY FORKED FROM https://github.com/antlr/grammars-v4/tree/master/xpath/xpath31 ON Dec15 2024
//
// //a[b[@id = "123"] and position() < 5]/c[starts-with(@name, "test") or contains(@value, "example")]/(d[@type = "primary"] | e[last() - 1])/@*[not(contains(name(), 'ignore'))]

grammar XPath31Grammar;


//LEXER
BANG       : '!';
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
PLUS       : '+';
QM         : '?';
SLASH      : '/';
SS         : '//';
STAR       : '*';

// KEYWORDS

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
KW_TO                     : 'to';
KW_UNION                  : 'union';
KW_ANY                    : 'any';
KW_ALL                    : 'all';
KW_ZIP                    : 'zip';
KW_PRODUCT                : 'product';

// A.2.1. TERMINAL SYMBOLS
// This isn't a complete list of tokens in the language.
// Keywords and symbols are terminals.

IntegerLiteral   : FragDigits;
DecimalLiteral   : '.' FragDigits | FragDigits '.' [0-9]*;
DoubleLiteral    : ('.' FragDigits | FragDigits ('.' [0-9]*)?) [eE] [+-]? FragDigits;
StringLiteral    : '"' (~["] | FragEscapeQuot)* '"' | '\'' (~['] | FragEscapeApos)* '\'';
BooleanLiteral   : 'true' | 'false';
// Error in spec: EscapeQuot and EscapeApos are not terminals!
fragment FragEscapeQuot : '""';
fragment FragEscapeApos : '\'\'';
// Error in spec: Comment isn't really a terminal, but an off-channel object.
Comment : '(:' (Comment | CommentContents)*? ':)' -> skip;
Name   : FragmentName;
// Error in spec: Char is not a terminal!
fragment Char            : FragChar;
fragment FragDigits      : [0-9]+;
fragment CommentContents : Char;
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
fragment FragmentName: FragNameStartChar FragNameChar*;

// https://www.w3.org/TR/REC-xml/#NT-Char

fragment FragChar:
    '\u0009'
    | '\u000a'
    | '\u000d'
    | '\u0020' ..'\ud7ff'
    | '\ue000' ..'\ufffd'
    | '\u{10000}' ..'\u{10ffff}'
;

// https://github.com/antlr/grammars-v4/blob/17d3db3fd6a8fc319a12176e0bb735b066ec0616/xpath/xpath31/XPath31.g4#L389
Whitespace: ('\u000d' | '\u000a' | '\u0020' | '\u0009')+ -> skip;


//PARSER
xpath
    : expr EOF
    ;

expr
    : path                                          # ExprPath
    | literal                                       # ExprLiteral
    | varref                                        # ExprVariable
    | expr BANG expr                                # ExprSimpleMap
    | <assoc=right> (MINUS | PLUS) expr             # ExprUnary
    | expr (COMMA) expr                             # ExprConcatenate
    | expr (KW_INTERSECT | KW_EXCEPT) expr          # ExprSetIntersect
    | expr (KW_UNION | P) expr                      # ExprSetUnion
    | expr (STAR | KW_DIV | KW_IDIV | KW_MOD) expr  # ExprMultiplicative
    | expr (PLUS | MINUS) expr                      # ExprAdditive
    | expr KW_TO expr                               # ExprRange
    | expr comp expr                                # ExprComparison
    | expr KW_AND expr                              # ExprAnd
    | expr KW_OR expr                               # ExprOr
    | OP expr CP                                    # ExprWrap
    | OB expr CB                                    # ExprWrapForceList
    ;

comp
    : (KW_ZIP | KW_PRODUCT)? (KW_ANY | KW_ALL)?  (EQ | NE | LT | LE | GT | GE | LL | GG)
    | (KW_ANY | KW_ALL)? (KW_ZIP | KW_PRODUCT)? (EQ | NE | LT | LE | GT | GE | LL | GG)
    ;

path
    : SLASH relpath    # PathFromRoot
    | SLASH            # PathRootExact
    | SS relpath       # PathFromAny
    | D SLASH relpath  # PathFromRelative
    | D                # PathSelf
    | DD               # PathParent
    ;

relpath
    : relpath (SLASH | SS) relpath                             # RelPathChain
    | (reversestep | forwardstep) (predicate | argumentlist)*  # RelPathStep
    ;

forwardstep
    : KW_CHILD COLONCOLON nodetest               # ForwardStepChild
    | KW_DESCENDANT COLONCOLON nodetest          # ForwardStepDescendant
    | KW_SELF COLONCOLON nodetest                # ForwardStepSelf
    | KW_DESCENDANT_OR_SELF COLONCOLON nodetest  # ForwardStepDescendantOrSelf
    | KW_FOLLOWING_SIBLING COLONCOLON nodetest   # ForwardStepFollowingSibling
    | KW_FOLLOWING COLONCOLON nodetest           # ForwardStepFollowing
    | nodetest                                   # ForwardStepValue
    | D                                          # ForwardStepDirectSelf
    ;

reversestep
    : KW_PARENT COLONCOLON nodetest             # ReverseStepParent
    | KW_ANCESTOR COLONCOLON nodetest           # ReverseStepAncestor
    | KW_PRECEDING_SIBLING COLONCOLON nodetest  # ReverseStepPrecedingSibling
    | KW_PRECEDING COLONCOLON nodetest          # ReverseStepPreceding
    | KW_ANCESTOR_OR_SELF COLONCOLON nodetest   # ReverseStepAncestorOrSelf
    | DD                                        # ReverseStepDirectParent
    ;

nodetest
    : Name  # NodeTestExact
    | STAR  # NodeTestWildcard
    | expr  # NodeTestExpr
    ;

argumentlist
    : OP (argument ( COMMA argument)*)? CP
    ;

argument
    : expr
    ;

predicate
    : OB expr CB
    ;

literal
    : IntegerLiteral
    | DecimalLiteral
    | DoubleLiteral
    | StringLiteral
    | BooleanLiteral
    ;

varref
    : DOLLAR Name
    ;
