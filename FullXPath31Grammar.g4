// ORIGINALLY FORKED FROM https://github.com/antlr/grammars-v4/tree/master/xpath/xpath31 ON Dec15 2024
//
// //a[b[@id = "123"] and position() < 5]/c[starts-with(@name, "test") or contains(@value, "example")]/(d[@type = "primary"] | e[last() - 1])/@*[not(contains(name(), 'ignore'))]

grammar FullXPath31Grammar;


//LEXER
AT         : '@';
BANG       : '!';
CB         : ']';
CC         : '}';
CEQ        : ':=';
COLON      : ':';
COLONCOLON : '::';
COMMA      : ',';
CP         : ')';
CS         : ':*';
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
SC         : '*:';
SLASH      : '/';
SS         : '//';
STAR       : '*';

// KEYWORDS

KW_ANCESTOR               : 'ancestor';
KW_ANCESTOR_OR_SELF       : 'ancestor-or-self';
KW_AND                    : 'and';
KW_ARRAY                  : 'array';
KW_AS                     : 'as';
KW_ATTRIBUTE              : 'attribute';
KW_CAST                   : 'cast';
KW_CASTABLE               : 'castable';
KW_CHILD                  : 'child';
KW_COMMENT                : 'comment';
KW_DESCENDANT             : 'descendant';
KW_DESCENDANT_OR_SELF     : 'descendant-or-self';
KW_DIV                    : 'div';
KW_DOCUMENT_NODE          : 'document-node';
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
KW_NAMESPACE              : 'namespace';
KW_NAMESPACE_NODE         : 'namespace-node';
KW_NE                     : 'ne';
KW_NODE                   : 'node';
KW_OF                     : 'of';
KW_OR                     : 'or';
KW_PARENT                 : 'parent';
KW_PRECEDING              : 'preceding';
KW_PRECEDING_SIBLING      : 'preceding-sibling';
KW_PROCESSING_INSTRUCTION : 'processing-instruction';
KW_RETURN                 : 'return';
KW_SATISFIES              : 'satisfies';
KW_SCHEMA_ATTRIBUTE       : 'schema-attribute';
KW_SCHEMA_ELEMENT         : 'schema-element';
KW_SELF                   : 'self';
KW_SOME                   : 'some';
KW_TEXT                   : 'text';
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
URIQualifiedName : BracedURILiteral NCName;
BracedURILiteral : 'Q' '{' [^{}]* '}';
// Error in spec: EscapeQuot and EscapeApos are not terminals!
fragment FragEscapeQuot : '""';
fragment FragEscapeApos : '\'\'';
// Error in spec: Comment isn't really a terminal, but an off-channel object.
Comment : '(:' (Comment | CommentContents)*? ':)' -> skip;
QName   : FragQName;
NCName  : FragmentNCName;
// Error in spec: Char is not a terminal!
fragment Char            : FragChar;
fragment FragDigits      : [0-9]+;
fragment CommentContents : Char;
// https://www.w3.org/TR/REC-xml-names/#NT-QName
fragment FragQName          : FragPrefixedName | FragUnprefixedName;
fragment FragPrefixedName   : FragPrefix ':' FragLocalPart;
fragment FragUnprefixedName : FragLocalPart;
fragment FragPrefix         : FragmentNCName;
fragment FragLocalPart      : FragmentNCName;
fragment FragNCNameStartChar:
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
fragment FragNCNameChar:
    FragNCNameStartChar
    | '-'
    | '.'
    | '0' ..'9'
    | '\u00B7'
    | '\u0300' ..'\u036F'
    | '\u203F' ..'\u2040'
;
fragment FragmentNCName: FragNCNameStartChar FragNCNameChar*;

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

enclosedexpr
    : OC expr? CC
    ;

expr
    : exprsingle (COMMA exprsingle)*
    ;

