# Generated from XPath31Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,78,628,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,
        78,7,78,2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,
        84,2,85,7,85,2,86,7,86,2,87,7,87,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,
        1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,
        10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,
        16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,
        21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,
        27,1,27,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,
        34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,
        37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,
        39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,
        41,1,41,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,
        43,1,43,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,46,1,46,1,46,1,46,1,
        46,1,46,1,46,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,
        48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,
        48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,
        51,1,51,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,1,
        53,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,
        56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,58,1,
        58,1,58,1,58,1,58,1,58,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,59,1,
        60,1,60,1,60,1,60,1,60,1,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,1,
        63,1,63,1,63,1,63,1,63,1,63,1,64,1,64,1,64,1,64,1,64,1,64,1,64,1,
        64,1,64,1,65,1,65,1,65,1,65,1,65,1,65,1,66,1,66,1,66,1,67,1,67,1,
        67,1,68,1,68,1,68,1,69,1,69,1,69,1,70,1,70,1,70,1,71,1,71,1,72,1,
        72,1,72,1,72,1,72,5,72,530,8,72,10,72,12,72,533,9,72,3,72,535,8,
        72,1,73,1,73,1,73,1,73,1,73,5,73,542,8,73,10,73,12,73,545,9,73,3,
        73,547,8,73,3,73,549,8,73,1,73,1,73,3,73,553,8,73,1,73,1,73,1,74,
        1,74,1,75,1,75,1,75,1,75,1,75,1,75,1,75,1,75,1,75,3,75,568,8,75,
        1,76,1,76,1,76,5,76,573,8,76,10,76,12,76,576,9,76,1,76,1,76,1,76,
        1,76,5,76,582,8,76,10,76,12,76,585,9,76,1,76,3,76,588,8,76,1,77,
        1,77,1,77,1,78,1,78,1,78,1,79,1,79,1,80,1,80,1,81,4,81,601,8,81,
        11,81,12,81,602,1,82,1,82,1,83,1,83,1,84,1,84,3,84,611,8,84,1,85,
        1,85,5,85,615,8,85,10,85,12,85,618,9,85,1,86,1,86,1,87,4,87,623,
        8,87,11,87,12,87,624,1,87,1,87,0,0,88,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,
        81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,
        51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,
        121,61,123,62,125,63,127,64,129,65,131,66,133,67,135,68,137,69,139,
        70,141,71,143,72,145,73,147,74,149,75,151,76,153,0,155,0,157,0,159,
        77,161,0,163,0,165,0,167,0,169,0,171,0,173,0,175,78,1,0,9,1,0,48,
        57,2,0,69,69,101,101,2,0,43,43,45,45,1,0,34,34,1,0,39,39,15,0,65,
        90,95,95,97,122,192,214,216,246,248,767,880,893,895,8191,8204,8205,
        8304,8591,11264,12271,12289,55295,63744,64975,65008,65533,65536,
        983039,5,0,45,46,48,57,183,183,768,879,8255,8256,5,0,9,10,13,13,
        32,55295,57344,65533,65536,1114111,3,0,9,10,13,13,32,32,633,0,1,
        1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,
        0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,
        0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,
        0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,
        0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,
        0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,
        0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,
        0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,
        0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,
        0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,
        0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,
        111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,
        0,0,0,121,1,0,0,0,0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,
        1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,
        0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,
        0,0,0,0,149,1,0,0,0,0,151,1,0,0,0,0,159,1,0,0,0,0,175,1,0,0,0,1,
        177,1,0,0,0,3,179,1,0,0,0,5,181,1,0,0,0,7,183,1,0,0,0,9,185,1,0,
        0,0,11,187,1,0,0,0,13,189,1,0,0,0,15,192,1,0,0,0,17,194,1,0,0,0,
        19,196,1,0,0,0,21,198,1,0,0,0,23,201,1,0,0,0,25,203,1,0,0,0,27,205,
        1,0,0,0,29,208,1,0,0,0,31,211,1,0,0,0,33,213,1,0,0,0,35,216,1,0,
        0,0,37,219,1,0,0,0,39,221,1,0,0,0,41,223,1,0,0,0,43,226,1,0,0,0,
        45,228,1,0,0,0,47,230,1,0,0,0,49,232,1,0,0,0,51,234,1,0,0,0,53,237,
        1,0,0,0,55,239,1,0,0,0,57,241,1,0,0,0,59,243,1,0,0,0,61,246,1,0,
        0,0,63,248,1,0,0,0,65,257,1,0,0,0,67,274,1,0,0,0,69,278,1,0,0,0,
        71,284,1,0,0,0,73,295,1,0,0,0,75,314,1,0,0,0,77,318,1,0,0,0,79,325,
        1,0,0,0,81,335,1,0,0,0,83,353,1,0,0,0,85,358,1,0,0,0,87,361,1,0,
        0,0,89,371,1,0,0,0,91,375,1,0,0,0,93,378,1,0,0,0,95,385,1,0,0,0,
        97,395,1,0,0,0,99,413,1,0,0,0,101,418,1,0,0,0,103,421,1,0,0,0,105,
        427,1,0,0,0,107,431,1,0,0,0,109,435,1,0,0,0,111,439,1,0,0,0,113,
        447,1,0,0,0,115,456,1,0,0,0,117,459,1,0,0,0,119,465,1,0,0,0,121,
        473,1,0,0,0,123,478,1,0,0,0,125,482,1,0,0,0,127,486,1,0,0,0,129,
        492,1,0,0,0,131,501,1,0,0,0,133,507,1,0,0,0,135,510,1,0,0,0,137,
        513,1,0,0,0,139,516,1,0,0,0,141,519,1,0,0,0,143,522,1,0,0,0,145,
        534,1,0,0,0,147,548,1,0,0,0,149,556,1,0,0,0,151,567,1,0,0,0,153,
        587,1,0,0,0,155,589,1,0,0,0,157,592,1,0,0,0,159,595,1,0,0,0,161,
        597,1,0,0,0,163,600,1,0,0,0,165,604,1,0,0,0,167,606,1,0,0,0,169,
        610,1,0,0,0,171,612,1,0,0,0,173,619,1,0,0,0,175,622,1,0,0,0,177,
        178,5,126,0,0,178,2,1,0,0,0,179,180,5,33,0,0,180,4,1,0,0,0,181,182,
        5,64,0,0,182,6,1,0,0,0,183,184,5,93,0,0,184,8,1,0,0,0,185,186,5,
        125,0,0,186,10,1,0,0,0,187,188,5,58,0,0,188,12,1,0,0,0,189,190,5,
        58,0,0,190,191,5,58,0,0,191,14,1,0,0,0,192,193,5,44,0,0,193,16,1,
        0,0,0,194,195,5,41,0,0,195,18,1,0,0,0,196,197,5,46,0,0,197,20,1,
        0,0,0,198,199,5,46,0,0,199,200,5,46,0,0,200,22,1,0,0,0,201,202,5,
        36,0,0,202,24,1,0,0,0,203,204,5,61,0,0,204,26,1,0,0,0,205,206,5,
        62,0,0,206,207,5,61,0,0,207,28,1,0,0,0,208,209,5,62,0,0,209,210,
        5,62,0,0,210,30,1,0,0,0,211,212,5,62,0,0,212,32,1,0,0,0,213,214,
        5,60,0,0,214,215,5,61,0,0,215,34,1,0,0,0,216,217,5,60,0,0,217,218,
        5,60,0,0,218,36,1,0,0,0,219,220,5,60,0,0,220,38,1,0,0,0,221,222,
        5,45,0,0,222,40,1,0,0,0,223,224,5,33,0,0,224,225,5,61,0,0,225,42,
        1,0,0,0,226,227,5,91,0,0,227,44,1,0,0,0,228,229,5,123,0,0,229,46,
        1,0,0,0,230,231,5,40,0,0,231,48,1,0,0,0,232,233,5,124,0,0,233,50,
        1,0,0,0,234,235,5,124,0,0,235,236,5,124,0,0,236,52,1,0,0,0,237,238,
        5,43,0,0,238,54,1,0,0,0,239,240,5,63,0,0,240,56,1,0,0,0,241,242,
        5,47,0,0,242,58,1,0,0,0,243,244,5,47,0,0,244,245,5,47,0,0,245,60,
        1,0,0,0,246,247,5,42,0,0,247,62,1,0,0,0,248,249,5,97,0,0,249,250,
        5,110,0,0,250,251,5,99,0,0,251,252,5,101,0,0,252,253,5,115,0,0,253,
        254,5,116,0,0,254,255,5,111,0,0,255,256,5,114,0,0,256,64,1,0,0,0,
        257,258,5,97,0,0,258,259,5,110,0,0,259,260,5,99,0,0,260,261,5,101,
        0,0,261,262,5,115,0,0,262,263,5,116,0,0,263,264,5,111,0,0,264,265,
        5,114,0,0,265,266,5,45,0,0,266,267,5,111,0,0,267,268,5,114,0,0,268,
        269,5,45,0,0,269,270,5,115,0,0,270,271,5,101,0,0,271,272,5,108,0,
        0,272,273,5,102,0,0,273,66,1,0,0,0,274,275,5,97,0,0,275,276,5,110,
        0,0,276,277,5,100,0,0,277,68,1,0,0,0,278,279,5,99,0,0,279,280,5,
        104,0,0,280,281,5,105,0,0,281,282,5,108,0,0,282,283,5,100,0,0,283,
        70,1,0,0,0,284,285,5,100,0,0,285,286,5,101,0,0,286,287,5,115,0,0,
        287,288,5,99,0,0,288,289,5,101,0,0,289,290,5,110,0,0,290,291,5,100,
        0,0,291,292,5,97,0,0,292,293,5,110,0,0,293,294,5,116,0,0,294,72,
        1,0,0,0,295,296,5,100,0,0,296,297,5,101,0,0,297,298,5,115,0,0,298,
        299,5,99,0,0,299,300,5,101,0,0,300,301,5,110,0,0,301,302,5,100,0,
        0,302,303,5,97,0,0,303,304,5,110,0,0,304,305,5,116,0,0,305,306,5,
        45,0,0,306,307,5,111,0,0,307,308,5,114,0,0,308,309,5,45,0,0,309,
        310,5,115,0,0,310,311,5,101,0,0,311,312,5,108,0,0,312,313,5,102,
        0,0,313,74,1,0,0,0,314,315,5,100,0,0,315,316,5,105,0,0,316,317,5,
        118,0,0,317,76,1,0,0,0,318,319,5,101,0,0,319,320,5,120,0,0,320,321,
        5,99,0,0,321,322,5,101,0,0,322,323,5,112,0,0,323,324,5,116,0,0,324,
        78,1,0,0,0,325,326,5,102,0,0,326,327,5,111,0,0,327,328,5,108,0,0,
        328,329,5,108,0,0,329,330,5,111,0,0,330,331,5,119,0,0,331,332,5,
        105,0,0,332,333,5,110,0,0,333,334,5,103,0,0,334,80,1,0,0,0,335,336,
        5,102,0,0,336,337,5,111,0,0,337,338,5,108,0,0,338,339,5,108,0,0,
        339,340,5,111,0,0,340,341,5,119,0,0,341,342,5,105,0,0,342,343,5,
        110,0,0,343,344,5,103,0,0,344,345,5,45,0,0,345,346,5,115,0,0,346,
        347,5,105,0,0,347,348,5,98,0,0,348,349,5,108,0,0,349,350,5,105,0,
        0,350,351,5,110,0,0,351,352,5,103,0,0,352,82,1,0,0,0,353,354,5,105,
        0,0,354,355,5,100,0,0,355,356,5,105,0,0,356,357,5,118,0,0,357,84,
        1,0,0,0,358,359,5,105,0,0,359,360,5,110,0,0,360,86,1,0,0,0,361,362,
        5,105,0,0,362,363,5,110,0,0,363,364,5,116,0,0,364,365,5,101,0,0,
        365,366,5,114,0,0,366,367,5,115,0,0,367,368,5,101,0,0,368,369,5,
        99,0,0,369,370,5,116,0,0,370,88,1,0,0,0,371,372,5,109,0,0,372,373,
        5,111,0,0,373,374,5,100,0,0,374,90,1,0,0,0,375,376,5,111,0,0,376,
        377,5,114,0,0,377,92,1,0,0,0,378,379,5,112,0,0,379,380,5,97,0,0,
        380,381,5,114,0,0,381,382,5,101,0,0,382,383,5,110,0,0,383,384,5,
        116,0,0,384,94,1,0,0,0,385,386,5,112,0,0,386,387,5,114,0,0,387,388,
        5,101,0,0,388,389,5,99,0,0,389,390,5,101,0,0,390,391,5,100,0,0,391,
        392,5,105,0,0,392,393,5,110,0,0,393,394,5,103,0,0,394,96,1,0,0,0,
        395,396,5,112,0,0,396,397,5,114,0,0,397,398,5,101,0,0,398,399,5,
        99,0,0,399,400,5,101,0,0,400,401,5,100,0,0,401,402,5,105,0,0,402,
        403,5,110,0,0,403,404,5,103,0,0,404,405,5,45,0,0,405,406,5,115,0,
        0,406,407,5,105,0,0,407,408,5,98,0,0,408,409,5,108,0,0,409,410,5,
        105,0,0,410,411,5,110,0,0,411,412,5,103,0,0,412,98,1,0,0,0,413,414,
        5,115,0,0,414,415,5,101,0,0,415,416,5,108,0,0,416,417,5,102,0,0,
        417,100,1,0,0,0,418,419,5,116,0,0,419,420,5,111,0,0,420,102,1,0,
        0,0,421,422,5,117,0,0,422,423,5,110,0,0,423,424,5,105,0,0,424,425,
        5,111,0,0,425,426,5,110,0,0,426,104,1,0,0,0,427,428,5,97,0,0,428,
        429,5,110,0,0,429,430,5,121,0,0,430,106,1,0,0,0,431,432,5,97,0,0,
        432,433,5,108,0,0,433,434,5,108,0,0,434,108,1,0,0,0,435,436,5,122,
        0,0,436,437,5,105,0,0,437,438,5,112,0,0,438,110,1,0,0,0,439,440,
        5,112,0,0,440,441,5,114,0,0,441,442,5,111,0,0,442,443,5,100,0,0,
        443,444,5,117,0,0,444,445,5,99,0,0,445,446,5,116,0,0,446,112,1,0,
        0,0,447,448,5,115,0,0,448,449,5,101,0,0,449,450,5,113,0,0,450,451,
        5,117,0,0,451,452,5,101,0,0,452,453,5,110,0,0,453,454,5,99,0,0,454,
        455,5,101,0,0,455,114,1,0,0,0,456,457,5,111,0,0,457,458,5,110,0,
        0,458,116,1,0,0,0,459,460,5,101,0,0,460,461,5,114,0,0,461,462,5,
        114,0,0,462,463,5,111,0,0,463,464,5,114,0,0,464,118,1,0,0,0,465,
        466,5,100,0,0,466,467,5,105,0,0,467,468,5,115,0,0,468,469,5,99,0,
        0,469,470,5,97,0,0,470,471,5,114,0,0,471,472,5,100,0,0,472,120,1,
        0,0,0,473,474,5,102,0,0,474,475,5,97,0,0,475,476,5,105,0,0,476,477,
        5,108,0,0,477,122,1,0,0,0,478,479,5,110,0,0,479,480,5,97,0,0,480,
        481,5,110,0,0,481,124,1,0,0,0,482,483,5,105,0,0,483,484,5,110,0,
        0,484,485,5,102,0,0,485,126,1,0,0,0,486,487,5,108,0,0,487,488,5,
        97,0,0,488,489,5,98,0,0,489,490,5,101,0,0,490,491,5,108,0,0,491,
        128,1,0,0,0,492,493,5,100,0,0,493,494,5,105,0,0,494,495,5,115,0,
        0,495,496,5,116,0,0,496,497,5,105,0,0,497,498,5,110,0,0,498,499,
        5,99,0,0,499,500,5,116,0,0,500,130,1,0,0,0,501,502,5,99,0,0,502,
        503,5,111,0,0,503,504,5,117,0,0,504,505,5,110,0,0,505,506,5,116,
        0,0,506,132,1,0,0,0,507,508,5,114,0,0,508,509,3,153,76,0,509,134,
        1,0,0,0,510,511,5,103,0,0,511,512,3,153,76,0,512,136,1,0,0,0,513,
        514,5,115,0,0,514,515,3,153,76,0,515,138,1,0,0,0,516,517,5,102,0,
        0,517,518,3,153,76,0,518,140,1,0,0,0,519,520,5,105,0,0,520,521,3,
        153,76,0,521,142,1,0,0,0,522,523,3,163,81,0,523,144,1,0,0,0,524,
        525,5,46,0,0,525,535,3,163,81,0,526,527,3,163,81,0,527,531,5,46,
        0,0,528,530,7,0,0,0,529,528,1,0,0,0,530,533,1,0,0,0,531,529,1,0,
        0,0,531,532,1,0,0,0,532,535,1,0,0,0,533,531,1,0,0,0,534,524,1,0,
        0,0,534,526,1,0,0,0,535,146,1,0,0,0,536,537,5,46,0,0,537,549,3,163,
        81,0,538,546,3,163,81,0,539,543,5,46,0,0,540,542,7,0,0,0,541,540,
        1,0,0,0,542,545,1,0,0,0,543,541,1,0,0,0,543,544,1,0,0,0,544,547,
        1,0,0,0,545,543,1,0,0,0,546,539,1,0,0,0,546,547,1,0,0,0,547,549,
        1,0,0,0,548,536,1,0,0,0,548,538,1,0,0,0,549,550,1,0,0,0,550,552,
        7,1,0,0,551,553,7,2,0,0,552,551,1,0,0,0,552,553,1,0,0,0,553,554,
        1,0,0,0,554,555,3,163,81,0,555,148,1,0,0,0,556,557,3,153,76,0,557,
        150,1,0,0,0,558,559,5,116,0,0,559,560,5,114,0,0,560,561,5,117,0,
        0,561,568,5,101,0,0,562,563,5,102,0,0,563,564,5,97,0,0,564,565,5,
        108,0,0,565,566,5,115,0,0,566,568,5,101,0,0,567,558,1,0,0,0,567,
        562,1,0,0,0,568,152,1,0,0,0,569,574,5,34,0,0,570,573,8,3,0,0,571,
        573,3,155,77,0,572,570,1,0,0,0,572,571,1,0,0,0,573,576,1,0,0,0,574,
        572,1,0,0,0,574,575,1,0,0,0,575,577,1,0,0,0,576,574,1,0,0,0,577,
        588,5,34,0,0,578,583,5,39,0,0,579,582,8,4,0,0,580,582,3,157,78,0,
        581,579,1,0,0,0,581,580,1,0,0,0,582,585,1,0,0,0,583,581,1,0,0,0,
        583,584,1,0,0,0,584,586,1,0,0,0,585,583,1,0,0,0,586,588,5,39,0,0,
        587,569,1,0,0,0,587,578,1,0,0,0,588,154,1,0,0,0,589,590,5,34,0,0,
        590,591,5,34,0,0,591,156,1,0,0,0,592,593,5,39,0,0,593,594,5,39,0,
        0,594,158,1,0,0,0,595,596,3,171,85,0,596,160,1,0,0,0,597,598,3,173,
        86,0,598,162,1,0,0,0,599,601,7,0,0,0,600,599,1,0,0,0,601,602,1,0,
        0,0,602,600,1,0,0,0,602,603,1,0,0,0,603,164,1,0,0,0,604,605,3,161,
        80,0,605,166,1,0,0,0,606,607,7,5,0,0,607,168,1,0,0,0,608,611,3,167,
        83,0,609,611,7,6,0,0,610,608,1,0,0,0,610,609,1,0,0,0,611,170,1,0,
        0,0,612,616,3,167,83,0,613,615,3,169,84,0,614,613,1,0,0,0,615,618,
        1,0,0,0,616,614,1,0,0,0,616,617,1,0,0,0,617,172,1,0,0,0,618,616,
        1,0,0,0,619,620,7,7,0,0,620,174,1,0,0,0,621,623,7,8,0,0,622,621,
        1,0,0,0,623,624,1,0,0,0,624,622,1,0,0,0,624,625,1,0,0,0,625,626,
        1,0,0,0,626,627,6,87,0,0,627,176,1,0,0,0,17,0,531,534,543,546,548,
        552,567,572,574,581,583,587,602,610,616,624,1,6,0,0
    ]

