# Generated from /home/huu/Documents/PPL/initial/assignmentPPL/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\13\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
                     "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
                     "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
                     "'Fasle'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "<INVALID>", "'<'", "'>'", "'<='", 
                     "'>='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", 
                     "'['", "']'", "':'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                      "ELSE_IF", "END_BODY", "END_IF", "END_FOR", "END_WHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE_", "FALSE_", "END_DO", "PLUS", 
                      "PLUS_FLOAT", "SUB", "SUB_FLOAT", "MUL", "MUL_FLOAT", 
                      "DIV", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", "EQUAL", 
                      "NOT_EQUAl", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                      "LESS_FLOAT", "GREATER_FLOAT", "LESS_EQUAL_FLOAT", 
                      "GREATER_EQUAL_FLOAT", "LEFTPAREN", "RIGHTPAREN", 
                      "LEFTBRACKET", "RIGHTBRACKET", "COLON", "DOT", "COMMA", 
                      "SEMI", "LEFTBRACE", "RIGHTBRACE", "LITERAL", "INTEGER_LITERAL", 
                      "FLOATING_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
                      "IDENTIFIERS", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "UNCLOSE_STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    BODY=1
    BREAK=2
    CONTINUE=3
    DO=4
    ELSE=5
    ELSE_IF=6
    END_BODY=7
    END_IF=8
    END_FOR=9
    END_WHILE=10
    FOR=11
    FUNCTION=12
    IF=13
    PARAMETER=14
    RETURN=15
    THEN=16
    VAR=17
    WHILE=18
    TRUE_=19
    FALSE_=20
    END_DO=21
    PLUS=22
    PLUS_FLOAT=23
    SUB=24
    SUB_FLOAT=25
    MUL=26
    MUL_FLOAT=27
    DIV=28
    DIV_FLOAT=29
    MOD=30
    NOT=31
    AND=32
    OR=33
    EQUAL=34
    NOT_EQUAl=35
    LESS=36
    GREATER=37
    LESS_EQUAL=38
    GREATER_EQUAL=39
    LESS_FLOAT=40
    GREATER_FLOAT=41
    LESS_EQUAL_FLOAT=42
    GREATER_EQUAL_FLOAT=43
    LEFTPAREN=44
    RIGHTPAREN=45
    LEFTBRACKET=46
    RIGHTBRACKET=47
    COLON=48
    DOT=49
    COMMA=50
    SEMI=51
    LEFTBRACE=52
    RIGHTBRACE=53
    LITERAL=54
    INTEGER_LITERAL=55
    FLOATING_LITERAL=56
    BOOLEAN_LITERAL=57
    STRING_LITERAL=58
    IDENTIFIERS=59
    WS=60
    LINE_COMMENT=61
    BLOCK_COMMENT=62
    UNCLOSE_STRING=63
    ERROR_CHAR=64
    ILLEGAL_ESCAPE=65
    UNTERMINATED_COMMENT=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





