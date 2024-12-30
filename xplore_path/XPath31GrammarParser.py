# Generated from XPath31Grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,76,311,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,48,8,1,1,1,1,1,1,1,3,1,53,8,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,71,
        8,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,1,1,1,1,1,1,1,3,1,83,8,1,1,1,1,
        1,1,1,1,1,3,1,89,8,1,1,1,1,1,1,1,1,1,3,1,95,8,1,5,1,97,8,1,10,1,
        12,1,100,9,1,1,2,1,2,1,2,1,2,3,2,106,8,2,1,2,1,2,1,2,1,2,3,2,112,
        8,2,1,2,1,2,3,2,116,8,2,1,2,1,2,3,2,120,8,2,1,2,1,2,1,2,1,2,1,2,
        3,2,127,8,2,3,2,129,8,2,1,2,1,2,1,2,3,2,134,8,2,5,2,136,8,2,10,2,
        12,2,139,9,2,1,3,1,3,1,3,1,3,5,3,145,8,3,10,3,12,3,148,9,3,3,3,150,
        8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,3,5,159,8,5,1,5,3,5,162,8,5,1,5,
        1,5,3,5,166,8,5,1,5,3,5,169,8,5,1,5,3,5,172,8,5,1,6,3,6,175,8,6,
        1,6,1,6,1,7,3,7,180,8,7,1,7,1,7,1,8,3,8,185,8,8,1,8,3,8,188,8,8,
        1,8,1,8,1,9,3,9,193,8,9,1,9,3,9,196,8,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,210,8,10,1,11,1,11,1,11,3,
        11,215,8,11,1,11,1,11,1,11,5,11,220,8,11,10,11,12,11,223,9,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,245,8,12,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,
        13,263,8,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,274,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,292,8,16,3,16,294,8,16,1,17,3,17,297,8,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,306,8,18,1,19,1,19,1,
        19,1,19,0,3,2,4,22,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,0,15,1,0,53,54,2,0,39,39,44,44,2,0,25,25,52,52,2,0,20,
        20,27,27,1,0,55,56,2,0,53,54,57,57,2,0,13,19,21,21,4,0,31,31,38,
        38,42,42,45,45,2,0,20,20,26,27,1,0,29,30,2,0,62,63,70,75,2,0,22,
        22,24,24,2,0,4,4,9,9,2,0,63,63,70,72,3,0,70,70,73,73,75,75,364,0,
        40,1,0,0,0,2,52,1,0,0,0,4,128,1,0,0,0,6,140,1,0,0,0,8,153,1,0,0,
        0,10,171,1,0,0,0,12,174,1,0,0,0,14,179,1,0,0,0,16,184,1,0,0,0,18,
        192,1,0,0,0,20,209,1,0,0,0,22,211,1,0,0,0,24,244,1,0,0,0,26,262,
        1,0,0,0,28,264,1,0,0,0,30,273,1,0,0,0,32,293,1,0,0,0,34,296,1,0,
        0,0,36,300,1,0,0,0,38,307,1,0,0,0,40,41,3,2,1,0,41,42,5,0,0,1,42,
        1,1,0,0,0,43,44,6,1,-1,0,44,45,7,0,0,0,45,47,3,2,1,0,46,48,3,36,
        18,0,47,46,1,0,0,0,47,48,1,0,0,0,48,53,1,0,0,0,49,50,5,64,0,0,50,
        53,3,2,1,7,51,53,3,4,2,0,52,43,1,0,0,0,52,49,1,0,0,0,52,51,1,0,0,
        0,53,98,1,0,0,0,54,55,10,11,0,0,55,56,5,8,0,0,56,97,3,2,1,12,57,
        58,10,10,0,0,58,59,7,1,0,0,59,97,3,2,1,11,60,61,10,9,0,0,61,62,7,
        2,0,0,62,97,3,2,1,10,63,64,10,8,0,0,64,65,5,51,0,0,65,97,3,2,1,9,
        66,67,10,6,0,0,67,68,3,18,9,0,68,70,3,2,1,0,69,71,3,36,18,0,70,69,
        1,0,0,0,70,71,1,0,0,0,71,97,1,0,0,0,72,73,10,5,0,0,73,74,3,16,8,
        0,74,76,3,2,1,0,75,77,3,36,18,0,76,75,1,0,0,0,76,77,1,0,0,0,77,97,
        1,0,0,0,78,79,10,4,0,0,79,80,3,10,5,0,80,82,3,2,1,0,81,83,3,36,18,
        0,82,81,1,0,0,0,82,83,1,0,0,0,83,97,1,0,0,0,84,85,10,3,0,0,85,86,
        3,14,7,0,86,88,3,2,1,0,87,89,3,36,18,0,88,87,1,0,0,0,88,89,1,0,0,
        0,89,97,1,0,0,0,90,91,10,2,0,0,91,92,3,12,6,0,92,94,3,2,1,0,93,95,
        3,36,18,0,94,93,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,54,1,0,0,
        0,96,57,1,0,0,0,96,60,1,0,0,0,96,63,1,0,0,0,96,66,1,0,0,0,96,72,
        1,0,0,0,96,78,1,0,0,0,96,84,1,0,0,0,96,90,1,0,0,0,97,100,1,0,0,0,
        98,96,1,0,0,0,98,99,1,0,0,0,99,3,1,0,0,0,100,98,1,0,0,0,101,102,
        6,2,-1,0,102,103,7,3,0,0,103,105,3,4,2,0,104,106,3,36,18,0,105,104,
        1,0,0,0,105,106,1,0,0,0,106,129,1,0,0,0,107,108,5,24,0,0,108,109,
        3,2,1,0,109,111,5,9,0,0,110,112,3,8,4,0,111,110,1,0,0,0,111,112,
        1,0,0,0,112,129,1,0,0,0,113,115,5,22,0,0,114,116,3,2,1,0,115,114,
        1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,119,5,4,0,0,118,120,
        3,8,4,0,119,118,1,0,0,0,119,120,1,0,0,0,120,129,1,0,0,0,121,129,
        3,30,15,0,122,129,3,38,19,0,123,129,3,28,14,0,124,126,3,20,10,0,
        125,127,3,8,4,0,126,125,1,0,0,0,126,127,1,0,0,0,127,129,1,0,0,0,
        128,101,1,0,0,0,128,107,1,0,0,0,128,113,1,0,0,0,128,121,1,0,0,0,
        128,122,1,0,0,0,128,123,1,0,0,0,128,124,1,0,0,0,129,137,1,0,0,0,
        130,131,10,5,0,0,131,133,3,6,3,0,132,134,3,36,18,0,133,132,1,0,0,
        0,133,134,1,0,0,0,134,136,1,0,0,0,135,130,1,0,0,0,136,139,1,0,0,
        0,137,135,1,0,0,0,137,138,1,0,0,0,138,5,1,0,0,0,139,137,1,0,0,0,
        140,149,5,24,0,0,141,146,3,2,1,0,142,143,5,8,0,0,143,145,3,2,1,0,
        144,142,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,
        147,150,1,0,0,0,148,146,1,0,0,0,149,141,1,0,0,0,149,150,1,0,0,0,
        150,151,1,0,0,0,151,152,5,9,0,0,152,7,1,0,0,0,153,154,5,22,0,0,154,
        155,3,2,1,0,155,156,5,4,0,0,156,9,1,0,0,0,157,159,7,4,0,0,158,157,
        1,0,0,0,158,159,1,0,0,0,159,161,1,0,0,0,160,162,7,5,0,0,161,160,
        1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,172,7,6,0,0,164,166,
        7,5,0,0,165,164,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,167,169,
        7,4,0,0,168,167,1,0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,170,172,
        7,6,0,0,171,158,1,0,0,0,171,165,1,0,0,0,172,11,1,0,0,0,173,175,7,
        4,0,0,174,173,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,7,
        7,0,0,177,13,1,0,0,0,178,180,7,4,0,0,179,178,1,0,0,0,179,180,1,0,
        0,0,180,181,1,0,0,0,181,182,7,8,0,0,182,15,1,0,0,0,183,185,7,4,0,
        0,184,183,1,0,0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,188,7,5,0,
        0,187,186,1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,5,34,0,
        0,190,17,1,0,0,0,191,193,7,4,0,0,192,191,1,0,0,0,192,193,1,0,0,0,
        193,195,1,0,0,0,194,196,7,5,0,0,195,194,1,0,0,0,195,196,1,0,0,0,
        196,197,1,0,0,0,197,198,5,46,0,0,198,19,1,0,0,0,199,200,5,29,0,0,
        200,210,3,22,11,0,201,210,5,29,0,0,202,203,5,30,0,0,203,210,3,22,
        11,0,204,205,5,10,0,0,205,206,5,29,0,0,206,210,3,22,11,0,207,210,
        5,10,0,0,208,210,5,11,0,0,209,199,1,0,0,0,209,201,1,0,0,0,209,202,
        1,0,0,0,209,204,1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,21,1,
        0,0,0,211,214,6,11,-1,0,212,215,3,26,13,0,213,215,3,24,12,0,214,
        212,1,0,0,0,214,213,1,0,0,0,215,221,1,0,0,0,216,217,10,2,0,0,217,
        218,7,9,0,0,218,220,3,22,11,3,219,216,1,0,0,0,220,223,1,0,0,0,221,
        219,1,0,0,0,221,222,1,0,0,0,222,23,1,0,0,0,223,221,1,0,0,0,224,225,
        5,35,0,0,225,226,5,7,0,0,226,245,3,4,2,0,227,228,5,36,0,0,228,229,
        5,7,0,0,229,245,3,4,2,0,230,231,5,50,0,0,231,232,5,7,0,0,232,245,
        3,4,2,0,233,234,5,37,0,0,234,235,5,7,0,0,235,245,3,4,2,0,236,237,
        5,41,0,0,237,238,5,7,0,0,238,245,3,4,2,0,239,240,5,40,0,0,240,241,
        5,7,0,0,241,245,3,4,2,0,242,245,5,10,0,0,243,245,3,4,2,0,244,224,
        1,0,0,0,244,227,1,0,0,0,244,230,1,0,0,0,244,233,1,0,0,0,244,236,
        1,0,0,0,244,239,1,0,0,0,244,242,1,0,0,0,244,243,1,0,0,0,245,25,1,
        0,0,0,246,247,5,47,0,0,247,248,5,7,0,0,248,263,3,4,2,0,249,250,5,
        32,0,0,250,251,5,7,0,0,251,263,3,4,2,0,252,253,5,49,0,0,253,254,
        5,7,0,0,254,263,3,4,2,0,255,256,5,48,0,0,256,257,5,7,0,0,257,263,
        3,4,2,0,258,259,5,33,0,0,259,260,5,7,0,0,260,263,3,4,2,0,261,263,
        5,11,0,0,262,246,1,0,0,0,262,249,1,0,0,0,262,252,1,0,0,0,262,255,
        1,0,0,0,262,258,1,0,0,0,262,261,1,0,0,0,263,27,1,0,0,0,264,265,7,
        10,0,0,265,29,1,0,0,0,266,274,5,67,0,0,267,274,5,65,0,0,268,274,
        5,66,0,0,269,274,5,68,0,0,270,274,5,69,0,0,271,274,3,32,16,0,272,
        274,5,31,0,0,273,266,1,0,0,0,273,267,1,0,0,0,273,268,1,0,0,0,273,
        269,1,0,0,0,273,270,1,0,0,0,273,271,1,0,0,0,273,272,1,0,0,0,274,
        31,1,0,0,0,275,276,5,1,0,0,276,277,3,34,17,0,277,278,5,6,0,0,278,
        279,3,34,17,0,279,294,1,0,0,0,280,281,5,1,0,0,281,282,7,11,0,0,282,
        283,3,34,17,0,283,284,5,6,0,0,284,285,3,34,17,0,285,286,7,12,0,0,
        286,294,1,0,0,0,287,288,5,1,0,0,288,291,3,34,17,0,289,290,5,3,0,
        0,290,292,3,34,17,0,291,289,1,0,0,0,291,292,1,0,0,0,292,294,1,0,
        0,0,293,275,1,0,0,0,293,280,1,0,0,0,293,287,1,0,0,0,294,33,1,0,0,
        0,295,297,5,20,0,0,296,295,1,0,0,0,296,297,1,0,0,0,297,298,1,0,0,
        0,298,299,7,13,0,0,299,35,1,0,0,0,300,301,5,58,0,0,301,305,5,59,
        0,0,302,306,5,60,0,0,303,306,5,61,0,0,304,306,3,2,1,0,305,302,1,
        0,0,0,305,303,1,0,0,0,305,304,1,0,0,0,306,37,1,0,0,0,307,308,5,12,
        0,0,308,309,7,14,0,0,309,39,1,0,0,0,40,47,52,70,76,82,88,94,96,98,
        105,111,115,119,126,128,133,137,146,149,158,161,165,168,171,174,
        179,184,187,192,195,209,214,221,244,262,273,291,293,296,305
    ]