class XPath31GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TILDE = 1
    BANG = 2
    AT = 3
    CB = 4
    CC = 5
    COLON = 6
    COLONCOLON = 7
    COMMA = 8
    CP = 9
    D = 10
    DD = 11
    DOLLAR = 12
    EQ = 13
    GE = 14
    GG = 15
    GT = 16
    LE = 17
    LL = 18
    LT = 19
    MINUS = 20
    NE = 21
    OB = 22
    OC = 23
    OP = 24
    P = 25
    PP = 26
    PLUS = 27
    QM = 28
    SLASH = 29
    SS = 30
    STAR = 31
    KW_ANCESTOR = 32
    KW_ANCESTOR_OR_SELF = 33
    KW_AND = 34
    KW_CHILD = 35
    KW_DESCENDANT = 36
    KW_DESCENDANT_OR_SELF = 37
    KW_DIV = 38
    KW_EXCEPT = 39
    KW_FOLLOWING = 40
    KW_FOLLOWING_SIBLING = 41
    KW_IDIV = 42
    KW_IN = 43
    KW_INTERSECT = 44
    KW_MOD = 45
    KW_OR = 46
    KW_PARENT = 47
    KW_PRECEDING = 48
    KW_PRECEDING_SIBLING = 49
    KW_SELF = 50
    KW_TO = 51
    KW_UNION = 52
    KW_ANY = 53
    KW_ALL = 54
    KW_ZIP = 55
    KW_PRODUCT = 56
    KW_SEQUENCE = 57
    KW_ON = 58
    KW_ERROR = 59
    KW_DISCARD = 60
    KW_FAIL = 61
    KW_NAN = 62
    KW_INF = 63
    KW_LABEL = 64
    KW_DISTINCT = 65
    KW_COUNT = 66
    RegexMatcher = 67
    GlobMatcher = 68
    StrictMatcher = 69
    FuzzyMatcher = 70
    IgnoreCaseMatcher = 71
    IntegerLiteral = 72
    DecimalLiteral = 73
    DoubleLiteral = 74
    StringLiteral = 75
    BooleanLiteral = 76
    Name = 77
    Whitespace = 78

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'~'", "'!'", "'@'", "']'", "'}'", "':'", "'::'", "','", "')'", 
            "'.'", "'..'", "'$'", "'='", "'>='", "'>>'", "'>'", "'<='", 
            "'<<'", "'<'", "'-'", "'!='", "'['", "'{'", "'('", "'|'", "'||'", 
            "'+'", "'?'", "'/'", "'//'", "'*'", "'ancestor'", "'ancestor-or-self'", 
            "'and'", "'child'", "'descendant'", "'descendant-or-self'", 
            "'div'", "'except'", "'following'", "'following-sibling'", "'idiv'", 
            "'in'", "'intersect'", "'mod'", "'or'", "'parent'", "'preceding'", 
            "'preceding-sibling'", "'self'", "'to'", "'union'", "'any'", 
            "'all'", "'zip'", "'product'", "'sequence'", "'on'", "'error'", 
            "'discard'", "'fail'", "'nan'", "'inf'", "'label'", "'distinct'", 
            "'count'" ]

    symbolicNames = [ "<INVALID>",
            "TILDE", "BANG", "AT", "CB", "CC", "COLON", "COLONCOLON", "COMMA", 
            "CP", "D", "DD", "DOLLAR", "EQ", "GE", "GG", "GT", "LE", "LL", 
            "LT", "MINUS", "NE", "OB", "OC", "OP", "P", "PP", "PLUS", "QM", 
            "SLASH", "SS", "STAR", "KW_ANCESTOR", "KW_ANCESTOR_OR_SELF", 
            "KW_AND", "KW_CHILD", "KW_DESCENDANT", "KW_DESCENDANT_OR_SELF", 
            "KW_DIV", "KW_EXCEPT", "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", 
            "KW_IDIV", "KW_IN", "KW_INTERSECT", "KW_MOD", "KW_OR", "KW_PARENT", 
            "KW_PRECEDING", "KW_PRECEDING_SIBLING", "KW_SELF", "KW_TO", 
            "KW_UNION", "KW_ANY", "KW_ALL", "KW_ZIP", "KW_PRODUCT", "KW_SEQUENCE", 
            "KW_ON", "KW_ERROR", "KW_DISCARD", "KW_FAIL", "KW_NAN", "KW_INF", 
            "KW_LABEL", "KW_DISTINCT", "KW_COUNT", "RegexMatcher", "GlobMatcher", 
            "StrictMatcher", "FuzzyMatcher", "IgnoreCaseMatcher", "IntegerLiteral", 
            "DecimalLiteral", "DoubleLiteral", "StringLiteral", "BooleanLiteral", 
            "Name", "Whitespace" ]

    ruleNames = [ "TILDE", "BANG", "AT", "CB", "CC", "COLON", "COLONCOLON", 
                  "COMMA", "CP", "D", "DD", "DOLLAR", "EQ", "GE", "GG", 
                  "GT", "LE", "LL", "LT", "MINUS", "NE", "OB", "OC", "OP", 
                  "P", "PP", "PLUS", "QM", "SLASH", "SS", "STAR", "KW_ANCESTOR", 
                  "KW_ANCESTOR_OR_SELF", "KW_AND", "KW_CHILD", "KW_DESCENDANT", 
                  "KW_DESCENDANT_OR_SELF", "KW_DIV", "KW_EXCEPT", "KW_FOLLOWING", 
                  "KW_FOLLOWING_SIBLING", "KW_IDIV", "KW_IN", "KW_INTERSECT", 
                  "KW_MOD", "KW_OR", "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
                  "KW_SELF", "KW_TO", "KW_UNION", "KW_ANY", "KW_ALL", "KW_ZIP", 
                  "KW_PRODUCT", "KW_SEQUENCE", "KW_ON", "KW_ERROR", "KW_DISCARD", 
                  "KW_FAIL", "KW_NAN", "KW_INF", "KW_LABEL", "KW_DISTINCT", 
                  "KW_COUNT", "RegexMatcher", "GlobMatcher", "StrictMatcher", 
                  "FuzzyMatcher", "IgnoreCaseMatcher", "IntegerLiteral", 
                  "DecimalLiteral", "DoubleLiteral", "StringLiteral", "BooleanLiteral", 
                  "FragStringLiteral", "FragEscapeQuot", "FragEscapeApos", 
                  "Name", "Char", "FragDigits", "CommentContents", "FragNameStartChar", 
                  "FragNameChar", "FragmentName", "FragChar", "Whitespace" ]

    grammarFileName = "XPath31Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


