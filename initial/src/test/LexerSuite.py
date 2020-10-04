import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_1(self):
        inp = "**Hello**"
        out = "<EOF>"
        num = 1
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_2(self):
        inp = "nameOfStu = \"Huu\""
        out = "nameOfStu,=,\"Huu\",<EOF>"
        num = 2
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_3(self):
        inp = "**Nguyen*"
        out = "Unterminated Comment"
        num = 3
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_4(self):
        inp = "\"Nguyen Van '\"Huu'\"\""
        out = "\"Nguyen Van '\"Huu'\"\",<EOF>"
        num = 4
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_5(self):
        inp = "x = 1.e-2 + 2.0000e+9 \. 80e9"
        out = "x,=,1.e-2,+,2.0000e+9,\.,80e9,<EOF>"
        num = 5
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_6(self):
        inp = "{ hehe }"
        out = "{,hehe,},<EOF>"
        num = 6
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_7(self):
        inp = "If(x=/=3 && y>6)\n\tThen:\n\t\tx=3;\n\t\ty=6;\nEndIf."
        out = "If,(,x,=/=,3,&&,y,>,6,),Then,:,x,=,3,;,y,=,6,;,EndIf,.,<EOF>"
        num = 7
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_8(self):
        inp = "Aabc"
        out = "Error Token A"
        num = 8
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_9(self):
        inp = "\"nguyen van"
        out = "Illegal Escape In String: \"nguyen van"
        num = 9
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_10(self):
        inp = "\"hello\nAdam;"
        out = "Unclosed String: \"hello"
        num = 10
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))