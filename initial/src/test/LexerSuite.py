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

    def test_11(self):
        inp = ""
        out = "<EOF>"
        num = 11
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_12(self):
        inp = "VAR..."
        out = "Error Token V"
        num = 12
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_13(self):
        inp = "\"'Nguyen van\""
        out = "\"'Nguyen van\",<EOF>"
        num = 13
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_14(self):
        inp = "x = True;"
        out = "x,=,True,;,<EOF>"
        num = 14
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_15(self):
        inp = "15e--12"
        out = "15,e,-,-,12,<EOF>"
        num = 15
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_16(self):
        inp = "**thisiscomment**isTrue == True;"
        out = "isTrue,==,True,;,<EOF>"
        num = 16
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_17(self):
        inp = "17.2<=.48e1"
        out = "17.2,<=.,48e1,<EOF>"
        num = 17
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_18(self):
        inp = "0x12 + 0o45 - 23e0"
        out = "0x12,+,0o45,-,23e0,<EOF>"
        num = 18
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))

    def test_19(self):
        inp = "If(x!=1)\nThen:y=y+1;"
        out = "If,(,x,!=,1,),Then,:,y,=,y,+,1,;,<EOF>"
        num = 19
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))
    
    def test_20(self):
        inp = "**NguyenVan*"
        out = "Unterminated Comment"
        num = 20
        self.assertTrue(TestLexer.checkLexeme(inp,out,num))