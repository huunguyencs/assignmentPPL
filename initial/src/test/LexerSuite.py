import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("Function:\n\tBody:\n\tEndBody","Function,:,Body,:,EndBody,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var 10.5e-15","Var,10.5e-15,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("While ++;","While,+,+,;,<EOF>",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("**Nguyen\n*van**Huu**","<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme("7.5<=.8.e-9","7.5,<=.,8.e-9,<EOF>",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme("(12+8=/=21.) || 8 != 5","(,12,+,8,=/=,21.,),||,8,!=,5,<EOF>",106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme("0X12 + 0o45 * 45","0X12,+,0o45,*,45,<EOF>",107))