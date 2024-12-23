// ORIGINALLY FORKED FROM https://github.com/antlr/grammars-v4/tree/master/xpath/xpath31 ON Dec15 2024
//
// //a[b[@id = "123"] and position() < 5]/c[starts-with(@name, "test") or contains(@value, "example")]/(d[@type = "primary"] | e[last() - 1])/@*[not(contains(name(), 'ignore'))]

grammar XPath31Grammar;


//LEXER
BANG       : '!';
CB         : ']';
CC         : '}';
CEQ        : ':=';
COLON      : ':';
COLONCOLON : '::';
COMMA      : ',';
CP         : ')';
D          : '.';
DD         : '..';
DOLLAR     : '$';
EG         : '=>';
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
POUND      : '#';
PP         : '||';
QM         : '?';
SLASH      : '/';
SS         : '//';
STAR       : '*';

// KEYWORDS

KW_ANCESTOR               : 'ancestor';
KW_ANCESTOR_OR_SELF       : 'ancestor-or-self';
KW_AND                    : 'and';
KW_ARRAY                  : 'array';
KW_AS                     : 'as';
KW_CAST                   : 'cast';
KW_CASTABLE               : 'castable';
KW_CHILD                  : 'child';
KW_COMMENT                : 'comment';
KW_DESCENDANT             : 'descendant';
KW_DESCENDANT_OR_SELF     : 'descendant-or-self';
KW_DIV                    : 'div';
KW_ELEMENT                : 'element';
KW_ELSE                   : 'else';
KW_EMPTY_SEQUENCE         : 'empty-sequence';
KW_EQ                     : 'eq';
KW_EVERY                  : 'every';
KW_EXCEPT                 : 'except';
KW_FOLLOWING              : 'following';
KW_FOLLOWING_SIBLING      : 'following-sibling';
KW_FOR                    : 'for';
KW_FUNCTION               : 'function';
KW_GE                     : 'ge';
KW_GT                     : 'gt';
KW_IDIV                   : 'idiv';
KW_IF                     : 'if';
KW_IN                     : 'in';
KW_INSTANCE               : 'instance';
KW_INTERSECT              : 'intersect';
KW_IS                     : 'is';
KW_ITEM                   : 'item';
KW_LE                     : 'le';
KW_LET                    : 'let';
KW_LT                     : 'lt';
KW_MAP                    : 'map';
KW_MOD                    : 'mod';
KW_NE                     : 'ne';
KW_NODE                   : 'node';
KW_OF                     : 'of';
KW_OR                     : 'or';
KW_PARENT                 : 'parent';
KW_PRECEDING              : 'preceding';
KW_PRECEDING_SIBLING      : 'preceding-sibling';
KW_RETURN                 : 'return';
KW_SATISFIES              : 'satisfies';
KW_SELF                   : 'self';
KW_SOME                   : 'some';
KW_THEN                   : 'then';
KW_TO                     : 'to';
KW_TREAT                  : 'treat';
KW_UNION                  : 'union';

// A.2.1. TERMINAL SYMBOLS
// This isn't a complete list of tokens in the language.
// Keywords and symbols are terminals.

