import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_101(self):
        inp = """**Hello**"""
        out = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,101))

    def test_102(self):
        inp = """nameOfStu = "This is a string: " """
        out = """nameOfStu,=,"This is a string: ",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,102))

    def test_103(self):
        inp = """**Nguyen*"""
        out = """Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,103))

    def test_104(self):
        inp = """ "Nguyen'"" """
        out = """"Nguyen'"",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,104))

    def test_105(self):
        inp = """x = 1.e-2 + 2.0000e+9 \. 80e9"""
        out = "x,=,1.e-2,+,2.0000e+9,\.,80e9,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(inp,out,105))

    def test_106(self):
        inp = """{ jkd }"""
        out = """{,jkd,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,106))

    def test_107(self):
        inp = """If(x=/=3 && y>6) Then:
            x=3;
            y=6;
        EndIf."""
        out = """If,(,x,=/=,3,&&,y,>,6,),Then,:,x,=,3,;,y,=,6,;,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,107))

    def test_108(self):
        inp = """Aabc"""
        out = "Error Token A"
        self.assertTrue(TestLexer.checkLexeme(inp,out,108))

    def test_109(self):
        inp = """ "nguyen van"""
        out = """Unclosed String: "nguyen van"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,109))

    def test_110(self):
        inp = """ "Nguyen \\t Van\\n Huu" """
        out = """\"Nguyen \\t Van\\n Huu\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,110))

    def test_111(self):
        inp = """ """
        out = """<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,111))

    def test_112(self):
        inp = """Varr x;"""
        out = """Var,r,x,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,112))

    def test_113(self):
        inp = """ "'Nguyen van" """
        out = """Illegal Escape In String: "'N"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,113))

    def test_114(self):
        inp = """x = True;"""
        out = """x,=,True,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,114))

    def test_115(self):
        inp = """15e--12"""
        out = """15,e,-,-,12,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,115))

    def test_116(self):
        inp = """**This
        is
        comment
        **isTrue == True;"""
        out = """isTrue,==,True,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,116))

    def test_117(self):
        inp = """17.2<=.48E1"""
        out = """17.2,<=.,48E1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,117))

    def test_118(self):
        inp = """0x12 + 0o45 - 23e0"""
        out = """0x12,+,0o45,-,23e0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,118))

    def test_119(self):
        inp = """If(x!=1)\nThen:y=y+1;"""
        out = """If,(,x,!=,1,),Then,:,y,=,y,+,1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,119))
    
    def test_120(self):
        inp = """str = "bkit\\kproc" """
        out = """str,=,Illegal Escape In String: "bkit\k"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,120))
    
    def test_121(self):
        inp = """Var: x = True;
Function: fact
    Parameter: n
    Body:
        If n == 0 Then
            Return 1;
        Else
            Return n * fact (n - 1);
        EndIf.
    EndBody.
Function: main
    Body:
        x = 10;
        fact (x);
    EndBody."""

        out = """Var,:,x,=,True,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,121))