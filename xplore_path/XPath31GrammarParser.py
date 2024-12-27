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
        4,1,71,310,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,46,8,1,1,1,3,1,49,8,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,1,1,1,1,1,1,
        1,3,1,73,8,1,1,1,1,1,1,1,1,1,3,1,79,8,1,1,1,1,1,1,1,1,1,3,1,85,8,
        1,1,1,1,1,1,1,1,1,3,1,91,8,1,5,1,93,8,1,10,1,12,1,96,9,1,1,2,1,2,
        1,2,3,2,101,8,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,109,8,2,1,2,1,2,1,2,
        1,2,1,2,3,2,116,8,2,1,3,3,3,119,8,3,1,3,3,3,122,8,3,1,3,1,3,3,3,
        126,8,3,1,3,3,3,129,8,3,1,3,1,3,1,3,3,3,134,8,3,1,3,3,3,137,8,3,
        1,3,1,3,3,3,141,8,3,1,3,3,3,144,8,3,3,3,146,8,3,1,4,3,4,149,8,4,
        1,4,1,4,1,4,3,4,154,8,4,3,4,156,8,4,1,5,3,5,159,8,5,1,5,1,5,1,5,
        3,5,164,8,5,3,5,166,8,5,1,6,3,6,169,8,6,1,6,3,6,172,8,6,1,6,1,6,
        1,6,3,6,177,8,6,1,6,3,6,180,8,6,3,6,182,8,6,1,7,3,7,185,8,7,1,7,
        3,7,188,8,7,1,7,1,7,1,7,3,7,193,8,7,1,7,3,7,196,8,7,3,7,198,8,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,210,8,8,1,9,1,9,1,9,
        3,9,215,8,9,1,9,1,9,5,9,219,8,9,10,9,12,9,222,9,9,1,9,1,9,1,9,5,
        9,227,8,9,10,9,12,9,230,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,
        10,252,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,3,11,270,8,11,1,12,1,12,1,12,1,12,5,
        12,276,8,12,10,12,12,12,279,9,12,3,12,281,8,12,1,12,1,12,1,13,1,
        13,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,298,
        8,16,1,17,1,17,1,17,1,17,1,17,3,17,305,8,17,1,18,1,18,1,18,1,18,
        0,2,2,18,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        0,10,1,0,50,51,2,0,36,36,41,41,2,0,23,23,49,49,2,0,18,18,24,24,1,
        0,52,53,2,0,50,51,54,54,2,0,11,17,19,19,4,0,28,28,35,35,39,39,42,
        42,1,0,26,27,2,0,59,60,65,70,370,0,38,1,0,0,0,2,48,1,0,0,0,4,115,
        1,0,0,0,6,145,1,0,0,0,8,155,1,0,0,0,10,165,1,0,0,0,12,181,1,0,0,
        0,14,197,1,0,0,0,16,209,1,0,0,0,18,211,1,0,0,0,20,251,1,0,0,0,22,
        269,1,0,0,0,24,271,1,0,0,0,26,284,1,0,0,0,28,286,1,0,0,0,30,290,
        1,0,0,0,32,297,1,0,0,0,34,299,1,0,0,0,36,306,1,0,0,0,38,39,3,2,1,
        0,39,40,5,0,0,1,40,1,1,0,0,0,41,42,6,1,-1,0,42,43,7,0,0,0,43,45,
        3,2,1,0,44,46,3,34,17,0,45,44,1,0,0,0,45,46,1,0,0,0,46,49,1,0,0,
        0,47,49,3,4,2,0,48,41,1,0,0,0,48,47,1,0,0,0,49,94,1,0,0,0,50,51,
        10,10,0,0,51,52,5,6,0,0,52,93,3,2,1,11,53,54,10,9,0,0,54,55,7,1,
        0,0,55,93,3,2,1,10,56,57,10,8,0,0,57,58,7,2,0,0,58,93,3,2,1,9,59,
        60,10,7,0,0,60,61,5,48,0,0,61,93,3,2,1,8,62,63,10,6,0,0,63,64,3,
        14,7,0,64,66,3,2,1,0,65,67,3,34,17,0,66,65,1,0,0,0,66,67,1,0,0,0,
        67,93,1,0,0,0,68,69,10,5,0,0,69,70,3,12,6,0,70,72,3,2,1,0,71,73,
        3,34,17,0,72,71,1,0,0,0,72,73,1,0,0,0,73,93,1,0,0,0,74,75,10,4,0,
        0,75,76,3,6,3,0,76,78,3,2,1,0,77,79,3,34,17,0,78,77,1,0,0,0,78,79,
        1,0,0,0,79,93,1,0,0,0,80,81,10,3,0,0,81,82,3,10,5,0,82,84,3,2,1,
        0,83,85,3,34,17,0,84,83,1,0,0,0,84,85,1,0,0,0,85,93,1,0,0,0,86,87,
        10,2,0,0,87,88,3,8,4,0,88,90,3,2,1,0,89,91,3,34,17,0,90,89,1,0,0,
        0,90,91,1,0,0,0,91,93,1,0,0,0,92,50,1,0,0,0,92,53,1,0,0,0,92,56,
        1,0,0,0,92,59,1,0,0,0,92,62,1,0,0,0,92,68,1,0,0,0,92,74,1,0,0,0,
        92,80,1,0,0,0,92,86,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,
        0,0,0,95,3,1,0,0,0,96,94,1,0,0,0,97,98,7,3,0,0,98,100,3,4,2,0,99,
        101,3,34,17,0,100,99,1,0,0,0,100,101,1,0,0,0,101,116,1,0,0,0,102,
        103,5,22,0,0,103,104,3,2,1,0,104,105,5,7,0,0,105,116,1,0,0,0,106,
        108,5,20,0,0,107,109,3,2,1,0,108,107,1,0,0,0,108,109,1,0,0,0,109,
        110,1,0,0,0,110,116,5,2,0,0,111,116,3,32,16,0,112,116,3,36,18,0,
        113,116,3,30,15,0,114,116,3,16,8,0,115,97,1,0,0,0,115,102,1,0,0,
        0,115,106,1,0,0,0,115,111,1,0,0,0,115,112,1,0,0,0,115,113,1,0,0,
        0,115,114,1,0,0,0,116,5,1,0,0,0,117,119,7,4,0,0,118,117,1,0,0,0,
        118,119,1,0,0,0,119,121,1,0,0,0,120,122,7,5,0,0,121,120,1,0,0,0,
        121,122,1,0,0,0,122,123,1,0,0,0,123,146,7,6,0,0,124,126,7,5,0,0,
        125,124,1,0,0,0,125,126,1,0,0,0,126,128,1,0,0,0,127,129,7,4,0,0,
        128,127,1,0,0,0,128,129,1,0,0,0,129,130,1,0,0,0,130,146,7,6,0,0,
        131,133,7,6,0,0,132,134,7,4,0,0,133,132,1,0,0,0,133,134,1,0,0,0,
        134,136,1,0,0,0,135,137,7,5,0,0,136,135,1,0,0,0,136,137,1,0,0,0,
        137,146,1,0,0,0,138,140,7,6,0,0,139,141,7,5,0,0,140,139,1,0,0,0,
        140,141,1,0,0,0,141,143,1,0,0,0,142,144,7,4,0,0,143,142,1,0,0,0,
        143,144,1,0,0,0,144,146,1,0,0,0,145,118,1,0,0,0,145,125,1,0,0,0,
        145,131,1,0,0,0,145,138,1,0,0,0,146,7,1,0,0,0,147,149,7,4,0,0,148,
        147,1,0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,156,7,7,0,0,151,
        153,7,7,0,0,152,154,7,4,0,0,153,152,1,0,0,0,153,154,1,0,0,0,154,
        156,1,0,0,0,155,148,1,0,0,0,155,151,1,0,0,0,156,9,1,0,0,0,157,159,
        7,4,0,0,158,157,1,0,0,0,158,159,1,0,0,0,159,160,1,0,0,0,160,166,
        7,3,0,0,161,163,7,3,0,0,162,164,7,4,0,0,163,162,1,0,0,0,163,164,
        1,0,0,0,164,166,1,0,0,0,165,158,1,0,0,0,165,161,1,0,0,0,166,11,1,
        0,0,0,167,169,7,4,0,0,168,167,1,0,0,0,168,169,1,0,0,0,169,171,1,
        0,0,0,170,172,7,5,0,0,171,170,1,0,0,0,171,172,1,0,0,0,172,173,1,
        0,0,0,173,182,5,31,0,0,174,176,5,31,0,0,175,177,7,4,0,0,176,175,
        1,0,0,0,176,177,1,0,0,0,177,179,1,0,0,0,178,180,7,5,0,0,179,178,
        1,0,0,0,179,180,1,0,0,0,180,182,1,0,0,0,181,168,1,0,0,0,181,174,
        1,0,0,0,182,13,1,0,0,0,183,185,7,4,0,0,184,183,1,0,0,0,184,185,1,
        0,0,0,185,187,1,0,0,0,186,188,7,5,0,0,187,186,1,0,0,0,187,188,1,
        0,0,0,188,189,1,0,0,0,189,198,5,43,0,0,190,192,5,43,0,0,191,193,
        7,4,0,0,192,191,1,0,0,0,192,193,1,0,0,0,193,195,1,0,0,0,194,196,
        7,5,0,0,195,194,1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,0,197,184,
        1,0,0,0,197,190,1,0,0,0,198,15,1,0,0,0,199,200,5,26,0,0,200,210,
        3,18,9,0,201,210,5,26,0,0,202,203,5,27,0,0,203,210,3,18,9,0,204,
        205,5,8,0,0,205,206,5,26,0,0,206,210,3,18,9,0,207,210,5,8,0,0,208,
        210,5,9,0,0,209,199,1,0,0,0,209,201,1,0,0,0,209,202,1,0,0,0,209,
        204,1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,17,1,0,0,0,211,214,
        6,9,-1,0,212,215,3,22,11,0,213,215,3,20,10,0,214,212,1,0,0,0,214,
        213,1,0,0,0,215,220,1,0,0,0,216,219,3,28,14,0,217,219,3,24,12,0,
        218,216,1,0,0,0,218,217,1,0,0,0,219,222,1,0,0,0,220,218,1,0,0,0,
        220,221,1,0,0,0,221,228,1,0,0,0,222,220,1,0,0,0,223,224,10,2,0,0,
        224,225,7,8,0,0,225,227,3,18,9,3,226,223,1,0,0,0,227,230,1,0,0,0,
        228,226,1,0,0,0,228,229,1,0,0,0,229,19,1,0,0,0,230,228,1,0,0,0,231,
        232,5,32,0,0,232,233,5,5,0,0,233,252,3,2,1,0,234,235,5,33,0,0,235,
        236,5,5,0,0,236,252,3,2,1,0,237,238,5,47,0,0,238,239,5,5,0,0,239,
        252,3,2,1,0,240,241,5,34,0,0,241,242,5,5,0,0,242,252,3,2,1,0,243,
        244,5,38,0,0,244,245,5,5,0,0,245,252,3,2,1,0,246,247,5,37,0,0,247,
        248,5,5,0,0,248,252,3,2,1,0,249,252,3,2,1,0,250,252,5,8,0,0,251,
        231,1,0,0,0,251,234,1,0,0,0,251,237,1,0,0,0,251,240,1,0,0,0,251,
        243,1,0,0,0,251,246,1,0,0,0,251,249,1,0,0,0,251,250,1,0,0,0,252,
        21,1,0,0,0,253,254,5,44,0,0,254,255,5,5,0,0,255,270,3,2,1,0,256,
        257,5,29,0,0,257,258,5,5,0,0,258,270,3,2,1,0,259,260,5,46,0,0,260,
        261,5,5,0,0,261,270,3,2,1,0,262,263,5,45,0,0,263,264,5,5,0,0,264,
        270,3,2,1,0,265,266,5,30,0,0,266,267,5,5,0,0,267,270,3,2,1,0,268,
        270,5,9,0,0,269,253,1,0,0,0,269,256,1,0,0,0,269,259,1,0,0,0,269,
        262,1,0,0,0,269,265,1,0,0,0,269,268,1,0,0,0,270,23,1,0,0,0,271,280,
        5,22,0,0,272,277,3,26,13,0,273,274,5,6,0,0,274,276,3,26,13,0,275,
        273,1,0,0,0,276,279,1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,
        281,1,0,0,0,279,277,1,0,0,0,280,272,1,0,0,0,280,281,1,0,0,0,281,
        282,1,0,0,0,282,283,5,7,0,0,283,25,1,0,0,0,284,285,3,2,1,0,285,27,
        1,0,0,0,286,287,5,20,0,0,287,288,3,2,1,0,288,289,5,2,0,0,289,29,
        1,0,0,0,290,291,7,9,0,0,291,31,1,0,0,0,292,298,5,63,0,0,293,298,
        5,61,0,0,294,298,5,62,0,0,295,298,5,64,0,0,296,298,5,28,0,0,297,
        292,1,0,0,0,297,293,1,0,0,0,297,294,1,0,0,0,297,295,1,0,0,0,297,
        296,1,0,0,0,298,33,1,0,0,0,299,300,5,55,0,0,300,304,5,56,0,0,301,
        305,5,57,0,0,302,305,5,58,0,0,303,305,3,2,1,0,304,301,1,0,0,0,304,
        302,1,0,0,0,304,303,1,0,0,0,305,35,1,0,0,0,306,307,5,10,0,0,307,
        308,5,70,0,0,308,37,1,0,0,0,48,45,48,66,72,78,84,90,92,94,100,108,
        115,118,121,125,128,133,136,140,143,145,148,153,155,158,163,165,
        168,171,176,179,181,184,187,192,195,197,209,214,218,220,228,251,
        269,277,280,297,304
    ]

