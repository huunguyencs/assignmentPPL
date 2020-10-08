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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
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
                     "'Fasle'", "'EndDo'", "'='", "'+'", "'+.'", "'-'", 
                     "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "<INVALID>", "'<'", "'>'", 
                     "'<='", "'>='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", 
                     "')'", "'['", "']'", "':'", "'.'", "','", "';'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                      "ELSE_IF", "END_BODY", "END_IF", "END_FOR", "END_WHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE_", "FALSE_", "END_DO", "ASSIGN", 
                      "ADD", "ADD_FLOAT", "SUB", "SUB_FLOAT", "MUL", "MUL_FLOAT", 
                      "DIV", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", "EQUAL", 
                      "NOT_EQUAL", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                      "LESS_FLOAT", "GREATER_FLOAT", "LESS_EQUAL_FLOAT", 
                      "GREATER_EQUAL_FLOAT", "LP", "RP", "LR", "RR", "CL", 
                      "DOT", "CM", "SM", "LB", "RB", "INTLIT", "FLOATLIT", 
                      "BOOLLIT", "STRINGLIT", "ID", "WS", "COMMENT", "UNCLOSE_STRING", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
    ASSIGN=22
    ADD=23
    ADD_FLOAT=24
    SUB=25
    SUB_FLOAT=26
    MUL=27
    MUL_FLOAT=28
    DIV=29
    DIV_FLOAT=30
    MOD=31
    NOT=32
    AND=33
    OR=34
    EQUAL=35
    NOT_EQUAL=36
    LESS=37
    GREATER=38
    LESS_EQUAL=39
    GREATER_EQUAL=40
    LESS_FLOAT=41
    GREATER_FLOAT=42
    LESS_EQUAL_FLOAT=43
    GREATER_EQUAL_FLOAT=44
    LP=45
    RP=46
    LR=47
    RR=48
    CL=49
    DOT=50
    CM=51
    SM=52
    LB=53
    RB=54
    INTLIT=55
    FLOATLIT=56
    BOOLLIT=57
    STRINGLIT=58
    ID=59
    WS=60
    COMMENT=61
    UNCLOSE_STRING=62
    ERROR_CHAR=63
    ILLEGAL_ESCAPE=64
    UNTERMINATED_COMMENT=65

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