exprsingle
    : path                                                      # PathOp
    | exprsingle BANG exprsingle                                # SimpleMapOp
    | <assoc=right> (MINUS | PLUS) exprsingle                   # UnaryOp
    | exprsingle EG arrowfunctionspecifier argumentlist         # ArrowOp
    | exprsingle KW_CAST KW_AS singletype                       # CastOp
    | exprsingle KW_CASTABLE KW_AS singletype                   # CastableOp
    | exprsingle KW_TREAT KW_AS sequencetype                    # TreatOp
    | exprsingle KW_INSTANCE KW_OF sequencetype                 # InstanceOfOp
    | exprsingle (KW_INTERSECT | KW_EXCEPT) exprsingle          # IntersectOp
    | exprsingle (KW_UNION | P) exprsingle                      # UnionOp
    | exprsingle (STAR | KW_DIV | KW_IDIV | KW_MOD) exprsingle  # MultiplicativeOp
    | exprsingle (PLUS | MINUS) exprsingle                      # AdditiveOp
    | exprsingle KW_TO exprsingle                               # RangeOp
    | exprsingle PP exprsingle                                  # StringConcatOp
    | exprsingle comp exprsingle                                # ComparisonOp
    | exprsingle KW_AND exprsingle                              # AndOp
    | exprsingle KW_OR exprsingle                               # OrOp
    | if                                                        # IfExpr
    | quantified                                                # QuantifiedExpr
    | let                                                       # LetExpr
    | for                                                       # ForExpr
    ;

for
    : KW_FOR forbinding (COMMA forbinding)* KW_RETURN exprsingle
    ;

forbinding
    : DOLLAR varname KW_IN exprsingle
    ;

let
    : KW_LET letbinding (COMMA letbinding)* KW_RETURN exprsingle
    ;

letbinding
    : DOLLAR varname CEQ exprsingle
    ;

quantified
    : (KW_SOME | KW_EVERY) quantifiedbinding (COMMA quantifiedbinding)* KW_SATISFIES exprsingle
    ;

quantifiedbinding
    : DOLLAR varname KW_IN exprsingle
    ;

if
    : KW_IF OP expr CP KW_THEN exprsingle KW_ELSE exprsingle
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

//path
//    : SLASH step ((SLASH | SS) step)*  # RootContextPathExpr
//    | SS step ((SLASH | SS) step)*     # AnyContextPathExpr
//    | step ((SLASH | SS) step)*        # RelativeContextPathExpr
//    ;

path
    : SLASH relpath  # PathRootContext
    | SLASH          # PathRootExactContext
    | SS relpath     # PathAnyContext
    | relpath        # PathRelativeContext
    ;

relpath
    : relpath (SLASH | SS) relpath  # RelPathChain
    | step                          # RelPathFinal
    ;

step
    : primaryexpr (predicate | argumentlist | lookup)*  # StepPrimary
    | (reversestep | forwardstep) predicate*            # StepStep
    ;

forwardstep
    : KW_CHILD COLONCOLON nodetest               # ForwardStepChild
    | KW_DESCENDANT COLONCOLON nodetest          # ForwardStepDescendant
    | KW_ATTRIBUTE COLONCOLON nodetest           # ForwardStepAttribute
    | KW_SELF COLONCOLON nodetest                # ForwardStepSelf
    | KW_DESCENDANT_OR_SELF COLONCOLON nodetest  # ForwardStepDescendantOrSelf
    | KW_FOLLOWING_SIBLING COLONCOLON nodetest   # ForwardStepFollowingSibling
    | KW_FOLLOWING COLONCOLON nodetest           # ForwardStepFollowing
    | KW_NAMESPACE COLONCOLON nodetest           # ForwardStepNamespace
    | AT nodetest                                # ForwardStepAttribute
    | nodetest                                   # ForwardStepValue
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
    : kindtest
    | nametest
    ;

nametest
    : eqname
    | wildcard
    ;