class XPath31GrammarParser ( Parser ):

    grammarFileName = "XPath31Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "']'", "'}'", "':'", "'::'", "','", 
                     "')'", "'.'", "'..'", "'$'", "'='", "'>='", "'>>'", 
                     "'>'", "'<='", "'<<'", "'<'", "'-'", "'!='", "'['", 
                     "'{'", "'('", "'|'", "'+'", "'?'", "'/'", "'//'", "'*'", 
                     "'ancestor'", "'ancestor-or-self'", "'and'", "'child'", 
                     "'descendant'", "'descendant-or-self'", "'div'", "'except'", 
                     "'following'", "'following-sibling'", "'idiv'", "'in'", 
                     "'intersect'", "'mod'", "'or'", "'parent'", "'preceding'", 
                     "'preceding-sibling'", "'self'", "'to'", "'union'", 
                     "'any'", "'all'", "'zip'", "'product'", "'sequence'", 
                     "'on'", "'error'", "'discard'", "'fail'", "'nan'", 
                     "'inf'" ]

    symbolicNames = [ "<INVALID>", "BANG", "CB", "CC", "COLON", "COLONCOLON", 
                      "COMMA", "CP", "D", "DD", "DOLLAR", "EQ", "GE", "GG", 
                      "GT", "LE", "LL", "LT", "MINUS", "NE", "OB", "OC", 
                      "OP", "P", "PLUS", "QM", "SLASH", "SS", "STAR", "KW_ANCESTOR", 
                      "KW_ANCESTOR_OR_SELF", "KW_AND", "KW_CHILD", "KW_DESCENDANT", 
                      "KW_DESCENDANT_OR_SELF", "KW_DIV", "KW_EXCEPT", "KW_FOLLOWING", 
                      "KW_FOLLOWING_SIBLING", "KW_IDIV", "KW_IN", "KW_INTERSECT", 
                      "KW_MOD", "KW_OR", "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
                      "KW_SELF", "KW_TO", "KW_UNION", "KW_ANY", "KW_ALL", 
                      "KW_ZIP", "KW_PRODUCT", "KW_SEQUENCE", "KW_ON", "KW_ERROR", 
                      "KW_DISCARD", "KW_FAIL", "KW_NAN", "KW_INF", "RegexMatcher", 
                      "GlobMatcher", "StrictMatcher", "FuzzyMatcher", "IntegerLiteral", 
                      "DecimalLiteral", "DoubleLiteral", "StringLiteral", 
                      "BooleanLiteral", "Name", "Whitespace" ]

    RULE_xpath = 0
    RULE_expr = 1
    RULE_atomicorencapsulate = 2
    RULE_relop = 3
    RULE_mulop = 4
    RULE_addop = 5
    RULE_andop = 6
    RULE_orop = 7
    RULE_path = 8
    RULE_relpath = 9
    RULE_forwardstep = 10
    RULE_reversestep = 11
    RULE_argumentlist = 12
    RULE_argument = 13
    RULE_predicate = 14
    RULE_literal = 15
    RULE_matcher = 16
    RULE_coerecefallback = 17
    RULE_varref = 18

    ruleNames =  [ "xpath", "expr", "atomicorencapsulate", "relop", "mulop", 
                   "addop", "andop", "orop", "path", "relpath", "forwardstep", 
                   "reversestep", "argumentlist", "argument", "predicate", 
                   "literal", "matcher", "coerecefallback", "varref" ]

    EOF = Token.EOF
    BANG=1
    CB=2
    CC=3
    COLON=4
    COLONCOLON=5
    COMMA=6
    CP=7
    D=8
    DD=9
    DOLLAR=10
    EQ=11
    GE=12
    GG=13
    GT=14
    LE=15
    LL=16
    LT=17
    MINUS=18
    NE=19
    OB=20
    OC=21
    OP=22
    P=23
    PLUS=24
    QM=25
    SLASH=26
    SS=27
    STAR=28
    KW_ANCESTOR=29
    KW_ANCESTOR_OR_SELF=30
    KW_AND=31
    KW_CHILD=32
    KW_DESCENDANT=33
    KW_DESCENDANT_OR_SELF=34
    KW_DIV=35
    KW_EXCEPT=36
    KW_FOLLOWING=37
    KW_FOLLOWING_SIBLING=38
    KW_IDIV=39
    KW_IN=40
    KW_INTERSECT=41
    KW_MOD=42
    KW_OR=43
    KW_PARENT=44
    KW_PRECEDING=45
    KW_PRECEDING_SIBLING=46
    KW_SELF=47
    KW_TO=48
    KW_UNION=49
    KW_ANY=50
    KW_ALL=51
    KW_ZIP=52
    KW_PRODUCT=53
    KW_SEQUENCE=54
    KW_ON=55
    KW_ERROR=56
    KW_DISCARD=57
    KW_FAIL=58
    KW_NAN=59
    KW_INF=60
    RegexMatcher=61
    GlobMatcher=62
    StrictMatcher=63
    FuzzyMatcher=64
    IntegerLiteral=65
    DecimalLiteral=66
    DoubleLiteral=67
    StringLiteral=68
    BooleanLiteral=69
    Name=70
    Whitespace=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class XpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


        def EOF(self):
            return self.getToken(XPath31GrammarParser.EOF, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_xpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXpath" ):
                listener.enterXpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXpath" ):
                listener.exitXpath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitXpath" ):
                return visitor.visitXpath(self)
            else:
                return visitor.visitChildren(self)




    def xpath(self):

        localctx = XPath31GrammarParser.XpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_xpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.expr(0)
            self.state = 39
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

        def andop(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AndopContext,0)

        def coerecefallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerecefallbackContext,0)


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
        def coerecefallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerecefallbackContext,0)


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

        def atomicorencapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicorencapsulateContext,0)


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

        def relop(self):
            return self.getTypedRuleContext(XPath31GrammarParser.RelopContext,0)

        def coerecefallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerecefallbackContext,0)


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


    class ExprOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,i)

        def orop(self):
            return self.getTypedRuleContext(XPath31GrammarParser.OropContext,0)

        def coerecefallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerecefallbackContext,0)


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

        def mulop(self):
            return self.getTypedRuleContext(XPath31GrammarParser.MulopContext,0)

        def coerecefallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerecefallbackContext,0)


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

        def addop(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AddopContext,0)

        def coerecefallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerecefallbackContext,0)


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
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50, 51]:
                localctx = XPath31GrammarParser.ExprBoolAggregateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 42
                _la = self._input.LA(1)
                if not(_la==50 or _la==51):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 43
                self.expr(0)
                self.state = 45
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 44
                    self.coerecefallback()


                pass
            elif token in [8, 9, 10, 18, 20, 22, 24, 26, 27, 28, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]:
                localctx = XPath31GrammarParser.ExprAtomicOrEncapsulateContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.atomicorencapsulate()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = XPath31GrammarParser.ExprConcatenateContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 51
                        self.match(XPath31GrammarParser.COMMA)
                        self.state = 52
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = XPath31GrammarParser.ExprSetIntersectContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 54
                        _la = self._input.LA(1)
                        if not(_la==36 or _la==41):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 55
                        self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = XPath31GrammarParser.ExprSetUnionContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 57
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==49):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 58
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = XPath31GrammarParser.ExprRangeContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 60
                        self.match(XPath31GrammarParser.KW_TO)
                        self.state = 61
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = XPath31GrammarParser.ExprOrContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 63
                        self.orop()
                        self.state = 64
                        self.expr(0)
                        self.state = 66
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                        if la_ == 1:
                            self.state = 65
                            self.coerecefallback()


                        pass

                    elif la_ == 6:
                        localctx = XPath31GrammarParser.ExprAndContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 69
                        self.andop()
                        self.state = 70
                        self.expr(0)
                        self.state = 72
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                        if la_ == 1:
                            self.state = 71
                            self.coerecefallback()


                        pass

                    elif la_ == 7:
                        localctx = XPath31GrammarParser.ExprComparisonContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 75
                        self.relop()
                        self.state = 76
                        self.expr(0)
                        self.state = 78
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                        if la_ == 1:
                            self.state = 77
                            self.coerecefallback()


                        pass

                    elif la_ == 8:
                        localctx = XPath31GrammarParser.ExprAdditiveContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 81
                        self.addop()
                        self.state = 82
                        self.expr(0)
                        self.state = 84
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                        if la_ == 1:
                            self.state = 83
                            self.coerecefallback()


                        pass

                    elif la_ == 9:
                        localctx = XPath31GrammarParser.ExprMultiplicativeContext(self, XPath31GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 87
                        self.mulop()
                        self.state = 88
                        self.expr(0)
                        self.state = 90
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                        if la_ == 1:
                            self.state = 89
                            self.coerecefallback()


                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomicorencapsulateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_atomicorencapsulate

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprWrapForceListContext(AtomicorencapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicorencapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OB(self):
            return self.getToken(XPath31GrammarParser.OB, 0)
        def CB(self):
            return self.getToken(XPath31GrammarParser.CB, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ExprMatcherContext(AtomicorencapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicorencapsulateContext
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


    class ExprWrapContext(AtomicorencapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicorencapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP(self):
            return self.getToken(XPath31GrammarParser.OP, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)

        def CP(self):
            return self.getToken(XPath31GrammarParser.CP, 0)

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


    class ExprUnaryContext(AtomicorencapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicorencapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atomicorencapsulate(self):
            return self.getTypedRuleContext(XPath31GrammarParser.AtomicorencapsulateContext,0)

        def MINUS(self):
            return self.getToken(XPath31GrammarParser.MINUS, 0)
        def PLUS(self):
            return self.getToken(XPath31GrammarParser.PLUS, 0)
        def coerecefallback(self):
            return self.getTypedRuleContext(XPath31GrammarParser.CoerecefallbackContext,0)


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


    class ExprLiteralContext(AtomicorencapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicorencapsulateContext
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


    class ExprPathContext(AtomicorencapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicorencapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def path(self):
            return self.getTypedRuleContext(XPath31GrammarParser.PathContext,0)


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


    class ExprVariableContext(AtomicorencapsulateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.AtomicorencapsulateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varref(self):
            return self.getTypedRuleContext(XPath31GrammarParser.VarrefContext,0)


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



    def atomicorencapsulate(self):

        localctx = XPath31GrammarParser.AtomicorencapsulateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atomicorencapsulate)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 24]:
                localctx = XPath31GrammarParser.ExprUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                _la = self._input.LA(1)
                if not(_la==18 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 98
                self.atomicorencapsulate()
                self.state = 100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 99
                    self.coerecefallback()


                pass
            elif token in [22]:
                localctx = XPath31GrammarParser.ExprWrapContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(XPath31GrammarParser.OP)
                self.state = 103
                self.expr(0)
                self.state = 104
                self.match(XPath31GrammarParser.CP)
                pass
            elif token in [20]:
                localctx = XPath31GrammarParser.ExprWrapForceListContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.match(XPath31GrammarParser.OB)
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 9221133431182545927) != 0):
                    self.state = 107
                    self.expr(0)


                self.state = 110
                self.match(XPath31GrammarParser.CB)
                pass
            elif token in [28, 61, 62, 63, 64]:
                localctx = XPath31GrammarParser.ExprMatcherContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.matcher()
                pass
            elif token in [10]:
                localctx = XPath31GrammarParser.ExprVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.varref()
                pass
            elif token in [59, 60, 65, 66, 67, 68, 69, 70]:
                localctx = XPath31GrammarParser.ExprLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.literal()
                pass
            elif token in [8, 9, 26, 27]:
                localctx = XPath31GrammarParser.ExprPathContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.path()
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


    class RelopContext(ParserRuleContext):
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
            return XPath31GrammarParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = XPath31GrammarParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 117
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0):
                    self.state = 120
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 123
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 784384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0):
                    self.state = 124
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 127
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 130
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 784384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 784384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 132
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 136
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 135
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 784384) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 140
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 139
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 142
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
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


    class MulopContext(ParserRuleContext):
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
            return XPath31GrammarParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulop" ):
                return visitor.visitMulop(self)
            else:
                return visitor.visitChildren(self)




    def mulop(self):

        localctx = XPath31GrammarParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mulop)
        self._la = 0 # Token type
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 147
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 150
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4982430498816) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4982430498816) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 152
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
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


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(XPath31GrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(XPath31GrammarParser.MINUS, 0)

        def KW_ZIP(self):
            return self.getToken(XPath31GrammarParser.KW_ZIP, 0)

        def KW_PRODUCT(self):
            return self.getToken(XPath31GrammarParser.KW_PRODUCT, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddop" ):
                return visitor.visitAddop(self)
            else:
                return visitor.visitChildren(self)




    def addop(self):

        localctx = XPath31GrammarParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 157
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 160
                _la = self._input.LA(1)
                if not(_la==18 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                _la = self._input.LA(1)
                if not(_la==18 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 162
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
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


    class AndopContext(ParserRuleContext):
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
            return XPath31GrammarParser.RULE_andop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndop" ):
                listener.enterAndop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndop" ):
                listener.exitAndop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndop" ):
                return visitor.visitAndop(self)
            else:
                return visitor.visitChildren(self)




    def andop(self):

        localctx = XPath31GrammarParser.AndopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_andop)
        self._la = 0 # Token type
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 167
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0):
                    self.state = 170
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 173
                self.match(XPath31GrammarParser.KW_AND)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(XPath31GrammarParser.KW_AND)
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 175
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 179
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 178
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0)):
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


    class OropContext(ParserRuleContext):
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
            return XPath31GrammarParser.RULE_orop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrop" ):
                listener.enterOrop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrop" ):
                listener.exitOrop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrop" ):
                return visitor.visitOrop(self)
            else:
                return visitor.visitChildren(self)




    def orop(self):

        localctx = XPath31GrammarParser.OropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_orop)
        self._la = 0 # Token type
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 183
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0):
                    self.state = 186
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 189
                self.match(XPath31GrammarParser.KW_OR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(XPath31GrammarParser.KW_OR)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==52 or _la==53:
                    self.state = 191
                    _la = self._input.LA(1)
                    if not(_la==52 or _la==53):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 195
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 194
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392098230009856) != 0)):
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
        def relpath(self):
            return self.getTypedRuleContext(XPath31GrammarParser.RelpathContext,0)


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
        def relpath(self):
            return self.getTypedRuleContext(XPath31GrammarParser.RelpathContext,0)


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
        def relpath(self):
            return self.getTypedRuleContext(XPath31GrammarParser.RelpathContext,0)


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
        self.enterRule(localctx, 16, self.RULE_path)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                localctx = XPath31GrammarParser.PathFromRootContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(XPath31GrammarParser.SLASH)
                self.state = 200
                self.relpath(0)
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
                self.relpath(0)
                pass

            elif la_ == 4:
                localctx = XPath31GrammarParser.PathFromRelativeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(XPath31GrammarParser.D)
                self.state = 205
                self.match(XPath31GrammarParser.SLASH)
                self.state = 206
                self.relpath(0)
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


    class RelpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_relpath

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RelPathStepContext(RelpathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.RelpathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reversestep(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ReversestepContext,0)

        def forwardstep(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ForwardstepContext,0)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.PredicateContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.PredicateContext,i)

        def argumentlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ArgumentlistContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ArgumentlistContext,i)


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


    class RelPathChainContext(RelpathContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.RelpathContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def relpath(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.RelpathContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.RelpathContext,i)

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



    def relpath(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = XPath31GrammarParser.RelpathContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_relpath, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = XPath31GrammarParser.RelPathStepContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 212
                self.reversestep()
                pass

            elif la_ == 2:
                self.state = 213
                self.forwardstep()
                pass


            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 218
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [20]:
                        self.state = 216
                        self.predicate()
                        pass
                    elif token in [22]:
                        self.state = 217
                        self.argumentlist()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = XPath31GrammarParser.RelPathChainContext(self, XPath31GrammarParser.RelpathContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relpath)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not(_la==26 or _la==27):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.relpath(3) 
                self.state = 230
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ForwardstepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_forwardstep

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForwardStepSelfContext(ForwardstepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardstepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_SELF(self):
            return self.getToken(XPath31GrammarParser.KW_SELF, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ForwardStepFollowingSiblingContext(ForwardstepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardstepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FOLLOWING_SIBLING(self):
            return self.getToken(XPath31GrammarParser.KW_FOLLOWING_SIBLING, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ForwardStepDescendantOrSelfContext(ForwardstepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardstepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_DESCENDANT_OR_SELF(self):
            return self.getToken(XPath31GrammarParser.KW_DESCENDANT_OR_SELF, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ForwardStepDescendantContext(ForwardstepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardstepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_DESCENDANT(self):
            return self.getToken(XPath31GrammarParser.KW_DESCENDANT, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ForwardStepFollowingContext(ForwardstepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardstepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_FOLLOWING(self):
            return self.getToken(XPath31GrammarParser.KW_FOLLOWING, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ForwardStepDirectSelfContext(ForwardstepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardstepContext
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


    class ForwardStepChildContext(ForwardstepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardstepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_CHILD(self):
            return self.getToken(XPath31GrammarParser.KW_CHILD, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ForwardStepValueContext(ForwardstepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ForwardstepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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



    def forwardstep(self):

        localctx = XPath31GrammarParser.ForwardstepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forwardstep)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                localctx = XPath31GrammarParser.ForwardStepChildContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(XPath31GrammarParser.KW_CHILD)
                self.state = 232
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 233
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = XPath31GrammarParser.ForwardStepDescendantContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(XPath31GrammarParser.KW_DESCENDANT)
                self.state = 235
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 236
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = XPath31GrammarParser.ForwardStepSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.match(XPath31GrammarParser.KW_SELF)
                self.state = 238
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 239
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = XPath31GrammarParser.ForwardStepDescendantOrSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 240
                self.match(XPath31GrammarParser.KW_DESCENDANT_OR_SELF)
                self.state = 241
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 242
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = XPath31GrammarParser.ForwardStepFollowingSiblingContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 243
                self.match(XPath31GrammarParser.KW_FOLLOWING_SIBLING)
                self.state = 244
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 245
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = XPath31GrammarParser.ForwardStepFollowingContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 246
                self.match(XPath31GrammarParser.KW_FOLLOWING)
                self.state = 247
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 248
                self.expr(0)
                pass

            elif la_ == 7:
                localctx = XPath31GrammarParser.ForwardStepValueContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 249
                self.expr(0)
                pass

            elif la_ == 8:
                localctx = XPath31GrammarParser.ForwardStepDirectSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 250
                self.match(XPath31GrammarParser.D)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReversestepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_reversestep

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReverseStepDirectParentContext(ReversestepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReversestepContext
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


    class ReverseStepParentContext(ReversestepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReversestepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_PARENT(self):
            return self.getToken(XPath31GrammarParser.KW_PARENT, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ReverseStepAncestorContext(ReversestepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReversestepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_ANCESTOR(self):
            return self.getToken(XPath31GrammarParser.KW_ANCESTOR, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ReverseStepPrecedingSiblingContext(ReversestepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReversestepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_PRECEDING_SIBLING(self):
            return self.getToken(XPath31GrammarParser.KW_PRECEDING_SIBLING, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ReverseStepAncestorOrSelfContext(ReversestepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReversestepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_ANCESTOR_OR_SELF(self):
            return self.getToken(XPath31GrammarParser.KW_ANCESTOR_OR_SELF, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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


    class ReverseStepPrecedingContext(ReversestepContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a XPath31GrammarParser.ReversestepContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_PRECEDING(self):
            return self.getToken(XPath31GrammarParser.KW_PRECEDING, 0)
        def COLONCOLON(self):
            return self.getToken(XPath31GrammarParser.COLONCOLON, 0)
        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


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



    def reversestep(self):

        localctx = XPath31GrammarParser.ReversestepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_reversestep)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                localctx = XPath31GrammarParser.ReverseStepParentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(XPath31GrammarParser.KW_PARENT)
                self.state = 254
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 255
                self.expr(0)
                pass
            elif token in [29]:
                localctx = XPath31GrammarParser.ReverseStepAncestorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.match(XPath31GrammarParser.KW_ANCESTOR)
                self.state = 257
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 258
                self.expr(0)
                pass
            elif token in [46]:
                localctx = XPath31GrammarParser.ReverseStepPrecedingSiblingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.match(XPath31GrammarParser.KW_PRECEDING_SIBLING)
                self.state = 260
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 261
                self.expr(0)
                pass
            elif token in [45]:
                localctx = XPath31GrammarParser.ReverseStepPrecedingContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.match(XPath31GrammarParser.KW_PRECEDING)
                self.state = 263
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 264
                self.expr(0)
                pass
            elif token in [30]:
                localctx = XPath31GrammarParser.ReverseStepAncestorOrSelfContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 265
                self.match(XPath31GrammarParser.KW_ANCESTOR_OR_SELF)
                self.state = 266
                self.match(XPath31GrammarParser.COLONCOLON)
                self.state = 267
                self.expr(0)
                pass
            elif token in [9]:
                localctx = XPath31GrammarParser.ReverseStepDirectParentContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 268
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


    class ArgumentlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(XPath31GrammarParser.OP, 0)

        def CP(self):
            return self.getToken(XPath31GrammarParser.CP, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath31GrammarParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(XPath31GrammarParser.ArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(XPath31GrammarParser.COMMA)
            else:
                return self.getToken(XPath31GrammarParser.COMMA, i)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_argumentlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentlist" ):
                listener.enterArgumentlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentlist" ):
                listener.exitArgumentlist(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentlist" ):
                return visitor.visitArgumentlist(self)
            else:
                return visitor.visitChildren(self)




    def argumentlist(self):

        localctx = XPath31GrammarParser.ArgumentlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argumentlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(XPath31GrammarParser.OP)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 9221133431182545927) != 0):
                self.state = 272
                self.argument()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 273
                    self.match(XPath31GrammarParser.COMMA)
                    self.state = 274
                    self.argument()
                    self.state = 279
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 282
            self.match(XPath31GrammarParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(XPath31GrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = XPath31GrammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
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
            return XPath31GrammarParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicate" ):
                return visitor.visitPredicate(self)
            else:
                return visitor.visitChildren(self)




    def predicate(self):

        localctx = XPath31GrammarParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(XPath31GrammarParser.OB)
            self.state = 287
            self.expr(0)
            self.state = 288
            self.match(XPath31GrammarParser.CB)
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
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            _la = self._input.LA(1)
            if not(((((_la - 59)) & ~0x3f) == 0 and ((1 << (_la - 59)) & 4035) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_matcher)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                localctx = XPath31GrammarParser.MatcherStrictContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(XPath31GrammarParser.StrictMatcher)
                pass
            elif token in [61]:
                localctx = XPath31GrammarParser.MatcherRegexContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.match(XPath31GrammarParser.RegexMatcher)
                pass
            elif token in [62]:
                localctx = XPath31GrammarParser.MatcherGlobContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.match(XPath31GrammarParser.GlobMatcher)
                pass
            elif token in [64]:
                localctx = XPath31GrammarParser.MatcherFuzzyContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.match(XPath31GrammarParser.FuzzyMatcher)
                pass
            elif token in [28]:
                localctx = XPath31GrammarParser.MatcherWildcardContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 296
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


    class CoerecefallbackContext(ParserRuleContext):
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
            return XPath31GrammarParser.RULE_coerecefallback

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoerecefallback" ):
                listener.enterCoerecefallback(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoerecefallback" ):
                listener.exitCoerecefallback(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCoerecefallback" ):
                return visitor.visitCoerecefallback(self)
            else:
                return visitor.visitChildren(self)




    def coerecefallback(self):

        localctx = XPath31GrammarParser.CoerecefallbackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_coerecefallback)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(XPath31GrammarParser.KW_ON)
            self.state = 300
            self.match(XPath31GrammarParser.KW_ERROR)
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.state = 301
                self.match(XPath31GrammarParser.KW_DISCARD)
                pass
            elif token in [58]:
                self.state = 302
                self.match(XPath31GrammarParser.KW_FAIL)
                pass
            elif token in [8, 9, 10, 18, 20, 22, 24, 26, 27, 28, 50, 51, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]:
                self.state = 303
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


    class VarrefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(XPath31GrammarParser.DOLLAR, 0)

        def Name(self):
            return self.getToken(XPath31GrammarParser.Name, 0)

        def getRuleIndex(self):
            return XPath31GrammarParser.RULE_varref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarref" ):
                listener.enterVarref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarref" ):
                listener.exitVarref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarref" ):
                return visitor.visitVarref(self)
            else:
                return visitor.visitChildren(self)




    def varref(self):

        localctx = XPath31GrammarParser.VarrefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_varref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(XPath31GrammarParser.DOLLAR)
            self.state = 307
            self.match(XPath31GrammarParser.Name)
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
        self._predicates[9] = self.relpath_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

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
         

    def relpath_sempred(self, localctx:RelpathContext, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




