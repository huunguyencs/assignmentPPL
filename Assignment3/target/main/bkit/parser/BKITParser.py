# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u019b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4o\n\4\f\4\16\4r\13\4\3")
        buf.write("\5\3\5\3\5\5\5w\n\5\3\6\3\6\5\6{\n\6\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u0081\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0089\n\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\7\t\u0090\n\t\f\t\16\t\u0093\13\t\3\n")
        buf.write("\3\n\3\n\7\n\u0098\n\n\f\n\16\n\u009b\13\n\3\n\7\n\u009e")
        buf.write("\n\n\f\n\16\n\u00a1\13\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\5\13\u00af\n\13\3\f\7\f\u00b2")
        buf.write("\n\f\f\f\16\f\u00b5\13\f\3\f\7\f\u00b8\n\f\f\f\16\f\u00bb")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\7\16\u00c4\n\16\f")
        buf.write("\16\16\16\u00c7\13\16\3\16\5\16\u00ca\n\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u0106\n\30\f\30\16\30\u0109\13\30\5\30\u010b")
        buf.write("\n\30\3\30\3\30\3\30\3\31\3\31\5\31\u0112\n\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\5\32\u011b\n\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\7\33\u0124\n\33\f\33\16\33\u0127")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0130\n")
        buf.write("\34\f\34\16\34\u0133\13\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\7\35\u013c\n\35\f\35\16\35\u013f\13\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u0146\n\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\7\37\u014d\n\37\f\37\16\37\u0150\13\37\3 \3 \5 ")
        buf.write("\u0154\n \3!\3!\3!\3!\3!\7!\u015b\n!\f!\16!\u015e\13!")
        buf.write("\5!\u0160\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u016a\n")
        buf.write("\"\3#\3#\3#\5#\u016f\n#\3#\5#\u0172\n#\3$\3$\3$\3$\5$")
        buf.write("\u0178\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3)\7)\u0186")
        buf.write("\n)\f)\16)\u0189\13)\5)\u018b\n)\3)\3)\3*\3*\3*\3*\5*")
        buf.write("\u0193\n*\3+\3+\5+\u0197\n+\3,\3,\3,\2\6\64\668<-\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTV\2\b\3\2\33\34\3\2%.\3\2#$\3\2\31\34")
        buf.write("\3\2\35!\3\2\25\26\2\u019d\2[\3\2\2\2\4f\3\2\2\2\6k\3")
        buf.write("\2\2\2\bs\3\2\2\2\nx\3\2\2\2\f|\3\2\2\2\16\u0082\3\2\2")
        buf.write("\2\20\u008c\3\2\2\2\22\u0094\3\2\2\2\24\u00ae\3\2\2\2")
        buf.write("\26\u00b3\3\2\2\2\30\u00bc\3\2\2\2\32\u00c1\3\2\2\2\34")
        buf.write("\u00ce\3\2\2\2\36\u00d3\3\2\2\2 \u00d8\3\2\2\2\"\u00db")
        buf.write("\3\2\2\2$\u00e4\3\2\2\2&\u00ec\3\2\2\2(\u00f3\3\2\2\2")
        buf.write("*\u00fa\3\2\2\2,\u00fd\3\2\2\2.\u0100\3\2\2\2\60\u010f")
        buf.write("\3\2\2\2\62\u011a\3\2\2\2\64\u011c\3\2\2\2\66\u0128\3")
        buf.write("\2\2\28\u0134\3\2\2\2:\u0145\3\2\2\2<\u0147\3\2\2\2>\u0153")
        buf.write("\3\2\2\2@\u0155\3\2\2\2B\u0169\3\2\2\2D\u0171\3\2\2\2")
        buf.write("F\u0173\3\2\2\2H\u0179\3\2\2\2J\u017b\3\2\2\2L\u017d\3")
        buf.write("\2\2\2N\u017f\3\2\2\2P\u0181\3\2\2\2R\u0192\3\2\2\2T\u0196")
        buf.write("\3\2\2\2V\u0198\3\2\2\2XZ\5\4\3\2YX\3\2\2\2Z]\3\2\2\2")
        buf.write("[Y\3\2\2\2[\\\3\2\2\2\\a\3\2\2\2][\3\2\2\2^`\5\16\b\2")
        buf.write("_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3")
        buf.write("\2\2\2de\7\2\2\3e\3\3\2\2\2fg\7\23\2\2gh\7\63\2\2hi\5")
        buf.write("\6\4\2ij\7\66\2\2j\5\3\2\2\2kp\5\b\5\2lm\7\65\2\2mo\5")
        buf.write("\b\5\2nl\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\7\3\2")
        buf.write("\2\2rp\3\2\2\2sv\5\n\6\2tu\7\30\2\2uw\5T+\2vt\3\2\2\2")
        buf.write("vw\3\2\2\2w\t\3\2\2\2xz\7<\2\2y{\5\f\7\2zy\3\2\2\2z{\3")
        buf.write("\2\2\2{\13\3\2\2\2|}\7\61\2\2}~\79\2\2~\u0080\7\62\2\2")
        buf.write("\177\u0081\5\f\7\2\u0080\177\3\2\2\2\u0080\u0081\3\2\2")
        buf.write("\2\u0081\r\3\2\2\2\u0082\u0083\7\16\2\2\u0083\u0084\7")
        buf.write("\63\2\2\u0084\u0088\7<\2\2\u0085\u0086\7\20\2\2\u0086")
        buf.write("\u0087\7\63\2\2\u0087\u0089\5\20\t\2\u0088\u0085\3\2\2")
        buf.write("\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b")
        buf.write("\5\22\n\2\u008b\17\3\2\2\2\u008c\u0091\5\n\6\2\u008d\u008e")
        buf.write("\7\65\2\2\u008e\u0090\5\n\6\2\u008f\u008d\3\2\2\2\u0090")
        buf.write("\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\21\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\7\3")
        buf.write("\2\2\u0095\u0099\7\63\2\2\u0096\u0098\5\4\3\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\u009f\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009c\u009e\5\24\13\2\u009d\u009c\3\2\2\2\u009e\u00a1")
        buf.write("\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0")
        buf.write("\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7\t\2\2")
        buf.write("\u00a3\u00a4\7\64\2\2\u00a4\23\3\2\2\2\u00a5\u00af\5\30")
        buf.write("\r\2\u00a6\u00af\5*\26\2\u00a7\u00af\5.\30\2\u00a8\u00af")
        buf.write("\5,\27\2\u00a9\u00af\5(\25\2\u00aa\u00af\5\"\22\2\u00ab")
        buf.write("\u00af\5\32\16\2\u00ac\u00af\5\60\31\2\u00ad\u00af\5&")
        buf.write("\24\2\u00ae\u00a5\3\2\2\2\u00ae\u00a6\3\2\2\2\u00ae\u00a7")
        buf.write("\3\2\2\2\u00ae\u00a8\3\2\2\2\u00ae\u00a9\3\2\2\2\u00ae")
        buf.write("\u00aa\3\2\2\2\u00ae\u00ab\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00ad\3\2\2\2\u00af\25\3\2\2\2\u00b0\u00b2\5\4")
        buf.write("\3\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b9\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b6\u00b8\5\24\13\2\u00b7\u00b6\3\2\2")
        buf.write("\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\27\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd")
        buf.write("\5D#\2\u00bd\u00be\7\30\2\2\u00be\u00bf\5\62\32\2\u00bf")
        buf.write("\u00c0\7\66\2\2\u00c0\31\3\2\2\2\u00c1\u00c5\5\34\17\2")
        buf.write("\u00c2\u00c4\5\36\20\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00ca\5 \21\2")
        buf.write("\u00c9\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\u00cc\7\n\2\2\u00cc\u00cd\7\64\2\2\u00cd")
        buf.write("\33\3\2\2\2\u00ce\u00cf\7\17\2\2\u00cf\u00d0\5\62\32\2")
        buf.write("\u00d0\u00d1\7\22\2\2\u00d1\u00d2\5\26\f\2\u00d2\35\3")
        buf.write("\2\2\2\u00d3\u00d4\7\b\2\2\u00d4\u00d5\5\62\32\2\u00d5")
        buf.write("\u00d6\7\22\2\2\u00d6\u00d7\5\26\f\2\u00d7\37\3\2\2\2")
        buf.write("\u00d8\u00d9\7\7\2\2\u00d9\u00da\5\26\f\2\u00da!\3\2\2")
        buf.write("\2\u00db\u00dc\7\r\2\2\u00dc\u00dd\7/\2\2\u00dd\u00de")
        buf.write("\5$\23\2\u00de\u00df\7\60\2\2\u00df\u00e0\7\6\2\2\u00e0")
        buf.write("\u00e1\5\26\f\2\u00e1\u00e2\7\13\2\2\u00e2\u00e3\7\64")
        buf.write("\2\2\u00e3#\3\2\2\2\u00e4\u00e5\7<\2\2\u00e5\u00e6\7\30")
        buf.write("\2\2\u00e6\u00e7\5\62\32\2\u00e7\u00e8\7\65\2\2\u00e8")
        buf.write("\u00e9\5\62\32\2\u00e9\u00ea\7\65\2\2\u00ea\u00eb\5\62")
        buf.write("\32\2\u00eb%\3\2\2\2\u00ec\u00ed\7\24\2\2\u00ed\u00ee")
        buf.write("\5\62\32\2\u00ee\u00ef\7\6\2\2\u00ef\u00f0\5\26\f\2\u00f0")
        buf.write("\u00f1\7\f\2\2\u00f1\u00f2\7\64\2\2\u00f2\'\3\2\2\2\u00f3")
        buf.write("\u00f4\7\6\2\2\u00f4\u00f5\5\26\f\2\u00f5\u00f6\7\24\2")
        buf.write("\2\u00f6\u00f7\5\62\32\2\u00f7\u00f8\7\27\2\2\u00f8\u00f9")
        buf.write("\7\64\2\2\u00f9)\3\2\2\2\u00fa\u00fb\7\4\2\2\u00fb\u00fc")
        buf.write("\7\66\2\2\u00fc+\3\2\2\2\u00fd\u00fe\7\5\2\2\u00fe\u00ff")
        buf.write("\7\66\2\2\u00ff-\3\2\2\2\u0100\u0101\7<\2\2\u0101\u010a")
        buf.write("\7/\2\2\u0102\u0107\5\62\32\2\u0103\u0104\7\65\2\2\u0104")
        buf.write("\u0106\5\62\32\2\u0105\u0103\3\2\2\2\u0106\u0109\3\2\2")
        buf.write("\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010b")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u0102\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\7\60\2")
        buf.write("\2\u010d\u010e\7\66\2\2\u010e/\3\2\2\2\u010f\u0111\7\21")
        buf.write("\2\2\u0110\u0112\5\62\32\2\u0111\u0110\3\2\2\2\u0111\u0112")
        buf.write("\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\7\66\2\2\u0114")
        buf.write("\61\3\2\2\2\u0115\u0116\5\64\33\2\u0116\u0117\5H%\2\u0117")
        buf.write("\u0118\5\64\33\2\u0118\u011b\3\2\2\2\u0119\u011b\5\64")
        buf.write("\33\2\u011a\u0115\3\2\2\2\u011a\u0119\3\2\2\2\u011b\63")
        buf.write("\3\2\2\2\u011c\u011d\b\33\1\2\u011d\u011e\5\66\34\2\u011e")
        buf.write("\u0125\3\2\2\2\u011f\u0120\f\4\2\2\u0120\u0121\5J&\2\u0121")
        buf.write("\u0122\5\66\34\2\u0122\u0124\3\2\2\2\u0123\u011f\3\2\2")
        buf.write("\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126")
        buf.write("\3\2\2\2\u0126\65\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129")
        buf.write("\b\34\1\2\u0129\u012a\58\35\2\u012a\u0131\3\2\2\2\u012b")
        buf.write("\u012c\f\4\2\2\u012c\u012d\5L\'\2\u012d\u012e\58\35\2")
        buf.write("\u012e\u0130\3\2\2\2\u012f\u012b\3\2\2\2\u0130\u0133\3")
        buf.write("\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\67")
        buf.write("\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0135\b\35\1\2\u0135")
        buf.write("\u0136\5:\36\2\u0136\u013d\3\2\2\2\u0137\u0138\f\4\2\2")
        buf.write("\u0138\u0139\5N(\2\u0139\u013a\5:\36\2\u013a\u013c\3\2")
        buf.write("\2\2\u013b\u0137\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e9\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140\u0141\t\2\2\2\u0141\u0146\5:\36\2\u0142")
        buf.write("\u0143\7\"\2\2\u0143\u0146\5:\36\2\u0144\u0146\5<\37\2")
        buf.write("\u0145\u0140\3\2\2\2\u0145\u0142\3\2\2\2\u0145\u0144\3")
        buf.write("\2\2\2\u0146;\3\2\2\2\u0147\u0148\b\37\1\2\u0148\u0149")
        buf.write("\5> \2\u0149\u014e\3\2\2\2\u014a\u014b\f\4\2\2\u014b\u014d")
        buf.write("\5F$\2\u014c\u014a\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f=\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0151\u0154\5@!\2\u0152\u0154\5B\"\2\u0153\u0151")
        buf.write("\3\2\2\2\u0153\u0152\3\2\2\2\u0154?\3\2\2\2\u0155\u0156")
        buf.write("\7<\2\2\u0156\u015f\7/\2\2\u0157\u015c\5\62\32\2\u0158")
        buf.write("\u0159\7\65\2\2\u0159\u015b\5\62\32\2\u015a\u0158\3\2")
        buf.write("\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015f")
        buf.write("\u0157\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161\u0162\7\60\2\2\u0162A\3\2\2\2\u0163\u016a\5T+\2")
        buf.write("\u0164\u0165\7/\2\2\u0165\u0166\5\62\32\2\u0166\u0167")
        buf.write("\7\60\2\2\u0167\u016a\3\2\2\2\u0168\u016a\7<\2\2\u0169")
        buf.write("\u0163\3\2\2\2\u0169\u0164\3\2\2\2\u0169\u0168\3\2\2\2")
        buf.write("\u016aC\3\2\2\2\u016b\u0172\7<\2\2\u016c\u016f\7<\2\2")
        buf.write("\u016d\u016f\5@!\2\u016e\u016c\3\2\2\2\u016e\u016d\3\2")
        buf.write("\2\2\u016f\u0170\3\2\2\2\u0170\u0172\5F$\2\u0171\u016b")
        buf.write("\3\2\2\2\u0171\u016e\3\2\2\2\u0172E\3\2\2\2\u0173\u0174")
        buf.write("\7\61\2\2\u0174\u0175\5\62\32\2\u0175\u0177\7\62\2\2\u0176")
        buf.write("\u0178\5F$\2\u0177\u0176\3\2\2\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("G\3\2\2\2\u0179\u017a\t\3\2\2\u017aI\3\2\2\2\u017b\u017c")
        buf.write("\t\4\2\2\u017cK\3\2\2\2\u017d\u017e\t\5\2\2\u017eM\3\2")
        buf.write("\2\2\u017f\u0180\t\6\2\2\u0180O\3\2\2\2\u0181\u018a\7")
        buf.write("\67\2\2\u0182\u0187\5T+\2\u0183\u0184\7\65\2\2\u0184\u0186")
        buf.write("\5T+\2\u0185\u0183\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185")
        buf.write("\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018b\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u018a\u0182\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018c\u018d\78\2\2\u018dQ\3\2\2\2")
        buf.write("\u018e\u0193\79\2\2\u018f\u0193\7:\2\2\u0190\u0193\5V")
        buf.write(",\2\u0191\u0193\7;\2\2\u0192\u018e\3\2\2\2\u0192\u018f")
        buf.write("\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("S\3\2\2\2\u0194\u0197\5R*\2\u0195\u0197\5P)\2\u0196\u0194")
        buf.write("\3\2\2\2\u0196\u0195\3\2\2\2\u0197U\3\2\2\2\u0198\u0199")
        buf.write("\t\7\2\2\u0199W\3\2\2\2%[apvz\u0080\u0088\u0091\u0099")
        buf.write("\u009f\u00ae\u00b3\u00b9\u00c5\u00c9\u0107\u010a\u0111")
        buf.write("\u011a\u0125\u0131\u013d\u0145\u014e\u0153\u015c\u015f")
        buf.write("\u0169\u016e\u0171\u0177\u0187\u018a\u0192\u0196")
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
                     "'False'", "'EndDo'", "'='", "'+'", "'+.'", "'-'", 
                     "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "<INVALID>", "'<'", "'>'", 
                     "'<='", "'>='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", 
                     "')'", "'['", "']'", "':'", "'.'", "','", "';'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                      "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "AS", "ADD", 
                      "ADDF", "SUB", "SUBF", "MUL", "MULF", "DIV", "DIVF", 
                      "MOD", "NOT", "AND", "OR", "EQ", "NEQ", "LT", "GT", 
                      "LTE", "GTE", "LTF", "GTF", "LTEF", "GTEF", "LP", 
                      "RP", "LR", "RR", "CL", "DOT", "CM", "SM", "LB", "RB", 
                      "INTLIT", "FLOATLIT", "STRINGLIT", "ID", "WS", "COMMENT", 
                      "UNCLOSE_STRING", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_vardeclare = 1
    RULE_idlistinit = 2
    RULE_idinit = 3
    RULE_iddimen = 4
    RULE_dimension = 5
    RULE_funcdeclare = 6
    RULE_paralist = 7
    RULE_body = 8
    RULE_stmt = 9
    RULE_stmt_list = 10
    RULE_assign_stmt = 11
    RULE_if_stmt = 12
    RULE_if_part = 13
    RULE_elseif_part = 14
    RULE_else_part = 15
    RULE_for_stmt = 16
    RULE_for_loop_con = 17
    RULE_while_stmt = 18
    RULE_do_stmt = 19
    RULE_break_stmt = 20
    RULE_continue_stmt = 21
    RULE_call_stmt = 22
    RULE_return_stmt = 23
    RULE_exp = 24
    RULE_exp1 = 25
    RULE_exp11 = 26
    RULE_exp12 = 27
    RULE_exp2 = 28
    RULE_exp3 = 29
    RULE_exp4 = 30
    RULE_call = 31
    RULE_operands = 32
    RULE_variable = 33
    RULE_index_op = 34
    RULE_relational = 35
    RULE_logical = 36
    RULE_adding = 37
    RULE_multiplying = 38
    RULE_arraylit = 39
    RULE_primitive = 40
    RULE_lit = 41
    RULE_boollit = 42

    ruleNames =  [ "program", "vardeclare", "idlistinit", "idinit", "iddimen", 
                   "dimension", "funcdeclare", "paralist", "body", "stmt", 
                   "stmt_list", "assign_stmt", "if_stmt", "if_part", "elseif_part", 
                   "else_part", "for_stmt", "for_loop_con", "while_stmt", 
                   "do_stmt", "break_stmt", "continue_stmt", "call_stmt", 
                   "return_stmt", "exp", "exp1", "exp11", "exp12", "exp2", 
                   "exp3", "exp4", "call", "operands", "variable", "index_op", 
                   "relational", "logical", "adding", "multiplying", "arraylit", 
                   "primitive", "lit", "boollit" ]

    EOF = Token.EOF
    BODY=1
    BREAK=2
    CONTINUE=3
    DO=4
    ELSE=5
    ELSEIF=6
    ENDBODY=7
    ENDIF=8
    ENDFOR=9
    ENDWHILE=10
    FOR=11
    FUNCTION=12
    IF=13
    PARAMETER=14
    RETURN=15
    THEN=16
    VAR=17
    WHILE=18
    TRUE=19
    FALSE=20
    ENDDO=21
    AS=22
    ADD=23
    ADDF=24
    SUB=25
    SUBF=26
    MUL=27
    MULF=28
    DIV=29
    DIVF=30
    MOD=31
    NOT=32
    AND=33
    OR=34
    EQ=35
    NEQ=36
    LT=37
    GT=38
    LTE=39
    GTE=40
    LTF=41
    GTF=42
    LTEF=43
    GTEF=44
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
    STRINGLIT=57
    ID=58
    WS=59
    COMMENT=60
    UNCLOSE_STRING=61
    ERROR_CHAR=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def vardeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VardeclareContext)
            else:
                return self.getTypedRuleContext(BKITParser.VardeclareContext,i)


        def funcdeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.FuncdeclareContext)
            else:
                return self.getTypedRuleContext(BKITParser.FuncdeclareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 86
                self.vardeclare()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 92
                self.funcdeclare()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def CL(self):
            return self.getToken(BKITParser.CL, 0)

        def idlistinit(self):
            return self.getTypedRuleContext(BKITParser.IdlistinitContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_vardeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclare" ):
                return visitor.visitVardeclare(self)
            else:
                return visitor.visitChildren(self)




    def vardeclare(self):

        localctx = BKITParser.VardeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardeclare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(BKITParser.VAR)
            self.state = 101
            self.match(BKITParser.CL)
            self.state = 102
            self.idlistinit()
            self.state = 103
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistinitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idinit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.IdinitContext)
            else:
                return self.getTypedRuleContext(BKITParser.IdinitContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_idlistinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlistinit" ):
                return visitor.visitIdlistinit(self)
            else:
                return visitor.visitChildren(self)




    def idlistinit(self):

        localctx = BKITParser.IdlistinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_idlistinit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.idinit()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 106
                self.match(BKITParser.CM)
                self.state = 107
                self.idinit()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdinitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iddimen(self):
            return self.getTypedRuleContext(BKITParser.IddimenContext,0)


        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def lit(self):
            return self.getTypedRuleContext(BKITParser.LitContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_idinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdinit" ):
                return visitor.visitIdinit(self)
            else:
                return visitor.visitChildren(self)




    def idinit(self):

        localctx = BKITParser.IdinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_idinit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.iddimen()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.AS:
                self.state = 114
                self.match(BKITParser.AS)
                self.state = 115
                self.lit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IddimenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_iddimen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIddimen" ):
                return visitor.visitIddimen(self)
            else:
                return visitor.visitChildren(self)




    def iddimen(self):

        localctx = BKITParser.IddimenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_iddimen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(BKITParser.ID)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.LR:
                self.state = 119
                self.dimension()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR(self):
            return self.getToken(BKITParser.LR, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RR(self):
            return self.getToken(BKITParser.RR, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = BKITParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dimension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(BKITParser.LR)
            self.state = 123
            self.match(BKITParser.INTLIT)
            self.state = 124
            self.match(BKITParser.RR)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.LR:
                self.state = 125
                self.dimension()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def CL(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CL)
            else:
                return self.getToken(BKITParser.CL, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def paralist(self):
            return self.getTypedRuleContext(BKITParser.ParalistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_funcdeclare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdeclare" ):
                return visitor.visitFuncdeclare(self)
            else:
                return visitor.visitChildren(self)




    def funcdeclare(self):

        localctx = BKITParser.FuncdeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(BKITParser.FUNCTION)
            self.state = 129
            self.match(BKITParser.CL)
            self.state = 130
            self.match(BKITParser.ID)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 131
                self.match(BKITParser.PARAMETER)
                self.state = 132
                self.match(BKITParser.CL)
                self.state = 133
                self.paralist()


            self.state = 136
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iddimen(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.IddimenContext)
            else:
                return self.getTypedRuleContext(BKITParser.IddimenContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = BKITParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.iddimen()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 139
                self.match(BKITParser.CM)
                self.state = 140
                self.iddimen()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def CL(self):
            return self.getToken(BKITParser.CL, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def vardeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VardeclareContext)
            else:
                return self.getTypedRuleContext(BKITParser.VardeclareContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(BKITParser.BODY)
            self.state = 147
            self.match(BKITParser.CL)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 148
                self.vardeclare()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 154
                self.stmt()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(BKITParser.ENDBODY)
            self.state = 161
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def do_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmt)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.call_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.continue_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.do_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 168
                self.for_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 169
                self.if_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 170
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 171
                self.while_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VardeclareContext)
            else:
                return self.getTypedRuleContext(BKITParser.VardeclareContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 174
                self.vardeclare()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 180
                    self.stmt() 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.variable()
            self.state = 187
            self.match(BKITParser.AS)
            self.state = 188
            self.exp()
            self.state = 189
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_part(self):
            return self.getTypedRuleContext(BKITParser.If_partContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def elseif_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Elseif_partContext)
            else:
                return self.getTypedRuleContext(BKITParser.Elseif_partContext,i)


        def else_part(self):
            return self.getTypedRuleContext(BKITParser.Else_partContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.if_part()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 192
                self.elseif_part()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 198
                self.else_part()


            self.state = 201
            self.match(BKITParser.ENDIF)
            self.state = 202
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_part" ):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)




    def if_part(self):

        localctx = BKITParser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BKITParser.IF)
            self.state = 205
            self.exp()
            self.state = 206
            self.match(BKITParser.THEN)
            self.state = 207
            self.stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_part" ):
                return visitor.visitElseif_part(self)
            else:
                return visitor.visitChildren(self)




    def elseif_part(self):

        localctx = BKITParser.Elseif_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_elseif_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(BKITParser.ELSEIF)
            self.state = 210
            self.exp()
            self.state = 211
            self.match(BKITParser.THEN)
            self.state = 212
            self.stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = BKITParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(BKITParser.ELSE)
            self.state = 215
            self.stmt_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def for_loop_con(self):
            return self.getTypedRuleContext(BKITParser.For_loop_conContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(BKITParser.FOR)
            self.state = 218
            self.match(BKITParser.LP)
            self.state = 219
            self.for_loop_con()
            self.state = 220
            self.match(BKITParser.RP)
            self.state = 221
            self.match(BKITParser.DO)
            self.state = 222
            self.stmt_list()
            self.state = 223
            self.match(BKITParser.ENDFOR)
            self.state = 224
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_conContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def AS(self):
            return self.getToken(BKITParser.AS, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_loop_con

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_con" ):
                return visitor.visitFor_loop_con(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_con(self):

        localctx = BKITParser.For_loop_conContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_loop_con)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(BKITParser.ID)
            self.state = 227
            self.match(BKITParser.AS)
            self.state = 228
            self.exp()
            self.state = 229
            self.match(BKITParser.CM)
            self.state = 230
            self.exp()
            self.state = 231
            self.match(BKITParser.CM)
            self.state = 232
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BKITParser.WHILE)
            self.state = 235
            self.exp()
            self.state = 236
            self.match(BKITParser.DO)
            self.state = 237
            self.stmt_list()
            self.state = 238
            self.match(BKITParser.ENDWHILE)
            self.state = 239
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_stmt" ):
                return visitor.visitDo_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_stmt(self):

        localctx = BKITParser.Do_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_do_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(BKITParser.DO)
            self.state = 242
            self.stmt_list()
            self.state = 243
            self.match(BKITParser.WHILE)
            self.state = 244
            self.exp()
            self.state = 245
            self.match(BKITParser.ENDDO)
            self.state = 246
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(BKITParser.BREAK)
            self.state = 249
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(BKITParser.CONTINUE)
            self.state = 252
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BKITParser.ID)
            self.state = 255
            self.match(BKITParser.LP)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ID))) != 0):
                self.state = 256
                self.exp()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 257
                    self.match(BKITParser.CM)
                    self.state = 258
                    self.exp()
                    self.state = 263
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 266
            self.match(BKITParser.RP)
            self.state = 267
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(BKITParser.RETURN)
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ID))) != 0):
                self.state = 270
                self.exp()


            self.state = 273
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def relational(self):
            return self.getTypedRuleContext(BKITParser.RelationalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.exp1(0)
                self.state = 276
                self.relational()
                self.state = 277
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp11(self):
            return self.getTypedRuleContext(BKITParser.Exp11Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def logical(self):
            return self.getTypedRuleContext(BKITParser.LogicalContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.exp11(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 285
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 286
                    self.logical()
                    self.state = 287
                    self.exp11(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp12(self):
            return self.getTypedRuleContext(BKITParser.Exp12Context,0)


        def exp11(self):
            return self.getTypedRuleContext(BKITParser.Exp11Context,0)


        def adding(self):
            return self.getTypedRuleContext(BKITParser.AddingContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)



    def exp11(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp11Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp11, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.exp12(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 303
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp11Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp11)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    self.adding()
                    self.state = 299
                    self.exp12(0) 
                self.state = 305
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp12Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp12(self):
            return self.getTypedRuleContext(BKITParser.Exp12Context,0)


        def multiplying(self):
            return self.getTypedRuleContext(BKITParser.MultiplyingContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp12" ):
                return visitor.visitExp12(self)
            else:
                return visitor.visitChildren(self)



    def exp12(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp12Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp12, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.exp2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp12Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp12)
                    self.state = 309
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    self.multiplying()
                    self.state = 311
                    self.exp2() 
                self.state = 317
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)




    def exp2(self):

        localctx = BKITParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 319
                self.exp2()
                pass
            elif token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(BKITParser.NOT)
                self.state = 321
                self.exp2()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT, BKITParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.exp3(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 328
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 329
                    self.index_op() 
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp4)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = BKITParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(BKITParser.ID)
            self.state = 340
            self.match(BKITParser.LP)
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ID))) != 0):
                self.state = 341
                self.exp()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 342
                    self.match(BKITParser.CM)
                    self.state = 343
                    self.exp()
                    self.state = 348
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 351
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lit(self):
            return self.getTypedRuleContext(BKITParser.LitContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operands)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.lit()
                pass
            elif token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(BKITParser.LP)
                self.state = 355
                self.exp()
                self.state = 356
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.match(BKITParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_variable)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 362
                    self.match(BKITParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 363
                    self.call()
                    pass


                self.state = 366
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR(self):
            return self.getToken(BKITParser.LR, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RR(self):
            return self.getToken(BKITParser.RR, 0)

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = BKITParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(BKITParser.LR)
            self.state = 370
            self.exp()
            self.state = 371
            self.match(BKITParser.RR)
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 372
                self.index_op()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKITParser.NEQ, 0)

        def LT(self):
            return self.getToken(BKITParser.LT, 0)

        def GT(self):
            return self.getToken(BKITParser.GT, 0)

        def LTE(self):
            return self.getToken(BKITParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKITParser.GTE, 0)

        def LTF(self):
            return self.getToken(BKITParser.LTF, 0)

        def GTF(self):
            return self.getToken(BKITParser.GTF, 0)

        def LTEF(self):
            return self.getToken(BKITParser.LTEF, 0)

        def GTEF(self):
            return self.getToken(BKITParser.GTEF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = BKITParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQ) | (1 << BKITParser.NEQ) | (1 << BKITParser.LT) | (1 << BKITParser.GT) | (1 << BKITParser.LTE) | (1 << BKITParser.GTE) | (1 << BKITParser.LTF) | (1 << BKITParser.GTF) | (1 << BKITParser.LTEF) | (1 << BKITParser.GTEF))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)




    def logical(self):

        localctx = BKITParser.LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            _la = self._input.LA(1)
            if not(_la==BKITParser.AND or _la==BKITParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADDF(self):
            return self.getToken(BKITParser.ADDF, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding" ):
                return visitor.visitAdding(self)
            else:
                return visitor.visitChildren(self)




    def adding(self):

        localctx = BKITParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.ADDF) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def MULF(self):
            return self.getToken(BKITParser.MULF, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIVF(self):
            return self.getToken(BKITParser.DIVF, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying" ):
                return visitor.visitMultiplying(self)
            else:
                return visitor.visitChildren(self)




    def multiplying(self):

        localctx = BKITParser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.MULF) | (1 << BKITParser.DIV) | (1 << BKITParser.DIVF) | (1 << BKITParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LitContext)
            else:
                return self.getTypedRuleContext(BKITParser.LitContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = BKITParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(BKITParser.LB)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 384
                self.lit()
                self.state = 389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 385
                    self.match(BKITParser.CM)
                    self.state = 386
                    self.lit()
                    self.state = 391
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 394
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def boollit(self):
            return self.getTypedRuleContext(BKITParser.BoollitContext,0)


        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive" ):
                return visitor.visitPrimitive(self)
            else:
                return visitor.visitChildren(self)




    def primitive(self):

        localctx = BKITParser.PrimitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_primitive)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 398
                self.boollit()
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 399
                self.match(BKITParser.STRINGLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive(self):
            return self.getTypedRuleContext(BKITParser.PrimitiveContext,0)


        def arraylit(self):
            return self.getTypedRuleContext(BKITParser.ArraylitContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)




    def lit(self):

        localctx = BKITParser.LitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_lit)
        try:
            self.state = 404
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.primitive()
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.arraylit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoollitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boollit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoollit" ):
                return visitor.visitBoollit(self)
            else:
                return visitor.visitChildren(self)




    def boollit(self):

        localctx = BKITParser.BoollitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            _la = self._input.LA(1)
            if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.exp1_sempred
        self._predicates[26] = self.exp11_sempred
        self._predicates[27] = self.exp12_sempred
        self._predicates[29] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp11_sempred(self, localctx:Exp11Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp12_sempred(self, localctx:Exp12Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