IntegerLiteral   : FragDigits;
DecimalLiteral   : '.' FragDigits | FragDigits '.' [0-9]*;
DoubleLiteral    : ('.' FragDigits | FragDigits ('.' [0-9]*)?) [eE] [+-]? FragDigits;
StringLiteral    : '"' (~["] | FragEscapeQuot)* '"' | '\'' (~['] | FragEscapeApos)* '\'';
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
    | expr BANG expr                                # ExprSimpleMap
    | <assoc=right> (MINUS | PLUS) expr             # ExprUnary
    | expr EG arrowfunctionspecifier argumentlist   # ExprArrow
    | expr KW_CAST KW_AS singletype                 # ExprCast
    | expr KW_CASTABLE KW_AS singletype             # ExprCastable
    | expr KW_TREAT KW_AS sequencetype              # ExprTreat
    | expr KW_INSTANCE KW_OF sequencetype           # ExprInstanceOf
    | expr (KW_INTERSECT | KW_EXCEPT) expr          # ExprSetIntersect
    | expr (KW_UNION | P) expr                      # ExprSetUnion
    | expr (COMMA) expr                             # ExprConcatenate
    | expr (STAR | KW_DIV | KW_IDIV | KW_MOD) expr  # ExprMultiplicative
    | expr (PLUS | MINUS) expr                      # ExprAdditive
    | expr KW_TO expr                               # ExprRange
    | expr PP expr                                  # ExprStringConcat
    | expr comp expr                                # ExprComparison
    | expr KW_AND expr                              # ExprAnd
    | expr KW_OR expr                               # ExprOr
    | OP expr CP                                    # ExprWrap
    | if                                            # ExprIf
    | quantified                                    # ExprQuantified
    | let                                           # ExprLet
    | for                                           # ExprFor
    ;

for
    : KW_FOR forbinding (COMMA forbinding)* KW_RETURN expr
    ;

forbinding
    : DOLLAR varname KW_IN expr
    ;

let
    : KW_LET letbinding (COMMA letbinding)* KW_RETURN expr
    ;

letbinding
    : DOLLAR varname CEQ expr
    ;

quantified
    : (KW_SOME | KW_EVERY) quantifiedbinding (COMMA quantifiedbinding)* KW_SATISFIES expr
    ;

quantifiedbinding
    : DOLLAR varname KW_IN expr
    ;

if
    : KW_IF OP expr CP KW_THEN expr KW_ELSE expr
    ;

comp
    : EQ  // This was under generalcomp
    | NE  // This was under generalcomp
    | LT  // This was under generalcomp
    | LE  // This was under generalcomp
    | GT  // This was under generalcomp
    | GE  // This was under generalcomp
    | KW_EQ  // This was under valuecomp
    | KW_NE  // This was under valuecomp
    | KW_LT  // This was under valuecomp
    | KW_LE  // This was under valuecomp
    | KW_GT  // This was under valuecomp
    | KW_GE  // This was under valuecomp
    | KW_IS  // This was under nodecomp
    | LL  // This was under nodecomp
    | GG  // This was under nodecomp
    ;

path
    : SLASH relpath    # PathRootContext
    | SLASH            # PathRootExactContext
    | SS relpath       # PathAnyContext
    | D SLASH relpath  # PathRelativeContext
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
    : eqname                              # NodeTestExact
    | literal                             # NodeTestLiteral
    | varref                              # NodeTestVarRef
    | STAR                                # NodeTestWildcard
    | OP expr CP                          # NodeTestLookupSubExpression
    | OB nodetest ( COMMA nodetest )* CB  # NodeTestUnionMany
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

arrowfunctionspecifier
    : eqname
    | varref
    | parenthesizedexpr
    ;

literal
    : IntegerLiteral
    | DecimalLiteral
    | DoubleLiteral
    | StringLiteral
    ;

varref
    : DOLLAR varname
    ;

varname
    : eqname
    ;

parenthesizedexpr
    : OP expr? CP
    ;

singletype
    : typename_ QM?
    ;

sequencetype
    : KW_EMPTY_SEQUENCE OP CP
    | itemtype occurrenceindicator?
    ;

occurrenceindicator
    : QM
    | STAR
    | PLUS
    ;

itemtype
    : KW_ITEM OP CP
    | functiontest
    | maptest
    | arraytest
    | atomicoruniontype
    | parenthesizeditemtype
    ;

atomicoruniontype
    : eqname
    ;

typename_
    : eqname
    ;

functiontest
    : anyfunctiontest
    | typedfunctiontest
    ;

anyfunctiontest
    : KW_FUNCTION OP STAR CP
    ;

typedfunctiontest
    : KW_FUNCTION OP (sequencetype ( COMMA sequencetype)*)? CP KW_AS sequencetype
    ;

maptest
    : anymaptest
    | typedmaptest
    ;

anymaptest
    : KW_MAP OP STAR CP
    ;

typedmaptest
    : KW_MAP OP atomicoruniontype COMMA sequencetype CP
    ;

arraytest
    : anyarraytest
    | typedarraytest
    ;

anyarraytest
    : KW_ARRAY OP STAR CP
    ;

typedarraytest
    : KW_ARRAY OP sequencetype CP
    ;

parenthesizeditemtype
    : OP itemtype CP
    ;

// Original grammar claimed "Error in the spec. EQName also includes acceptable keywords." To work around this, it included
// "acceptable keywords" (also known as reserved words) into this rule, then used a chunk of code that stopped the rule from
// running if certain "acceptable keywords" were detected? I've simplified the grammar by removing this (at the cost of
// potentially being incorrect).
eqname
    : Name
    ;
