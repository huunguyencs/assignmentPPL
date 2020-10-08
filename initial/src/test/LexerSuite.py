import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_1(self):
        inp = """**Hello**"""
        out = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,1))

    def test_2(self):
        inp = """nameOfStu = "This is a string: " """
        out = """nameOfStu,=,"This is a string: ",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,2))

    def test_3(self):
        inp = """**Nguyen*"""
        out = """Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,3))

    def test_4(self):
        inp = """ "Nguyen'"" """
        out = """"Nguyen'"",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,4))

    def test_5(self):
        inp = """x = 1.e-2 + 2.0000e+9 \. 80e9"""
        out = "x,=,1.e-2,+,2.0000e+9,\.,80e9,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(inp,out,5))

    def test_6(self):
        inp = """{ jkd }"""
        out = """{,jkd,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,6))

    def test_7(self):
        inp = """If(x=/=3 && y>6) Then:
            x=3;
            y=6;
        EndIf."""
        out = """If,(,x,=/=,3,&&,y,>,6,),Then,:,x,=,3,;,y,=,6,;,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,7))

    def test_8(self):
        inp = """Aabc"""
        out = "Error Token A"
        self.assertTrue(TestLexer.checkLexeme(inp,out,8))

    def test_9(self):
        inp = """ "nguyen van"""
        out = """Unclosed String: "nguyen van"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,9))

    def test_10(self):
        inp = """ "Nguyen \\t Van\\n Huu" """
        out = """\"Nguyen \\t Van\\n Huu\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,10))

    def test_11(self):
        inp = """ """
        out = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,11))

    def test_12(self):
        inp = """VAR..."""
        out = """Error Token V"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,12))

    def test_13(self):
        inp = """ "'Nguyen van" """
        out = """Illegal Escape In String: "'N"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,13))

    def test_14(self):
        inp = """x = True;"""
        out = """x,=,True,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,14))

    def test_15(self):
        inp = """15e--12"""
        out = """15,e,-,-,12,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,15))

    def test_16(self):
        inp = """**This
        is
        comment
        **isTrue == True;"""
        out = """isTrue,==,True,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,16))

    def test_17(self):
        inp = """17.2<=.48E1"""
        out = """17.2,<=.,48E1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,17))

    def test_18(self):
        inp = """0x12 + 0o45 - 23e0"""
        out = """0x12,+,0o45,-,23e0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,18))

    def test_19(self):
        inp = """If(x!=1)\nThen:y=y+1;"""
        out = """If,(,x,!=,1,),Then,:,y,=,y,+,1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,19))
    
    def test_20(self):
        inp = """str = "bkit\\kproc" """
        out = """str,=,Illegal Escape In String: "bkit\k"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,20))