wildcard
    : STAR
    | NCName CS
    | SC NCName
    | BracedURILiteral STAR
    ;

argumentlist
    : OP (argument ( COMMA argument)*)? CP
    ;

predicate
    : OB expr CB
    ;

lookup
    : QM keyspecifier
    ;

keyspecifier
    : NCName
    | IntegerLiteral
    | parenthesizedexpr
    | STAR
    ;

arrowfunctionspecifier
    : eqname
    | varref
    | parenthesizedexpr
    ;

primaryexpr
    : literal
    | varref
    | parenthesizedexpr
    | contextitemexpr
    | functioncall
    | functionitemexpr
    | mapconstructor
    | arrayconstructor
    | unarylookup
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

contextitemexpr
    : D
    ;

functioncall
    : eqname argumentlist
    ;

argument
    : exprsingle
    | argumentplaceholder
    ;

argumentplaceholder
    : QM
    ;

functionitemexpr
    : namedfunctionref
    | inlinefunctionexpr
    ;

namedfunctionref
    : eqname POUND IntegerLiteral /* xgc: reserved-function-names */
    ;

inlinefunctionexpr
    : KW_FUNCTION OP paramlist? CP (KW_AS sequencetype)? functionbody
    ;

functionbody
    : enclosedexpr
    ;

paramlist
    : param (COMMA param)*
    ;

param
    : varname typedeclaration?
    ;

mapconstructor
    : KW_MAP OC (mapconstructorentry ( COMMA mapconstructorentry)*)? CC
    ;

mapconstructorentry
    : mapkeyexpr COLON mapvalueexpr
    ;

mapkeyexpr
    : exprsingle
    ;

mapvalueexpr
    : exprsingle
    ;

arrayconstructor
    : squarearrayconstructor
    | curlyarrayconstructor
    ;

squarearrayconstructor
    : OB (exprsingle ( COMMA exprsingle)*)? CB
    ;

curlyarrayconstructor
    : KW_ARRAY enclosedexpr
    ;

unarylookup
    : QM keyspecifier
    ;

singletype
    : typename_ QM?
    ;

typedeclaration
    : KW_AS sequencetype
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
    : kindtest
    | KW_ITEM OP CP
    | functiontest
    | maptest
    | arraytest
    | atomicoruniontype
    | parenthesizeditemtype
    ;

atomicoruniontype
    : eqname
    ;

kindtest
    : documenttest
    | elementtest
    | attributetest
    | schemaelementtest
    | schemaattributetest
    | pitest
    | commenttest
    | texttest
    | namespacenodetest
    | anykindtest
    ;

anykindtest
    : KW_NODE OP CP
    ;

documenttest
    : KW_DOCUMENT_NODE OP (elementtest | schemaelementtest)? CP
    ;

texttest
    : KW_TEXT OP CP
    ;

commenttest
    : KW_COMMENT OP CP
    ;

namespacenodetest
    : KW_NAMESPACE_NODE OP CP
    ;

pitest
    : KW_PROCESSING_INSTRUCTION OP (NCName | StringLiteral)? CP
    ;

attributetest
    : KW_ATTRIBUTE OP (attribnameorwildcard ( COMMA typename_)?)? CP
    ;

attribnameorwildcard
    : attributename
    | STAR
    ;

schemaattributetest
    : KW_SCHEMA_ATTRIBUTE OP attributedeclaration CP
    ;

attributedeclaration
    : attributename
    ;

elementtest
    : KW_ELEMENT OP (elementnameorwildcard ( COMMA typename_ QM?)?)? CP
    ;

elementnameorwildcard
    : elementname
    | STAR
    ;

schemaelementtest
    : KW_SCHEMA_ELEMENT OP elementdeclaration CP
    ;

elementdeclaration
    : elementname
    ;

attributename
    : eqname
    ;

elementname
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
    : QName
    | URIQualifiedName
    ;
