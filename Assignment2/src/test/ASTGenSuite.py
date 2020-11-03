import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = r"""Function: foo
    Parameter: a[5], b
    Body:
        Var: i = 0;
        While i < 5 Do
            a[i] = b +. 1.0;
            i = i + 1;
        EndWhile.
    EndBody."""
        expect = """Program([VarDecl(Id(x),IntLiteral(7)),VarDecl(Id(y),[5])])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

 
   