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
        inp = """x = 1.e-2 + 2.0000e+9 \\. 80e9"""
        out = "x,=,1.e-2,+,2.0000e+9,\\.,80e9,<EOF>"
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
        inp = """str = "bkit\\kproc" """
        out = """str,=,Illegal Escape In String: bkit\\k"""
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
        inp = """ "Escape\\wrongstring" """
        out = """Illegal Escape In String: Escape\\w"""
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

    def test_152(self):
        inp = """ "abcd'a" """
        out = """Illegal Escape In String: abcd'a"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    def test_153(self):
        inp = """{ ** Ambiguous ** }"""
        out = """{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,153))
    
    def test_154(self):
        inp = """Var**x=5**x=6;"""
        out = """Var,x,=,6,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,154))
    
    def test_155(self):
        inp = """If(x=5) Then ====="""
        out = """If,(,x,=,5,),Then,==,==,=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,155))
    
    def test_156(self):
        inp = """ "\\\\\\" """
        out = """Illegal Escape In String: \\\\\\\""""
        self.assertTrue(TestLexer.checkLexeme(inp,out,156))
    
    def test_157(self):
        inp = """{"abc",5,6.e-8};"""
        out = """{,"abc",,,5,,,6.e-8,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,157))
    
    def test_158(self):
        inp = """vAR@ x = 7;"""
        out = """vAR,Error Token @"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,158))
    
    def test_159(self):
        inp = """_test"""
        out = """Error Token _"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,159))
    
    def test_160(self):
        inp = """ "escape@@string'"" """
        out = """"escape@@string'"",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,160))
    
    def test_161(self):
        inp = """ "helloWorld"hello"a\nThis is a string" """
        out = """"helloWorld",hello,Unclosed String: a\n"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,161))
    
    def test_162(self):
        inp = """Function: testfor Body: For(i = 0,i!=1,i=i+1) DoEndFor.EndBody."""
        out = """Function,:,testfor,Body,:,For,(,i,=,0,,,i,!=,1,,,i,=,i,+,1,),Do,EndFor,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    def test_163(self):
        inp = """Return True;"""
        out = """Return,True,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,163))
    
    def test_164(self):
        inp = """Var x=-5.e9;"""
        out = """Var,x,=,-,5.e9,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,164))
    
    def test_165(self):
        inp = """Function: area(){}"""
        out = """Function,:,area,(,),{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,165))
    
    def test_166(self):
        inp = """int foo(){}"""
        out = """int,foo,(,),{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,166))
    
    def test_167(self):
        inp = """Var: er___s<ert>"""
        out = """Var,:,er___s,<,ert,>,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,167))
    
    def test_168(self):
        inp = """<eof>**This is a comment**"""
        out = """<,eof,>,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,168))
    
    def test_169(self):
        inp = """If the is === -0X65e;"""
        out = """If,the,is,==,=,-,0X65e,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,169))
    
    def test_170(self):
        inp = """tt==========ttt"""
        out = """tt,==,==,==,==,==,ttt,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,170))
    
    def test_171(self):
        inp = """ "helloWorld'\""""
        out = """Unclosed String: helloWorld'\""""
        self.assertTrue(TestLexer.checkLexeme(inp,out,171))
    
    def test_172(self):
        inp = """00001e0"""
        out = """0,0,0,0,1e0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,172))
    
    def test_173(self):
        inp = """0000xx45"""
        out = """0,0,0,0,xx45,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,173))
    
    def test_174(self):
        inp = """0x7e-5"""
        out = """0x7e,-,5,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,174))
    
    def test_175(self):
        inp = """**Comment**Var: x = "Nguyen\'" """
        out = """Var,:,x,=,Unclosed String: Nguyen'" """
        self.assertTrue(TestLexer.checkLexeme(inp,out,175))
    
    def test_176(self):
        inp = """45aRT-e+5.2e1"""
        out = """45,aRT,-,e,+,5.2e1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    def test_177(self):
        inp = """154.9+=/==5"""
        out = """154.9,+,=/=,=,5,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    def test_178(self):
        inp = """uT578e-5"""
        out = """uT578e,-,5,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    def test_179(self):
        inp = """19++2==0e-1"""
        out = """19,+,+,2,==,0e-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    def test_180(self):
        inp = """While x !==/=5r Then\no"""
        out = """While,x,!=,=/=,5,r,Then,o,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_181(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_182(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_183(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_184(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_185(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_186(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_187(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_188(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_189(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_190(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_191(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_192(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_193(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_194(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_195(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_196(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_197(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_198(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_199(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    
    # def test_200(self):
    #     inp = """ """
    #     out = """ """
    #     self.assertTrue(TestLexer.checkLexeme(inp,out,152))
    