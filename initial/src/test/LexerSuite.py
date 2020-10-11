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
        out = """Unclosed String: nguyen van"""
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
        inp = """ "'Assignment" """
        out = """Illegal Escape In String: 'A"""
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
        inp = """str = "bkit\kproc" """
        out = """str,=,Illegal Escape In String: bkit\k"""
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

    def test_122(self):
        inp = """ "Escape\wrongstring """
        out = """Illegal Escape In String: Escape\w"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,122))

    def test_123(self):
        inp = """ "Backs\\\\"  """
        out = """"Backs\\\\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,123))

    def test_124(self):
        inp = """var[5][6] = {1,2,3,4,5};"""
        out = """var,[,5,],[,6,],=,{,1,,,2,,,3,,,4,,,5,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,124))

    def test_125(self):
        inp = """BreaK EOF"""
        out = """Error Token B"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,125))

    def test_126(self):
        inp = """x+x+x+.3"""
        out = """x,+,x,+,x,+.,3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,126))
    
    def test_127(self):
        inp = """;;;"""
        out = """;,;,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,127))

    def test_128(self):
        inp = """0X0x"""
        out = """0,Error Token X"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,128))

    def test_129(self):
        inp = """0O89"""
        out = """0,Error Token O"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,129))

    def test_130(self):
        inp = """0123e-5"""
        out = """0,123e-5,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,130))

    def test_131(self):
        inp = """0X7f + 0O45 == 0"""
        out = """0X7f,+,0O45,==,0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,131))

    def test_132(self):
        inp = """True == 2.1"""
        out = """True,==,2.1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,132))

    def test_133(self):
        inp = """ "this is my string\\n" + 1.2e100 """
        out = """"this is my string\\n",+,1.2e100,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,133))

    def test_134(self):
        inp = """ "\\n" + "\\f" + "\\r" + "\\t" + "\\'" + "\\\\" """
        out = """"\\n",+,"\\f",+,"\\r",+,"\\t",+,"\\'",+,"\\\\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,134))

    def test_135(self):
        inp = """ "This is an error string\\g" """
        out = """Illegal Escape In String: This is an error string\\g"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,135))

    def test_136(self):
        inp = """ "This is a unclose string\n" """
        out = """Unclosed String: This is a unclose string\n"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,136))

    def test_137(self):
        inp = """!True == False||True"""
        out = """!,True,==,False,||,True,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,137))

    def test_138(self):
        inp = """hcMUT + Then"""
        out = """hcMUT,+,Then,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,138))

    def test_139(self):
        inp = """function_call       ()"""
        out = """function_call,(,),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,139))

    def test_140(self):
        inp = """Operator"""
        out = """Error Token O"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,140))

    def test_141(self):
        inp = """b = float_of_int (a) +. 2.0;"""
        out = """b,=,float_of_int,(,a,),+.,2.0,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,141))

    def test_142(self):
        inp = """\\\\"""
        out = """\\,\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,142))

    def test_143(self):
        inp = """\\.\\.3.0\\"""
        out = """\\.,\\.,3.0,\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,143))

    def test_144(self):
        inp = """#5+5"""
        out = """Error Token #"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,144))

    def test_145(self):
        inp = """If condition Then statement_list"""
        out = """If,condition,Then,statement_list,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,145))

    def test_146(self):
        inp = """      x         <eof>"""
        out = """x,<,eof,>,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,146))

    def test_147(self):
        inp = """this is test_147"""
        out = """this,is,test_147,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,147))

    def test_148(self):
        inp = """ "\\Nguyen" """
        out = """Illegal Escape In String: \\N"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,148))

    def test_149(self):
        inp = """4.5*.4e-1-.05"""
        out = """4.5,*.,4e-1,-.,0,5,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,149))

    def test_150(self):
        inp = """Continue;"""
        out = """Continue,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,150))

    def test_151(self):
        inp ="""****Function: hello Parameter:x Body:EndBody.**"""
        out = """Function,:,hello,Parameter,:,x,Body,:,EndBody,.,Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,151))

    