class XPath31GrammarParser ( Parser ):

    grammarFileName = "XPath31Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'~'", "'!'", "'@'", "']'", "'}'", "':'", 
                     "'::'", "','", "')'", "'.'", "'..'", "'$'", "'='", 
                     "'>='", "'>>'", "'>'", "'<='", "'<<'", "'<'", "'-'", 
                     "'!='", "'['", "'{'", "'('", "'|'", "'||'", "'+'", 
                     "'?'", "'/'", "'//'", "'*'", "'ancestor'", "'ancestor-or-self'", 
                     "'and'", "'child'", "'descendant'", "'descendant-or-self'", 
                     "'div'", "'except'", "'following'", "'following-sibling'", 
                     "'idiv'", "'in'", "'intersect'", "'mod'", "'or'", "'parent'", 
                     "'preceding'", "'preceding-sibling'", "'self'", "'to'", 
                     "'union'", "'any'", "'all'", "'zip'", "'product'", 
                     "'sequence'", "'on'", "'error'", "'discard'", "'fail'", 
                     "'nan'", "'inf'", "'label'" ]

    symbolicNames = [ "<INVALID>", "TILDE", "BANG", "AT", "CB", "CC", "COLON", 
                      "COLONCOLON", "COMMA", "CP", "D", "DD", "DOLLAR", 
                      "EQ", "GE", "GG", "GT", "LE", "LL", "LT", "MINUS", 
                      "NE", "OB", "OC", "OP", "P", "PP", "PLUS", "QM", "SLASH", 
                      "SS", "STAR", "KW_ANCESTOR", "KW_ANCESTOR_OR_SELF", 
                      "KW_AND", "KW_CHILD", "KW_DESCENDANT", "KW_DESCENDANT_OR_SELF", 
                      "KW_DIV", "KW_EXCEPT", "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", 
                      "KW_IDIV", "KW_IN", "KW_INTERSECT", "KW_MOD", "KW_OR", 
                      "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
                      "KW_SELF", "KW_TO", "KW_UNION", "KW_ANY", "KW_ALL", 
                      "KW_ZIP", "KW_PRODUCT", "KW_SEQUENCE", "KW_ON", "KW_ERROR", 
                      "KW_DISCARD", "KW_FAIL", "KW_NAN", "KW_INF", "KW_LABEL", 
                      "RegexMatcher", "GlobMatcher", "StrictMatcher", "FuzzyMatcher", 
                      "IgnoreCaseMatcher", "IntegerLiteral", "DecimalLiteral", 
                      "DoubleLiteral", "StringLiteral", "BooleanLiteral", 
                      "Name", "Whitespace" ]

    RULE_xplorePath = 0
    RULE_expr = 1
    RULE_atomicOrEncapsulate = 2
    RULE_argumentList = 3
    RULE_filter = 4
    RULE_relOp = 5
    RULE_mulOp = 6
    RULE_addOp = 7
    RULE_andOp = 8
    RULE_orOp = 9
    RULE_path = 10
    RULE_relPath = 11
    RULE_forwardStep = 12
    RULE_reverseStep = 13
    RULE_literal = 14
    RULE_matcher = 15
    RULE_numericRangeMatcher = 16
    RULE_numericRangeMatcherLiteral = 17
    RULE_coerceFallback = 18
    RULE_varRef = 19

    ruleNames =  [ "xplorePath", "expr", "atomicOrEncapsulate", "argumentList", 
                   "filter", "relOp", "mulOp", "addOp", "andOp", "orOp", 
                   "path", "relPath", "forwardStep", "reverseStep", "literal", 
                   "matcher", "numericRangeMatcher", "numericRangeMatcherLiteral", 
                   "coerceFallback", "varRef" ]

    EOF = Token.EOF
    TILDE=1
    BANG=2
    AT=3
    CB=4
    CC=5
    COLON=6
    COLONCOLON=7
    COMMA=8
    CP=9
    D=10
    DD=11
    DOLLAR=12
    EQ=13
    GE=14
    GG=15
    GT=16
    LE=17
    LL=18
    LT=19
    MINUS=20
    NE=21
    OB=22
    OC=23
    OP=24
    P=25
    PP=26
    PLUS=27
    QM=28
    SLASH=29
    SS=30
    STAR=31
    KW_ANCESTOR=32
    KW_ANCESTOR_OR_SELF=33
    KW_AND=34
    KW_CHILD=35
    KW_DESCENDANT=36
    KW_DESCENDANT_OR_SELF=37
    KW_DIV=38
    KW_EXCEPT=39
    KW_FOLLOWING=40
    KW_FOLLOWING_SIBLING=41
    KW_IDIV=42
    KW_IN=43
    KW_INTERSECT=44
    KW_MOD=45
    KW_OR=46
    KW_PARENT=47
    KW_PRECEDING=48
    KW_PRECEDING_SIBLING=49
    KW_SELF=50
    KW_TO=51
    KW_UNION=52
    KW_ANY=53
    KW_ALL=54
    KW_ZIP=55
    KW_PRODUCT=56
    KW_SEQUENCE=57
    KW_ON=58
    KW_ERROR=59
    KW_DISCARD=60
    KW_FAIL=61
    KW_NAN=62
    KW_INF=63
    KW_LABEL=64
    RegexMatcher=65
    GlobMatcher=66
    StrictMatcher=67
    FuzzyMatcher=68
    IgnoreCaseMatcher=69
    IntegerLiteral=70
    DecimalLiteral=71
    DoubleLiteral=72
    StringLiteral=73
    BooleanLiteral=74
    Name=75
    Whitespace=76

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class XplorePathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


        def EOF(self):
            return self.getToken(XPath31GrammarParser.EOF, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_xplorePath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXplorePath" ):
                listener.enterXplorePath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXplorePath" ):
                listener.exitXplorePath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXplorePath" ):
                return visitor.visitXplorePath(self)
            else:
                return visitor.visitChildren(self)




    def xplorePath(self):

        localctx = XPath31GrammarParser.XplorePathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_xplorePath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.expr(0)
            self.state = 41
            self.match(XPath31GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def andOp(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AndOpContext,0)

        def coerceFallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerceFallbackContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAnd" ):
                listener.enterExprAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAnd" ):
                listener.exitExprAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAnd" ):
                return visitor.visitExprAnd(self)
            else:
                return visitor.visitChildren(self)


    class ExprBoolAggregateContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)

        def KW_ANY(self):
            return self.getToken(XPath31GrammarParser.KW_ANY, 0)
        def KW_ALL(self):
            return self.getToken(XPath31GrammarParser.KW_ALL, 0)
        def coerceFallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerceFallbackContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBoolAggregate" ):
                listener.enterExprBoolAggregate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBoolAggregate" ):
                listener.exitExprBoolAggregate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBoolAggregate" ):
                return visitor.visitExprBoolAggregate(self)
            else:
                return visitor.visitChildren(self)


    class ExprAtomicOrEncapsulateContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAtomicOrEncapsulate" ):
                listener.enterExprAtomicOrEncapsulate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAtomicOrEncapsulate" ):
                listener.exitExprAtomicOrEncapsulate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAtomicOrEncapsulate" ):
                return visitor.visitExprAtomicOrEncapsulate(self)
            else:
                return visitor.visitChildren(self)


    class ExprSetIntersectContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def KW_INTERSECT(self):
            return self.getToken(XPath31GrammarParser.KW_INTERSECT, 0)
        def KW_EXCEPT(self):
            return self.getToken(XPath31GrammarParser.KW_EXCEPT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSetIntersect" ):
                listener.enterExprSetIntersect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSetIntersect" ):
                listener.exitExprSetIntersect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSetIntersect" ):
                return visitor.visitExprSetIntersect(self)
            else:
                return visitor.visitChildren(self)


    class ExprComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def relOp(self):
            return self.getTypedRuleContext(XPath31GrammarParser.RelOpContext,0)

        def coerceFallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerceFallbackContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprComparison" ):
                listener.enterExprComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprComparison" ):
                listener.exitExprComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprComparison" ):
                return visitor.visitExprComparison(self)
            else:
                return visitor.visitChildren(self)


    class ExprExtractLabelContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_LABEL(self):
            return self.getToken(XPath31GrammarParser.KW_LABEL, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprExtractLabel" ):
                listener.enterExprExtractLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprExtractLabel" ):
                listener.exitExprExtractLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprExtractLabel" ):
                return visitor.visitExprExtractLabel(self)
            else:
                return visitor.visitChildren(self)


    class ExprOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def orOp(self):
            return self.getTypedRuleContext(XPath31GrammarParser.OrOpContext,0)

        def coerceFallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerceFallbackContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprOr" ):
                listener.enterExprOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprOr" ):
                listener.exitExprOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprOr" ):
                return visitor.visitExprOr(self)
            else:
                return visitor.visitChildren(self)


    class ExprMultiplicativeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def mulOp(self):
            return self.getTypedRuleContext(XPath31GrammarParser.MulOpContext,0)

        def coerceFallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerceFallbackContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMultiplicative" ):
                listener.enterExprMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMultiplicative" ):
                listener.exitExprMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMultiplicative" ):
                return visitor.visitExprMultiplicative(self)
            else:
                return visitor.visitChildren(self)


    class ExprConcatenateContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(XPath31GrammarParser.COMMA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprConcatenate" ):
                listener.enterExprConcatenate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprConcatenate" ):
                listener.exitExprConcatenate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprConcatenate" ):
                return visitor.visitExprConcatenate(self)
            else:
                return visitor.visitChildren(self)


    class ExprSetUnionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def KW_UNION(self):
            return self.getToken(XPath31GrammarParser.KW_UNION, 0)
        def P(self):
            return self.getToken(XPath31GrammarParser.P, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprSetUnion" ):
                listener.enterExprSetUnion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprSetUnion" ):
                listener.exitExprSetUnion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprSetUnion" ):
                return visitor.visitExprSetUnion(self)
            else:
                return visitor.visitChildren(self)


    class ExprRangeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def KW_TO(self):
            return self.getToken(XPath31GrammarParser.KW_TO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRange" ):
                listener.enterExprRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRange" ):
                listener.exitExprRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRange" ):
                return visitor.visitExprRange(self)
            else:
                return visitor.visitChildren(self)


    class ExprAdditiveContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def addOp(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AddOpContext,0)

        def coerceFallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerceFallbackContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAdditive" ):
                listener.enterExprAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAdditive" ):
                listener.exitExprAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAdditive" ):
                return visitor.visitExprAdditive(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XPath31GrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53, 54]:
                localctx = XPath31GrammarParser.ExprBoolAggregateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                _la = self._input.LA(1)
                if not(_la==53 or _la==54):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
                self.expr(0)
                self.state = 47
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 46
                    self.coerceFallback()


                pass
            elif token in [64]:
                localctx = XPath31GrammarParser.ExprExtractLabelContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(XPath31GrammarParser.KW_LABEL)
                self.state = 50
                self.expr(7)
                pass
            elif token in [1, 10, 11, 12, 20, 22, 24, 27, 29, 30, 31, 62, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]:
                localctx = XPath31GrammarParser.ExprAtomicOrEncapsulateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.atomicOrEncapsulate(0)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 96
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = XPath31GrammarParser.ExprConcatenateContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 55
                        self.match(XPath31GrammarParser.COMMA)
                        self.state = 56
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = XPath31GrammarParser.ExprSetIntersectContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not(_la==39 or _la==44):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = XPath31GrammarParser.ExprSetUnionContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 61
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==52):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = XPath31GrammarParser.ExprRangeContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 64
                        self.match(XPath31GrammarParser.KW_TO)
                        self.state = 65
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = XPath31GrammarParser.ExprOrContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 67
                        self.orOp()
                        self.state = 68
                        self.expr(0)
                        self.state = 70
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                        if la_ == 1:
                            self.state = 69
                            self.coerceFallback()


                        pass

                    elif la_ == 6:
                        localctx = XPath31GrammarParser.ExprAndContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 73
                        self.andOp()
                        self.state = 74
                        self.expr(0)
                        self.state = 76
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                        if la_ == 1:
                            self.state = 75
                            self.coerceFallback()


                        pass

                    elif la_ == 7:
                        localctx = XPath31GrammarParser.ExprComparisonContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 79
                        self.relOp()
                        self.state = 80
                        self.expr(0)
                        self.state = 82
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                        if la_ == 1:
                            self.state = 81
                            self.coerceFallback()


                        pass

                    elif la_ == 8:
                        localctx = XPath31GrammarParser.ExprAdditiveContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 85
                        self.addOp()
                        self.state = 86
                        self.expr(0)
                        self.state = 88
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                        if la_ == 1:
                            self.state = 87
                            self.coerceFallback()


                        pass

                    elif la_ == 9:
                        localctx = XPath31GrammarParser.ExprMultiplicativeContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 91
                        self.mulOp()
                        self.state = 92
                        self.expr(0)
                        self.state = 94
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                        if la_ == 1:
                            self.state = 93
                            self.coerceFallback()


                        pass

             
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomicOrEncapsulateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_atomicOrEncapsulate

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprWrapForceListContext(AtomicOrEncapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicOrEncapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OB(self):
            return self.getToken(XPath31GrammarParser.OB, 0)
        def CB(self):
            return self.getToken(XPath31GrammarParser.CB, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)

        def filter_(self):
            return self.getTypedRuleContext(XPath31GrammarParser.FilterContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprWrapForceList" ):
                listener.enterExprWrapForceList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprWrapForceList" ):
                listener.exitExprWrapForceList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprWrapForceList" ):
                return visitor.visitExprWrapForceList(self)
            else:
                return visitor.visitChildren(self)


    class ExprMatcherContext(AtomicOrEncapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicOrEncapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def matcher(self):
            return self.getTypedRuleContext(XPath31GrammarParser.MatcherContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprMatcher" ):
                listener.enterExprMatcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprMatcher" ):
                listener.exitExprMatcher(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMatcher" ):
                return visitor.visitExprMatcher(self)
            else:
                return visitor.visitChildren(self)


    class ExprFunctionCallContext(AtomicOrEncapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicOrEncapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)

        def argumentList(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ArgumentListContext,0)

        def coerceFallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerceFallbackContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprFunctionCall" ):
                listener.enterExprFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprFunctionCall" ):
                listener.exitExprFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFunctionCall" ):
                return visitor.visitExprFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class ExprWrapContext(AtomicOrEncapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicOrEncapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP(self):
            return self.getToken(XPath31GrammarParser.OP, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)

        def CP(self):
            return self.getToken(XPath31GrammarParser.CP, 0)
        def filter_(self):
            return self.getTypedRuleContext(XPath31GrammarParser.FilterContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprWrap" ):
                listener.enterExprWrap(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprWrap" ):
                listener.exitExprWrap(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprWrap" ):
                return visitor.visitExprWrap(self)
            else:
                return visitor.visitChildren(self)


    class ExprUnaryContext(AtomicOrEncapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicOrEncapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)

        def MINUS(self):
            return self.getToken(XPath31GrammarParser.MINUS, 0)
        def PLUS(self):
            return self.getToken(XPath31GrammarParser.PLUS, 0)
        def coerceFallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerceFallbackContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprUnary" ):
                listener.enterExprUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprUnary" ):
                listener.exitExprUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprUnary" ):
                return visitor.visitExprUnary(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralContext(AtomicOrEncapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicOrEncapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(XPath31GrammarParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLiteral" ):
                listener.enterExprLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLiteral" ):
                listener.exitExprLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteral" ):
                return visitor.visitExprLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ExprPathContext(AtomicOrEncapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicOrEncapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def path(self):
            return self.getTypedRuleContext(XPath31GrammarParser.PathContext,0)

        def filter_(self):
            return self.getTypedRuleContext(XPath31GrammarParser.FilterContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPath" ):
                listener.enterExprPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPath" ):
                listener.exitExprPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPath" ):
                return visitor.visitExprPath(self)
            else:
                return visitor.visitChildren(self)


    class ExprVariableContext(AtomicOrEncapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicOrEncapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varRef(self):
            return self.getTypedRuleContext(XPath31GrammarParser.VarRefContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprVariable" ):
                listener.enterExprVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprVariable" ):
                listener.exitExprVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprVariable" ):
                return visitor.visitExprVariable(self)
            else:
                return visitor.visitChildren(self)



    def atomicOrEncapsulate(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XPath31GrammarParser.AtomicOrEncapsulateContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_atomicOrEncapsulate, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 27]:
                localctx = XPath31GrammarParser.ExprUnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 102
                _la = self._input.LA(1)
                if not(_la==20 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 103
                self.atomicOrEncapsulate(0)
                self.state = 105
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 104
                    self.coerceFallback()


                pass
            elif token in [24]:
                localctx = XPath31GrammarParser.ExprWrapContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(XPath31GrammarParser.OP)
                self.state = 108
                self.expr(0)
                self.state = 109
                self.match(XPath31GrammarParser.CP)
                self.state = 111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 110
                    self.filter_()


                pass
            elif token in [22]:
                localctx = XPath31GrammarParser.ExprWrapForceListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(XPath31GrammarParser.OB)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -4584664416748823550) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 4095) != 0):
                    self.state = 114
                    self.expr(0)


                self.state = 117
                self.match(XPath31GrammarParser.CB)
                self.state = 119
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 118
                    self.filter_()


                pass
            elif token in [1, 31, 65, 66, 67, 68, 69]:
                localctx = XPath31GrammarParser.ExprMatcherContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.matcher()
                pass
            elif token in [12]:
                localctx = XPath31GrammarParser.ExprVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.varRef()
                pass
            elif token in [62, 63, 70, 71, 72, 73, 74, 75]:
                localctx = XPath31GrammarParser.ExprLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.literal()
                pass
            elif token in [10, 11, 29, 30]:
                localctx = XPath31GrammarParser.ExprPathContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.path()
                self.state = 126
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 125
                    self.filter_()


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = XPath31GrammarParser.ExprFunctionCallContext(self, XPath31GrammarParser.AtomicOrEncapsulateContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_atomicOrEncapsulate)
                    self.state = 130
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 131
                    self.argumentList()
                    self.state = 133
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        self.state = 132
                        self.coerceFallback()

             
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(XPath31GrammarParser.OP, 0)

        def CP(self):
            return self.getToken(XPath31GrammarParser.CP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(XPath31GrammarParser.COMMA)
            else:
                return self.getToken(XPath31GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = XPath31GrammarParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(XPath31GrammarParser.OP)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -4584664416748823550) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 4095) != 0):
                self.state = 141
                self.expr(0)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 142
                    self.match(XPath31GrammarParser.COMMA)
                    self.state = 143
                    self.expr(0)
                    self.state = 148
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 151
            self.match(XPath31GrammarParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(XPath31GrammarParser.OB, 0)

        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


        def CB(self):
            return self.getToken(XPath31GrammarParser.CB, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilter" ):
                listener.enterFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilter" ):
                listener.exitFilter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilter" ):
                return visitor.visitFilter(self)
            else:
                return visitor.visitChildren(self)




    def filter_(self):

        localctx = XPath31GrammarParser.FilterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(XPath31GrammarParser.OB)
            self.state = 154
            self.expr(0)
            self.state = 155
            self.match(XPath31GrammarParser.CB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(XPath31GrammarParser.EQ, 0)

        def NE(self):
            return self.getToken(XPath31GrammarParser.NE, 0)

        def LT(self):
            return self.getToken(XPath31GrammarParser.LT, 0)

        def LE(self):
            return self.getToken(XPath31GrammarParser.LE, 0)

        def GT(self):
            return self.getToken(XPath31GrammarParser.GT, 0)

        def GE(self):
            return self.getToken(XPath31GrammarParser.GE, 0)

        def LL(self):
            return self.getToken(XPath31GrammarParser.LL, 0)

        def GG(self):
            return self.getToken(XPath31GrammarParser.GG, 0)

        def KW_ZIP(self):
            return self.getToken(XPath31GrammarParser.KW_ZIP, 0)

        def KW_PRODUCT(self):
            return self.getToken(XPath31GrammarParser.KW_PRODUCT, 0)

        def KW_ANY(self):
            return self.getToken(XPath31GrammarParser.KW_ANY, 0)

        def KW_ALL(self):
            return self.getToken(XPath31GrammarParser.KW_ALL, 0)

        def KW_SEQUENCE(self):
            return self.getToken(XPath31GrammarParser.KW_SEQUENCE, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_relOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelOp" ):
                listener.enterRelOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelOp" ):
                listener.exitRelOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelOp" ):
                return visitor.visitRelOp(self)
            else:
                return visitor.visitChildren(self)




    def relOp(self):

        localctx = XPath31GrammarParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relOp)
        self._la = 0 # Token type
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55 or _la==56:
                    self.state = 157
                    _la = self._input.LA(1)
                    if not(_la==55 or _la==56):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 171136785840078848) != 0):
                    self.state = 160
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 171136785840078848) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 163
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3137536) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 171136785840078848) != 0):
                    self.state = 164
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 171136785840078848) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55 or _la==56:
                    self.state = 167
                    _la = self._input.LA(1)
                    if not(_la==55 or _la==56):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 170
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3137536) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(XPath31GrammarParser.STAR, 0)

        def KW_DIV(self):
            return self.getToken(XPath31GrammarParser.KW_DIV, 0)

        def KW_IDIV(self):
            return self.getToken(XPath31GrammarParser.KW_IDIV, 0)

        def KW_MOD(self):
            return self.getToken(XPath31GrammarParser.KW_MOD, 0)

        def KW_ZIP(self):
            return self.getToken(XPath31GrammarParser.KW_ZIP, 0)

        def KW_PRODUCT(self):
            return self.getToken(XPath31GrammarParser.KW_PRODUCT, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_mulOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulOp" ):
                listener.enterMulOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulOp" ):
                listener.exitMulOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOp" ):
                return visitor.visitMulOp(self)
            else:
                return visitor.visitChildren(self)




    def mulOp(self):

        localctx = XPath31GrammarParser.MulOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55 or _la==56:
                self.state = 173
                _la = self._input.LA(1)
                if not(_la==55 or _la==56):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 39859443990528) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(XPath31GrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(XPath31GrammarParser.MINUS, 0)

        def PP(self):
            return self.getToken(XPath31GrammarParser.PP, 0)

        def KW_ZIP(self):
            return self.getToken(XPath31GrammarParser.KW_ZIP, 0)

        def KW_PRODUCT(self):
            return self.getToken(XPath31GrammarParser.KW_PRODUCT, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_addOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = XPath31GrammarParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55 or _la==56:
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==55 or _la==56):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 181
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 202375168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_AND(self):
            return self.getToken(XPath31GrammarParser.KW_AND, 0)

        def KW_ZIP(self):
            return self.getToken(XPath31GrammarParser.KW_ZIP, 0)

        def KW_PRODUCT(self):
            return self.getToken(XPath31GrammarParser.KW_PRODUCT, 0)

        def KW_ANY(self):
            return self.getToken(XPath31GrammarParser.KW_ANY, 0)

        def KW_ALL(self):
            return self.getToken(XPath31GrammarParser.KW_ALL, 0)

        def KW_SEQUENCE(self):
            return self.getToken(XPath31GrammarParser.KW_SEQUENCE, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_andOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndOp" ):
                listener.enterAndOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndOp" ):
                listener.exitAndOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndOp" ):
                return visitor.visitAndOp(self)
            else:
                return visitor.visitChildren(self)




    def andOp(self):

        localctx = XPath31GrammarParser.AndOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_andOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55 or _la==56:
                self.state = 183
                _la = self._input.LA(1)
                if not(_la==55 or _la==56):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 171136785840078848) != 0):
                self.state = 186
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 171136785840078848) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 189
            self.match(XPath31GrammarParser.KW_AND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_OR(self):
            return self.getToken(XPath31GrammarParser.KW_OR, 0)

        def KW_ZIP(self):
            return self.getToken(XPath31GrammarParser.KW_ZIP, 0)

        def KW_PRODUCT(self):
            return self.getToken(XPath31GrammarParser.KW_PRODUCT, 0)

        def KW_ANY(self):
            return self.getToken(XPath31GrammarParser.KW_ANY, 0)

        def KW_ALL(self):
            return self.getToken(XPath31GrammarParser.KW_ALL, 0)

        def KW_SEQUENCE(self):
            return self.getToken(XPath31GrammarParser.KW_SEQUENCE, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_orOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrOp" ):
                listener.enterOrOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrOp" ):
                listener.exitOrOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrOp" ):
                return visitor.visitOrOp(self)
            else:
                return visitor.visitChildren(self)




    def orOp(self):

        localctx = XPath31GrammarParser.OrOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_orOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55 or _la==56:
                self.state = 191
                _la = self._input.LA(1)
                if not(_la==55 or _la==56):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 171136785840078848) != 0):
                self.state = 194
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 171136785840078848) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 197
            self.match(XPath31GrammarParser.KW_OR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_path

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PathFromRootContext(PathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.PathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SLASH(self):
            return self.getToken(XPath31GrammarParser.SLASH, 0)
        def relPath(self):
            return self.getTypedRuleContext(XPath31GrammarParser.RelPathContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathFromRoot" ):
                listener.enterPathFromRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathFromRoot" ):
                listener.exitPathFromRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathFromRoot" ):
                return visitor.visitPathFromRoot(self)
            else:
                return visitor.visitChildren(self)


    class PathRootExactContext(PathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.PathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SLASH(self):
            return self.getToken(XPath31GrammarParser.SLASH, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathRootExact" ):
                listener.enterPathRootExact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathRootExact" ):
                listener.exitPathRootExact(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathRootExact" ):
                return visitor.visitPathRootExact(self)
            else:
                return visitor.visitChildren(self)


    class PathFromRelativeContext(PathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.PathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def D(self):
            return self.getToken(XPath31GrammarParser.D, 0)
        def SLASH(self):
            return self.getToken(XPath31GrammarParser.SLASH, 0)
        def relPath(self):
            return self.getTypedRuleContext(XPath31GrammarParser.RelPathContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathFromRelative" ):
                listener.enterPathFromRelative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathFromRelative" ):
                listener.exitPathFromRelative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathFromRelative" ):
                return visitor.visitPathFromRelative(self)
            else:
                return visitor.visitChildren(self)


    class PathSelfContext(PathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.PathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def D(self):
            return self.getToken(XPath31GrammarParser.D, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathSelf" ):
                listener.enterPathSelf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathSelf" ):
                listener.exitPathSelf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathSelf" ):
                return visitor.visitPathSelf(self)
            else:
                return visitor.visitChildren(self)


    class PathFromAnyContext(PathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.PathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SS(self):
            return self.getToken(XPath31GrammarParser.SS, 0)
        def relPath(self):
            return self.getTypedRuleContext(XPath31GrammarParser.RelPathContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathFromAny" ):
                listener.enterPathFromAny(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathFromAny" ):
                listener.exitPathFromAny(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathFromAny" ):
                return visitor.visitPathFromAny(self)
            else:
                return visitor.visitChildren(self)


    class PathParentContext(PathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.PathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DD(self):
            return self.getToken(XPath31GrammarParser.DD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathParent" ):
                listener.enterPathParent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathParent" ):
                listener.exitPathParent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathParent" ):
                return visitor.visitPathParent(self)
            else:
                return visitor.visitChildren(self)



    def path(self):

        localctx = XPath31GrammarParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_path)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                localctx = XPath31GrammarParser.PathFromRootContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(XPath31GrammarParser.SLASH)
                self.state = 200
                self.relPath(0)
                pass

            elif la_ == 2:
                localctx = XPath31GrammarParser.PathRootExactContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(XPath31GrammarParser.SLASH)
                pass

            elif la_ == 3:
                localctx = XPath31GrammarParser.PathFromAnyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.match(XPath31GrammarParser.SS)
                self.state = 203
                self.relPath(0)
                pass

            elif la_ == 4:
                localctx = XPath31GrammarParser.PathFromRelativeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(XPath31GrammarParser.D)
                self.state = 205
                self.match(XPath31GrammarParser.SLASH)
                self.state = 206
                self.relPath(0)
                pass

            elif la_ == 5:
                localctx = XPath31GrammarParser.PathSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 207
                self.match(XPath31GrammarParser.D)
                pass

            elif la_ == 6:
                localctx = XPath31GrammarParser.PathParentContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 208
                self.match(XPath31GrammarParser.DD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_relPath

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RelPathStepContext(RelPathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.RelPathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reverseStep(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ReverseStepContext,0)

        def forwardStep(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ForwardStepContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelPathStep" ):
                listener.enterRelPathStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelPathStep" ):
                listener.exitRelPathStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelPathStep" ):
                return visitor.visitRelPathStep(self)
            else:
                return visitor.visitChildren(self)


    class RelPathChainContext(RelPathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.RelPathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def relPath(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.RelPathContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.RelPathContext,i)

        def SLASH(self):
            return self.getToken(XPath31GrammarParser.SLASH, 0)
        def SS(self):
            return self.getToken(XPath31GrammarParser.SS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelPathChain" ):
                listener.enterRelPathChain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelPathChain" ):
                listener.exitRelPathChain(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelPathChain" ):
                return visitor.visitRelPathChain(self)
            else:
                return visitor.visitChildren(self)



    def relPath(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XPath31GrammarParser.RelPathContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_relPath, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = XPath31GrammarParser.RelPathStepContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 212
                self.reverseStep()
                pass

            elif la_ == 2:
                self.state = 213
                self.forwardStep()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 221
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = XPath31GrammarParser.RelPathChainContext(self, XPath31GrammarParser.RelPathContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relPath)
                    self.state = 216
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 217
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 218
                    self.relPath(3) 
                self.state = 223
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ForwardStepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_forwardStep

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForwardStepSelfContext(ForwardStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_SELF(self):
            return self.getToken(XPath31GrammarParser.KW_SELF, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardStepSelf" ):
                listener.enterForwardStepSelf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardStepSelf" ):
                listener.exitForwardStepSelf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardStepSelf" ):
                return visitor.visitForwardStepSelf(self)
            else:
                return visitor.visitChildren(self)


    class ForwardStepFollowingSiblingContext(ForwardStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FOLLOWING_SIBLING(self):
            return self.getToken(XPath31GrammarParser.KW_FOLLOWING_SIBLING, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardStepFollowingSibling" ):
                listener.enterForwardStepFollowingSibling(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardStepFollowingSibling" ):
                listener.exitForwardStepFollowingSibling(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardStepFollowingSibling" ):
                return visitor.visitForwardStepFollowingSibling(self)
            else:
                return visitor.visitChildren(self)


    class ForwardStepDescendantOrSelfContext(ForwardStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_DESCENDANT_OR_SELF(self):
            return self.getToken(XPath31GrammarParser.KW_DESCENDANT_OR_SELF, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardStepDescendantOrSelf" ):
                listener.enterForwardStepDescendantOrSelf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardStepDescendantOrSelf" ):
                listener.exitForwardStepDescendantOrSelf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardStepDescendantOrSelf" ):
                return visitor.visitForwardStepDescendantOrSelf(self)
            else:
                return visitor.visitChildren(self)


    class ForwardStepDescendantContext(ForwardStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_DESCENDANT(self):
            return self.getToken(XPath31GrammarParser.KW_DESCENDANT, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardStepDescendant" ):
                listener.enterForwardStepDescendant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardStepDescendant" ):
                listener.exitForwardStepDescendant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardStepDescendant" ):
                return visitor.visitForwardStepDescendant(self)
            else:
                return visitor.visitChildren(self)


    class ForwardStepFollowingContext(ForwardStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FOLLOWING(self):
            return self.getToken(XPath31GrammarParser.KW_FOLLOWING, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardStepFollowing" ):
                listener.enterForwardStepFollowing(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardStepFollowing" ):
                listener.exitForwardStepFollowing(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardStepFollowing" ):
                return visitor.visitForwardStepFollowing(self)
            else:
                return visitor.visitChildren(self)


    class ForwardStepDirectSelfContext(ForwardStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def D(self):
            return self.getToken(XPath31GrammarParser.D, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardStepDirectSelf" ):
                listener.enterForwardStepDirectSelf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardStepDirectSelf" ):
                listener.exitForwardStepDirectSelf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardStepDirectSelf" ):
                return visitor.visitForwardStepDirectSelf(self)
            else:
                return visitor.visitChildren(self)


    class ForwardStepChildContext(ForwardStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_CHILD(self):
            return self.getToken(XPath31GrammarParser.KW_CHILD, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardStepChild" ):
                listener.enterForwardStepChild(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardStepChild" ):
                listener.exitForwardStepChild(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardStepChild" ):
                return visitor.visitForwardStepChild(self)
            else:
                return visitor.visitChildren(self)


    class ForwardStepValueContext(ForwardStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardStepValue" ):
                listener.enterForwardStepValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardStepValue" ):
                listener.exitForwardStepValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForwardStepValue" ):
                return visitor.visitForwardStepValue(self)
            else:
                return visitor.visitChildren(self)



    def forwardStep(self):

        localctx = XPath31GrammarParser.ForwardStepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forwardStep)
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                localctx = XPath31GrammarParser.ForwardStepChildContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(XPath31GrammarParser.KW_CHILD)
                self.state = 225
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 226
                self.atomicOrEncapsulate(0)
                pass

            elif la_ == 2:
                localctx = XPath31GrammarParser.ForwardStepDescendantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(XPath31GrammarParser.KW_DESCENDANT)
                self.state = 228
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 229
                self.atomicOrEncapsulate(0)
                pass

            elif la_ == 3:
                localctx = XPath31GrammarParser.ForwardStepSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(XPath31GrammarParser.KW_SELF)
                self.state = 231
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 232
                self.atomicOrEncapsulate(0)
                pass

            elif la_ == 4:
                localctx = XPath31GrammarParser.ForwardStepDescendantOrSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.match(XPath31GrammarParser.KW_DESCENDANT_OR_SELF)
                self.state = 234
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 235
                self.atomicOrEncapsulate(0)
                pass

            elif la_ == 5:
                localctx = XPath31GrammarParser.ForwardStepFollowingSiblingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.match(XPath31GrammarParser.KW_FOLLOWING_SIBLING)
                self.state = 237
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 238
                self.atomicOrEncapsulate(0)
                pass

            elif la_ == 6:
                localctx = XPath31GrammarParser.ForwardStepFollowingContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 239
                self.match(XPath31GrammarParser.KW_FOLLOWING)
                self.state = 240
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 241
                self.atomicOrEncapsulate(0)
                pass

            elif la_ == 7:
                localctx = XPath31GrammarParser.ForwardStepDirectSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 242
                self.match(XPath31GrammarParser.D)
                pass

            elif la_ == 8:
                localctx = XPath31GrammarParser.ForwardStepValueContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 243
                self.atomicOrEncapsulate(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReverseStepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_reverseStep

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReverseStepDirectParentContext(ReverseStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReverseStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DD(self):
            return self.getToken(XPath31GrammarParser.DD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverseStepDirectParent" ):
                listener.enterReverseStepDirectParent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverseStepDirectParent" ):
                listener.exitReverseStepDirectParent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReverseStepDirectParent" ):
                return visitor.visitReverseStepDirectParent(self)
            else:
                return visitor.visitChildren(self)


    class ReverseStepParentContext(ReverseStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReverseStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_PARENT(self):
            return self.getToken(XPath31GrammarParser.KW_PARENT, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverseStepParent" ):
                listener.enterReverseStepParent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverseStepParent" ):
                listener.exitReverseStepParent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReverseStepParent" ):
                return visitor.visitReverseStepParent(self)
            else:
                return visitor.visitChildren(self)


    class ReverseStepAncestorContext(ReverseStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReverseStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_ANCESTOR(self):
            return self.getToken(XPath31GrammarParser.KW_ANCESTOR, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverseStepAncestor" ):
                listener.enterReverseStepAncestor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverseStepAncestor" ):
                listener.exitReverseStepAncestor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReverseStepAncestor" ):
                return visitor.visitReverseStepAncestor(self)
            else:
                return visitor.visitChildren(self)


    class ReverseStepPrecedingSiblingContext(ReverseStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReverseStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_PRECEDING_SIBLING(self):
            return self.getToken(XPath31GrammarParser.KW_PRECEDING_SIBLING, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverseStepPrecedingSibling" ):
                listener.enterReverseStepPrecedingSibling(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverseStepPrecedingSibling" ):
                listener.exitReverseStepPrecedingSibling(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReverseStepPrecedingSibling" ):
                return visitor.visitReverseStepPrecedingSibling(self)
            else:
                return visitor.visitChildren(self)


    class ReverseStepAncestorOrSelfContext(ReverseStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReverseStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_ANCESTOR_OR_SELF(self):
            return self.getToken(XPath31GrammarParser.KW_ANCESTOR_OR_SELF, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverseStepAncestorOrSelf" ):
                listener.enterReverseStepAncestorOrSelf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverseStepAncestorOrSelf" ):
                listener.exitReverseStepAncestorOrSelf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReverseStepAncestorOrSelf" ):
                return visitor.visitReverseStepAncestorOrSelf(self)
            else:
                return visitor.visitChildren(self)


    class ReverseStepPrecedingContext(ReverseStepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReverseStepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_PRECEDING(self):
            return self.getToken(XPath31GrammarParser.KW_PRECEDING, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def atomicOrEncapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicOrEncapsulateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverseStepPreceding" ):
                listener.enterReverseStepPreceding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverseStepPreceding" ):
                listener.exitReverseStepPreceding(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReverseStepPreceding" ):
                return visitor.visitReverseStepPreceding(self)
            else:
                return visitor.visitChildren(self)



    def reverseStep(self):

        localctx = XPath31GrammarParser.ReverseStepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_reverseStep)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                localctx = XPath31GrammarParser.ReverseStepParentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(XPath31GrammarParser.KW_PARENT)
                self.state = 247
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 248
                self.atomicOrEncapsulate(0)
                pass
            elif token in [32]:
                localctx = XPath31GrammarParser.ReverseStepAncestorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(XPath31GrammarParser.KW_ANCESTOR)
                self.state = 250
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 251
                self.atomicOrEncapsulate(0)
                pass
            elif token in [49]:
                localctx = XPath31GrammarParser.ReverseStepPrecedingSiblingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(XPath31GrammarParser.KW_PRECEDING_SIBLING)
                self.state = 253
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 254
                self.atomicOrEncapsulate(0)
                pass
            elif token in [48]:
                localctx = XPath31GrammarParser.ReverseStepPrecedingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 255
                self.match(XPath31GrammarParser.KW_PRECEDING)
                self.state = 256
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 257
                self.atomicOrEncapsulate(0)
                pass
            elif token in [33]:
                localctx = XPath31GrammarParser.ReverseStepAncestorOrSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 258
                self.match(XPath31GrammarParser.KW_ANCESTOR_OR_SELF)
                self.state = 259
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 260
                self.atomicOrEncapsulate(0)
                pass
            elif token in [11]:
                localctx = XPath31GrammarParser.ReverseStepDirectParentContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.match(XPath31GrammarParser.DD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(XPath31GrammarParser.IntegerLiteral, 0)

        def DecimalLiteral(self):
            return self.getToken(XPath31GrammarParser.DecimalLiteral, 0)

        def DoubleLiteral(self):
            return self.getToken(XPath31GrammarParser.DoubleLiteral, 0)

        def StringLiteral(self):
            return self.getToken(XPath31GrammarParser.StringLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(XPath31GrammarParser.BooleanLiteral, 0)

        def KW_NAN(self):
            return self.getToken(XPath31GrammarParser.KW_NAN, 0)

        def KW_INF(self):
            return self.getToken(XPath31GrammarParser.KW_INF, 0)

        def Name(self):
            return self.getToken(XPath31GrammarParser.Name, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = XPath31GrammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            _la = self._input.LA(1)
            if not(((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & 16131) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_matcher

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MatcherCaseInsensitiveContext(MatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.MatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IgnoreCaseMatcher(self):
            return self.getToken(XPath31GrammarParser.IgnoreCaseMatcher, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcherCaseInsensitive" ):
                listener.enterMatcherCaseInsensitive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcherCaseInsensitive" ):
                listener.exitMatcherCaseInsensitive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatcherCaseInsensitive" ):
                return visitor.visitMatcherCaseInsensitive(self)
            else:
                return visitor.visitChildren(self)


    class MatcherGlobContext(MatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.MatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def GlobMatcher(self):
            return self.getToken(XPath31GrammarParser.GlobMatcher, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcherGlob" ):
                listener.enterMatcherGlob(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcherGlob" ):
                listener.exitMatcherGlob(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatcherGlob" ):
                return visitor.visitMatcherGlob(self)
            else:
                return visitor.visitChildren(self)


    class MatcherFuzzyContext(MatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.MatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FuzzyMatcher(self):
            return self.getToken(XPath31GrammarParser.FuzzyMatcher, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcherFuzzy" ):
                listener.enterMatcherFuzzy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcherFuzzy" ):
                listener.exitMatcherFuzzy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatcherFuzzy" ):
                return visitor.visitMatcherFuzzy(self)
            else:
                return visitor.visitChildren(self)


    class MatcherNumericRangeContext(MatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.MatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def numericRangeMatcher(self):
            return self.getTypedRuleContext(XPath31GrammarParser.NumericRangeMatcherContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcherNumericRange" ):
                listener.enterMatcherNumericRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcherNumericRange" ):
                listener.exitMatcherNumericRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatcherNumericRange" ):
                return visitor.visitMatcherNumericRange(self)
            else:
                return visitor.visitChildren(self)


    class MatcherWildcardContext(MatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.MatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STAR(self):
            return self.getToken(XPath31GrammarParser.STAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcherWildcard" ):
                listener.enterMatcherWildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcherWildcard" ):
                listener.exitMatcherWildcard(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatcherWildcard" ):
                return visitor.visitMatcherWildcard(self)
            else:
                return visitor.visitChildren(self)


    class MatcherRegexContext(MatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.MatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RegexMatcher(self):
            return self.getToken(XPath31GrammarParser.RegexMatcher, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcherRegex" ):
                listener.enterMatcherRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcherRegex" ):
                listener.exitMatcherRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatcherRegex" ):
                return visitor.visitMatcherRegex(self)
            else:
                return visitor.visitChildren(self)


    class MatcherStrictContext(MatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.MatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def StrictMatcher(self):
            return self.getToken(XPath31GrammarParser.StrictMatcher, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatcherStrict" ):
                listener.enterMatcherStrict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatcherStrict" ):
                listener.exitMatcherStrict(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatcherStrict" ):
                return visitor.visitMatcherStrict(self)
            else:
                return visitor.visitChildren(self)



    def matcher(self):

        localctx = XPath31GrammarParser.MatcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_matcher)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [67]:
                localctx = XPath31GrammarParser.MatcherStrictContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(XPath31GrammarParser.StrictMatcher)
                pass
            elif token in [65]:
                localctx = XPath31GrammarParser.MatcherRegexContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.match(XPath31GrammarParser.RegexMatcher)
                pass
            elif token in [66]:
                localctx = XPath31GrammarParser.MatcherGlobContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 268
                self.match(XPath31GrammarParser.GlobMatcher)
                pass
            elif token in [68]:
                localctx = XPath31GrammarParser.MatcherFuzzyContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 269
                self.match(XPath31GrammarParser.FuzzyMatcher)
                pass
            elif token in [69]:
                localctx = XPath31GrammarParser.MatcherCaseInsensitiveContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 270
                self.match(XPath31GrammarParser.IgnoreCaseMatcher)
                pass
            elif token in [1]:
                localctx = XPath31GrammarParser.MatcherNumericRangeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 271
                self.numericRangeMatcher()
                pass
            elif token in [31]:
                localctx = XPath31GrammarParser.MatcherWildcardContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 272
                self.match(XPath31GrammarParser.STAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericRangeMatcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_numericRangeMatcher

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumericRangeMatcherInclusiveContext(NumericRangeMatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.NumericRangeMatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TILDE(self):
            return self.getToken(XPath31GrammarParser.TILDE, 0)
        def numericRangeMatcherLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.NumericRangeMatcherLiteralContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.NumericRangeMatcherLiteralContext,i)

        def COLON(self):
            return self.getToken(XPath31GrammarParser.COLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericRangeMatcherInclusive" ):
                listener.enterNumericRangeMatcherInclusive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericRangeMatcherInclusive" ):
                listener.exitNumericRangeMatcherInclusive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericRangeMatcherInclusive" ):
                return visitor.visitNumericRangeMatcherInclusive(self)
            else:
                return visitor.visitChildren(self)


    class NumericRangeMatcherToleranceContext(NumericRangeMatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.NumericRangeMatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TILDE(self):
            return self.getToken(XPath31GrammarParser.TILDE, 0)
        def numericRangeMatcherLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.NumericRangeMatcherLiteralContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.NumericRangeMatcherLiteralContext,i)

        def AT(self):
            return self.getToken(XPath31GrammarParser.AT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericRangeMatcherTolerance" ):
                listener.enterNumericRangeMatcherTolerance(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericRangeMatcherTolerance" ):
                listener.exitNumericRangeMatcherTolerance(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericRangeMatcherTolerance" ):
                return visitor.visitNumericRangeMatcherTolerance(self)
            else:
                return visitor.visitChildren(self)


    class NumericRangeMatcherBoundedContext(NumericRangeMatcherContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.NumericRangeMatcherContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TILDE(self):
            return self.getToken(XPath31GrammarParser.TILDE, 0)
        def numericRangeMatcherLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.NumericRangeMatcherLiteralContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.NumericRangeMatcherLiteralContext,i)

        def COLON(self):
            return self.getToken(XPath31GrammarParser.COLON, 0)
        def OP(self):
            return self.getToken(XPath31GrammarParser.OP, 0)
        def OB(self):
            return self.getToken(XPath31GrammarParser.OB, 0)
        def CP(self):
            return self.getToken(XPath31GrammarParser.CP, 0)
        def CB(self):
            return self.getToken(XPath31GrammarParser.CB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericRangeMatcherBounded" ):
                listener.enterNumericRangeMatcherBounded(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericRangeMatcherBounded" ):
                listener.exitNumericRangeMatcherBounded(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericRangeMatcherBounded" ):
                return visitor.visitNumericRangeMatcherBounded(self)
            else:
                return visitor.visitChildren(self)



    def numericRangeMatcher(self):

        localctx = XPath31GrammarParser.NumericRangeMatcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_numericRangeMatcher)
        self._la = 0 # Token type
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                localctx = XPath31GrammarParser.NumericRangeMatcherInclusiveContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(XPath31GrammarParser.TILDE)
                self.state = 276
                self.numericRangeMatcherLiteral()
                self.state = 277
                self.match(XPath31GrammarParser.COLON)
                self.state = 278
                self.numericRangeMatcherLiteral()
                pass

            elif la_ == 2:
                localctx = XPath31GrammarParser.NumericRangeMatcherBoundedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(XPath31GrammarParser.TILDE)
                self.state = 281
                _la = self._input.LA(1)
                if not(_la==22 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 282
                self.numericRangeMatcherLiteral()
                self.state = 283
                self.match(XPath31GrammarParser.COLON)
                self.state = 284
                self.numericRangeMatcherLiteral()
                self.state = 285
                _la = self._input.LA(1)
                if not(_la==4 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = XPath31GrammarParser.NumericRangeMatcherToleranceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(XPath31GrammarParser.TILDE)
                self.state = 288
                self.numericRangeMatcherLiteral()
                self.state = 291
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 289
                    self.match(XPath31GrammarParser.AT)
                    self.state = 290
                    self.numericRangeMatcherLiteral()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericRangeMatcherLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(XPath31GrammarParser.IntegerLiteral, 0)

        def DecimalLiteral(self):
            return self.getToken(XPath31GrammarParser.DecimalLiteral, 0)

        def DoubleLiteral(self):
            return self.getToken(XPath31GrammarParser.DoubleLiteral, 0)

        def KW_INF(self):
            return self.getToken(XPath31GrammarParser.KW_INF, 0)

        def MINUS(self):
            return self.getToken(XPath31GrammarParser.MINUS, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_numericRangeMatcherLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericRangeMatcherLiteral" ):
                listener.enterNumericRangeMatcherLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericRangeMatcherLiteral" ):
                listener.exitNumericRangeMatcherLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericRangeMatcherLiteral" ):
                return visitor.visitNumericRangeMatcherLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericRangeMatcherLiteral(self):

        localctx = XPath31GrammarParser.NumericRangeMatcherLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_numericRangeMatcherLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 295
                self.match(XPath31GrammarParser.MINUS)


            self.state = 298
            _la = self._input.LA(1)
            if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & 897) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoerceFallbackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ON(self):
            return self.getToken(XPath31GrammarParser.KW_ON, 0)

        def KW_ERROR(self):
            return self.getToken(XPath31GrammarParser.KW_ERROR, 0)

        def KW_DISCARD(self):
            return self.getToken(XPath31GrammarParser.KW_DISCARD, 0)

        def KW_FAIL(self):
            return self.getToken(XPath31GrammarParser.KW_FAIL, 0)

        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_coerceFallback

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoerceFallback" ):
                listener.enterCoerceFallback(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoerceFallback" ):
                listener.exitCoerceFallback(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoerceFallback" ):
                return visitor.visitCoerceFallback(self)
            else:
                return visitor.visitChildren(self)




    def coerceFallback(self):

        localctx = XPath31GrammarParser.CoerceFallbackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_coerceFallback)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(XPath31GrammarParser.KW_ON)
            self.state = 301
            self.match(XPath31GrammarParser.KW_ERROR)
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [60]:
                self.state = 302
                self.match(XPath31GrammarParser.KW_DISCARD)
                pass
            elif token in [61]:
                self.state = 303
                self.match(XPath31GrammarParser.KW_FAIL)
                pass
            elif token in [1, 10, 11, 12, 20, 22, 24, 27, 29, 30, 31, 53, 54, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]:
                self.state = 304
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(XPath31GrammarParser.DOLLAR, 0)

        def Name(self):
            return self.getToken(XPath31GrammarParser.Name, 0)

        def IntegerLiteral(self):
            return self.getToken(XPath31GrammarParser.IntegerLiteral, 0)

        def StringLiteral(self):
            return self.getToken(XPath31GrammarParser.StringLiteral, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_varRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarRef" ):
                listener.enterVarRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarRef" ):
                listener.exitVarRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarRef" ):
                return visitor.visitVarRef(self)
            else:
                return visitor.visitChildren(self)




    def varRef(self):

        localctx = XPath31GrammarParser.VarRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_varRef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(XPath31GrammarParser.DOLLAR)
            self.state = 308
            _la = self._input.LA(1)
            if not(((((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 41) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.atomicOrEncapsulate_sempred
        self._predicates[11] = self.relPath_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def atomicOrEncapsulate_sempred(self, localctx:AtomicOrEncapsulateContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

    def relPath_sempred(self, localctx:RelPathContext, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




