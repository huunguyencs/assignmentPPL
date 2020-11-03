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
        buf.write("\u0185\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\7\2T\n\2\f\2\16\2W\13\2\3\2")
        buf.write("\7\2Z\n\2\f\2\16\2]\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\7\4i\n\4\f\4\16\4l\13\4\3\5\3\5\5\5p\n\5\3")
        buf.write("\5\3\5\5\5t\n\5\3\6\3\6\3\6\3\6\5\6z\n\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u0082\n\7\3\7\3\7\3\b\3\b\5\b\u0088\n\b")
        buf.write("\3\b\3\b\3\b\5\b\u008d\n\b\7\b\u008f\n\b\f\b\16\b\u0092")
        buf.write("\13\b\3\t\3\t\3\t\7\t\u0097\n\t\f\t\16\t\u009a\13\t\3")
        buf.write("\t\7\t\u009d\n\t\f\t\16\t\u00a0\13\t\3\t\3\t\3\t\3\n\7")
        buf.write("\n\u00a6\n\n\f\n\16\n\u00a9\13\n\3\n\7\n\u00ac\n\n\f\n")
        buf.write("\16\n\u00af\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00ba\n\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00ca\n\r\f\r\16\r\u00cd")
        buf.write("\13\r\3\r\3\r\5\r\u00d1\n\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\5\25\u0100\n\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\5\26\u0109\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\7\27\u0112\n\27\f\27\16\27\u0115")
        buf.write("\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u011e\n")
        buf.write("\30\f\30\16\30\u0121\13\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\7\31\u012a\n\31\f\31\16\31\u012d\13\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u0134\n\32\3\33\3\33\5\33\u0138")
        buf.write("\n\33\3\34\3\34\5\34\u013c\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\7\35\u0143\n\35\f\35\16\35\u0146\13\35\5\35\u0148")
        buf.write("\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0152")
        buf.write("\n\36\3\37\3\37\5\37\u0156\n\37\3 \3 \5 \u015a\n \3 \3")
        buf.write(" \3!\3!\3!\3!\5!\u0162\n!\3\"\3\"\3#\3#\3$\3$\3%\3%\3")
        buf.write("&\3&\3&\3&\7&\u0170\n&\f&\16&\u0173\13&\5&\u0175\n&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\5\'\u017d\n\'\3(\3(\5(\u0181\n(\3")
        buf.write(")\3)\3)\2\5,.\60*\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNP\2\b\3\2\33\34\3")
        buf.write("\2%.\3\2#$\3\2\31\34\3\2\35!\3\2\25\26\2\u018a\2U\3\2")
        buf.write("\2\2\4`\3\2\2\2\6e\3\2\2\2\bm\3\2\2\2\nu\3\2\2\2\f{\3")
        buf.write("\2\2\2\16\u0085\3\2\2\2\20\u0093\3\2\2\2\22\u00a7\3\2")
        buf.write("\2\2\24\u00b9\3\2\2\2\26\u00bb\3\2\2\2\30\u00c0\3\2\2")
        buf.write("\2\32\u00d5\3\2\2\2\34\u00de\3\2\2\2\36\u00e6\3\2\2\2")
        buf.write(" \u00ed\3\2\2\2\"\u00f4\3\2\2\2$\u00f7\3\2\2\2&\u00fa")
        buf.write("\3\2\2\2(\u00fd\3\2\2\2*\u0108\3\2\2\2,\u010a\3\2\2\2")
        buf.write(".\u0116\3\2\2\2\60\u0122\3\2\2\2\62\u0133\3\2\2\2\64\u0137")
        buf.write("\3\2\2\2\66\u013b\3\2\2\28\u013d\3\2\2\2:\u0151\3\2\2")
        buf.write("\2<\u0155\3\2\2\2>\u0159\3\2\2\2@\u015d\3\2\2\2B\u0163")
        buf.write("\3\2\2\2D\u0165\3\2\2\2F\u0167\3\2\2\2H\u0169\3\2\2\2")
        buf.write("J\u016b\3\2\2\2L\u017c\3\2\2\2N\u0180\3\2\2\2P\u0182\3")
        buf.write("\2\2\2RT\5\4\3\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2")
        buf.write("\2V[\3\2\2\2WU\3\2\2\2XZ\5\f\7\2YX\3\2\2\2Z]\3\2\2\2[")
        buf.write("Y\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2][\3\2\2\2^_\7\2\2\3_\3")
        buf.write("\3\2\2\2`a\7\23\2\2ab\7\63\2\2bc\5\6\4\2cd\7\66\2\2d\5")
        buf.write("\3\2\2\2ej\5\b\5\2fg\7\65\2\2gi\5\b\5\2hf\3\2\2\2il\3")
        buf.write("\2\2\2jh\3\2\2\2jk\3\2\2\2k\7\3\2\2\2lj\3\2\2\2mo\7<\2")
        buf.write("\2np\5\n\6\2on\3\2\2\2op\3\2\2\2ps\3\2\2\2qr\7\30\2\2")
        buf.write("rt\5N(\2sq\3\2\2\2st\3\2\2\2t\t\3\2\2\2uv\7\61\2\2vw\7")
        buf.write("9\2\2wy\7\62\2\2xz\5\n\6\2yx\3\2\2\2yz\3\2\2\2z\13\3\2")
        buf.write("\2\2{|\7\16\2\2|}\7\63\2\2}\u0081\7<\2\2~\177\7\20\2\2")
        buf.write("\177\u0080\7\63\2\2\u0080\u0082\5\16\b\2\u0081~\3\2\2")
        buf.write("\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\5\20\t\2\u0084\r\3\2\2\2\u0085\u0087\7<\2\2\u0086\u0088")
        buf.write("\5\n\6\2\u0087\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\u0090\3\2\2\2\u0089\u008a\7\65\2\2\u008a\u008c\7<\2\2")
        buf.write("\u008b\u008d\5\n\6\2\u008c\u008b\3\2\2\2\u008c\u008d\3")
        buf.write("\2\2\2\u008d\u008f\3\2\2\2\u008e\u0089\3\2\2\2\u008f\u0092")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\17\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\7\3\2\2\u0094")
        buf.write("\u0098\7\63\2\2\u0095\u0097\5\4\3\2\u0096\u0095\3\2\2")
        buf.write("\2\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u009e\3\2\2\2\u009a\u0098\3\2\2\2\u009b")
        buf.write("\u009d\5\24\13\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2")
        buf.write("\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1")
        buf.write("\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2\7\t\2\2\u00a2")
        buf.write("\u00a3\7\64\2\2\u00a3\21\3\2\2\2\u00a4\u00a6\5\4\3\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\u00ad\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00aa\u00ac\5\24\13\2\u00ab\u00aa\3\2\2\2\u00ac")
        buf.write("\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2")
        buf.write("\u00ae\23\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00ba\5\26")
        buf.write("\f\2\u00b1\u00ba\5\"\22\2\u00b2\u00ba\5&\24\2\u00b3\u00ba")
        buf.write("\5$\23\2\u00b4\u00ba\5 \21\2\u00b5\u00ba\5\32\16\2\u00b6")
        buf.write("\u00ba\5\30\r\2\u00b7\u00ba\5(\25\2\u00b8\u00ba\5\36\20")
        buf.write("\2\u00b9\u00b0\3\2\2\2\u00b9\u00b1\3\2\2\2\u00b9\u00b2")
        buf.write("\3\2\2\2\u00b9\u00b3\3\2\2\2\u00b9\u00b4\3\2\2\2\u00b9")
        buf.write("\u00b5\3\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00b9\u00b8\3\2\2\2\u00ba\25\3\2\2\2\u00bb\u00bc\5<\37")
        buf.write("\2\u00bc\u00bd\7\30\2\2\u00bd\u00be\5*\26\2\u00be\u00bf")
        buf.write("\7\66\2\2\u00bf\27\3\2\2\2\u00c0\u00c1\7\17\2\2\u00c1")
        buf.write("\u00c2\5*\26\2\u00c2\u00c3\7\22\2\2\u00c3\u00cb\5\22\n")
        buf.write("\2\u00c4\u00c5\7\b\2\2\u00c5\u00c6\5*\26\2\u00c6\u00c7")
        buf.write("\7\22\2\2\u00c7\u00c8\5\22\n\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c4\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00d0\3\2\2\2\u00cd\u00cb\3")
        buf.write("\2\2\2\u00ce\u00cf\7\7\2\2\u00cf\u00d1\5\22\n\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d3\7\n\2\2\u00d3\u00d4\7\64\2\2\u00d4\31\3\2")
        buf.write("\2\2\u00d5\u00d6\7\r\2\2\u00d6\u00d7\7/\2\2\u00d7\u00d8")
        buf.write("\5\34\17\2\u00d8\u00d9\7\60\2\2\u00d9\u00da\7\6\2\2\u00da")
        buf.write("\u00db\5\22\n\2\u00db\u00dc\7\13\2\2\u00dc\u00dd\7\64")
        buf.write("\2\2\u00dd\33\3\2\2\2\u00de\u00df\7<\2\2\u00df\u00e0\7")
        buf.write("\30\2\2\u00e0\u00e1\5*\26\2\u00e1\u00e2\7\65\2\2\u00e2")
        buf.write("\u00e3\5*\26\2\u00e3\u00e4\7\65\2\2\u00e4\u00e5\5*\26")
        buf.write("\2\u00e5\35\3\2\2\2\u00e6\u00e7\7\24\2\2\u00e7\u00e8\5")
        buf.write("*\26\2\u00e8\u00e9\7\6\2\2\u00e9\u00ea\5\22\n\2\u00ea")
        buf.write("\u00eb\7\f\2\2\u00eb\u00ec\7\64\2\2\u00ec\37\3\2\2\2\u00ed")
        buf.write("\u00ee\7\6\2\2\u00ee\u00ef\5\22\n\2\u00ef\u00f0\7\24\2")
        buf.write("\2\u00f0\u00f1\5*\26\2\u00f1\u00f2\7\27\2\2\u00f2\u00f3")
        buf.write("\7\64\2\2\u00f3!\3\2\2\2\u00f4\u00f5\7\4\2\2\u00f5\u00f6")
        buf.write("\7\66\2\2\u00f6#\3\2\2\2\u00f7\u00f8\7\5\2\2\u00f8\u00f9")
        buf.write("\7\66\2\2\u00f9%\3\2\2\2\u00fa\u00fb\58\35\2\u00fb\u00fc")
        buf.write("\7\66\2\2\u00fc\'\3\2\2\2\u00fd\u00ff\7\21\2\2\u00fe\u0100")
        buf.write("\5*\26\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0101\u0102\7\66\2\2\u0102)\3\2\2\2\u0103")
        buf.write("\u0104\5,\27\2\u0104\u0105\5B\"\2\u0105\u0106\5,\27\2")
        buf.write("\u0106\u0109\3\2\2\2\u0107\u0109\5,\27\2\u0108\u0103\3")
        buf.write("\2\2\2\u0108\u0107\3\2\2\2\u0109+\3\2\2\2\u010a\u010b")
        buf.write("\b\27\1\2\u010b\u010c\5.\30\2\u010c\u0113\3\2\2\2\u010d")
        buf.write("\u010e\f\4\2\2\u010e\u010f\5D#\2\u010f\u0110\5.\30\2\u0110")
        buf.write("\u0112\3\2\2\2\u0111\u010d\3\2\2\2\u0112\u0115\3\2\2\2")
        buf.write("\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114-\3\2\2")
        buf.write("\2\u0115\u0113\3\2\2\2\u0116\u0117\b\30\1\2\u0117\u0118")
        buf.write("\5\60\31\2\u0118\u011f\3\2\2\2\u0119\u011a\f\4\2\2\u011a")
        buf.write("\u011b\5F$\2\u011b\u011c\5\60\31\2\u011c\u011e\3\2\2\2")
        buf.write("\u011d\u0119\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d\3")
        buf.write("\2\2\2\u011f\u0120\3\2\2\2\u0120/\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0122\u0123\b\31\1\2\u0123\u0124\5\62\32\2\u0124")
        buf.write("\u012b\3\2\2\2\u0125\u0126\f\4\2\2\u0126\u0127\5H%\2\u0127")
        buf.write("\u0128\5\62\32\2\u0128\u012a\3\2\2\2\u0129\u0125\3\2\2")
        buf.write("\2\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c")
        buf.write("\3\2\2\2\u012c\61\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f")
        buf.write("\7\"\2\2\u012f\u0134\5\62\32\2\u0130\u0131\t\2\2\2\u0131")
        buf.write("\u0134\5\62\32\2\u0132\u0134\5\64\33\2\u0133\u012e\3\2")
        buf.write("\2\2\u0133\u0130\3\2\2\2\u0133\u0132\3\2\2\2\u0134\63")
        buf.write("\3\2\2\2\u0135\u0138\5> \2\u0136\u0138\5\66\34\2\u0137")
        buf.write("\u0135\3\2\2\2\u0137\u0136\3\2\2\2\u0138\65\3\2\2\2\u0139")
        buf.write("\u013c\58\35\2\u013a\u013c\5:\36\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013a\3\2\2\2\u013c\67\3\2\2\2\u013d\u013e\7<\2")
        buf.write("\2\u013e\u0147\7/\2\2\u013f\u0144\5*\26\2\u0140\u0141")
        buf.write("\7\65\2\2\u0141\u0143\5*\26\2\u0142\u0140\3\2\2\2\u0143")
        buf.write("\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u013f\3")
        buf.write("\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a")
        buf.write("\7\60\2\2\u014a9\3\2\2\2\u014b\u0152\5N(\2\u014c\u014d")
        buf.write("\7/\2\2\u014d\u014e\5*\26\2\u014e\u014f\7\60\2\2\u014f")
        buf.write("\u0152\3\2\2\2\u0150\u0152\7<\2\2\u0151\u014b\3\2\2\2")
        buf.write("\u0151\u014c\3\2\2\2\u0151\u0150\3\2\2\2\u0152;\3\2\2")
        buf.write("\2\u0153\u0156\7<\2\2\u0154\u0156\5> \2\u0155\u0153\3")
        buf.write("\2\2\2\u0155\u0154\3\2\2\2\u0156=\3\2\2\2\u0157\u015a")
        buf.write("\58\35\2\u0158\u015a\7<\2\2\u0159\u0157\3\2\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\5@!\2\u015c")
        buf.write("?\3\2\2\2\u015d\u015e\7\61\2\2\u015e\u015f\5*\26\2\u015f")
        buf.write("\u0161\7\62\2\2\u0160\u0162\5@!\2\u0161\u0160\3\2\2\2")
        buf.write("\u0161\u0162\3\2\2\2\u0162A\3\2\2\2\u0163\u0164\t\3\2")
        buf.write("\2\u0164C\3\2\2\2\u0165\u0166\t\4\2\2\u0166E\3\2\2\2\u0167")
        buf.write("\u0168\t\5\2\2\u0168G\3\2\2\2\u0169\u016a\t\6\2\2\u016a")
        buf.write("I\3\2\2\2\u016b\u0174\7\67\2\2\u016c\u0171\5N(\2\u016d")
        buf.write("\u016e\7\65\2\2\u016e\u0170\5N(\2\u016f\u016d\3\2\2\2")
        buf.write("\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u016c")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176")
        buf.write("\u0177\78\2\2\u0177K\3\2\2\2\u0178\u017d\79\2\2\u0179")
        buf.write("\u017d\7:\2\2\u017a\u017d\5P)\2\u017b\u017d\7;\2\2\u017c")
        buf.write("\u0178\3\2\2\2\u017c\u0179\3\2\2\2\u017c\u017a\3\2\2\2")
        buf.write("\u017c\u017b\3\2\2\2\u017dM\3\2\2\2\u017e\u0181\5L\'\2")
        buf.write("\u017f\u0181\5J&\2\u0180\u017e\3\2\2\2\u0180\u017f\3\2")
        buf.write("\2\2\u0181O\3\2\2\2\u0182\u0183\t\7\2\2\u0183Q\3\2\2\2")
        buf.write("%U[josy\u0081\u0087\u008c\u0090\u0098\u009e\u00a7\u00ad")
        buf.write("\u00b9\u00cb\u00d0\u00ff\u0108\u0113\u011f\u012b\u0133")
        buf.write("\u0137\u013b\u0144\u0147\u0151\u0155\u0159\u0161\u0171")
        buf.write("\u0174\u017c\u0180")
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
    RULE_dimension = 4
    RULE_funcdeclare = 5
    RULE_paralist = 6
    RULE_body = 7
    RULE_stmt_list = 8
    RULE_stmt = 9
    RULE_stmt_assign = 10
    RULE_stmt_if = 11
    RULE_stmt_for = 12
    RULE_for_loop_con = 13
    RULE_stmt_while = 14
    RULE_stmt_do = 15
    RULE_stmt_break = 16
    RULE_stmt_con = 17
    RULE_stmt_call = 18
    RULE_stmt_ret = 19
    RULE_exp = 20
    RULE_exp1 = 21
    RULE_exp11 = 22
    RULE_exp12 = 23
    RULE_exp2 = 24
    RULE_exp3 = 25
    RULE_exp4 = 26
    RULE_call = 27
    RULE_operands = 28
    RULE_variable = 29
    RULE_ele_exp = 30
    RULE_index_op = 31
    RULE_relational = 32
    RULE_logical = 33
    RULE_adding = 34
    RULE_multiplying = 35
    RULE_arraylit = 36
    RULE_primitive = 37
    RULE_lit = 38
    RULE_boollit = 39

    ruleNames =  [ "program", "vardeclare", "idlistinit", "idinit", "dimension", 
                   "funcdeclare", "paralist", "body", "stmt_list", "stmt", 
                   "stmt_assign", "stmt_if", "stmt_for", "for_loop_con", 
                   "stmt_while", "stmt_do", "stmt_break", "stmt_con", "stmt_call", 
                   "stmt_ret", "exp", "exp1", "exp11", "exp12", "exp2", 
                   "exp3", "exp4", "call", "operands", "variable", "ele_exp", 
                   "index_op", "relational", "logical", "adding", "multiplying", 
                   "arraylit", "primitive", "lit", "boollit" ]

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
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 80
                self.vardeclare()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 86
                self.funcdeclare()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
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
            self.state = 94
            self.match(BKITParser.VAR)
            self.state = 95
            self.match(BKITParser.CL)
            self.state = 96
            self.idlistinit()
            self.state = 97
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
            self.state = 99
            self.idinit()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 100
                self.match(BKITParser.CM)
                self.state = 101
                self.idinit()
                self.state = 106
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

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


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
            self.state = 107
            self.match(BKITParser.ID)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.LR:
                self.state = 108
                self.dimension()


            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.AS:
                self.state = 111
                self.match(BKITParser.AS)
                self.state = 112
                self.lit()


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
        self.enterRule(localctx, 8, self.RULE_dimension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(BKITParser.LR)
            self.state = 116
            self.match(BKITParser.INTLIT)
            self.state = 117
            self.match(BKITParser.RR)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.LR:
                self.state = 118
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
        self.enterRule(localctx, 10, self.RULE_funcdeclare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(BKITParser.FUNCTION)
            self.state = 122
            self.match(BKITParser.CL)
            self.state = 123
            self.match(BKITParser.ID)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 124
                self.match(BKITParser.PARAMETER)
                self.state = 125
                self.match(BKITParser.CL)
                self.state = 126
                self.paralist()


            self.state = 129
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def dimension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.DimensionContext)
            else:
                return self.getTypedRuleContext(BKITParser.DimensionContext,i)


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
        self.enterRule(localctx, 12, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(BKITParser.ID)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.LR:
                self.state = 132
                self.dimension()


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 135
                self.match(BKITParser.CM)
                self.state = 136
                self.match(BKITParser.ID)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.LR:
                    self.state = 137
                    self.dimension()


                self.state = 144
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
        self.enterRule(localctx, 14, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(BKITParser.BODY)
            self.state = 146
            self.match(BKITParser.CL)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 147
                self.vardeclare()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.ID))) != 0):
                self.state = 153
                self.stmt()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self.match(BKITParser.ENDBODY)
            self.state = 160
            self.match(BKITParser.DOT)
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
        self.enterRule(localctx, 16, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 162
                self.vardeclare()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 168
                    self.stmt() 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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

        def stmt_assign(self):
            return self.getTypedRuleContext(BKITParser.Stmt_assignContext,0)


        def stmt_break(self):
            return self.getTypedRuleContext(BKITParser.Stmt_breakContext,0)


        def stmt_call(self):
            return self.getTypedRuleContext(BKITParser.Stmt_callContext,0)


        def stmt_con(self):
            return self.getTypedRuleContext(BKITParser.Stmt_conContext,0)


        def stmt_do(self):
            return self.getTypedRuleContext(BKITParser.Stmt_doContext,0)


        def stmt_for(self):
            return self.getTypedRuleContext(BKITParser.Stmt_forContext,0)


        def stmt_if(self):
            return self.getTypedRuleContext(BKITParser.Stmt_ifContext,0)


        def stmt_ret(self):
            return self.getTypedRuleContext(BKITParser.Stmt_retContext,0)


        def stmt_while(self):
            return self.getTypedRuleContext(BKITParser.Stmt_whileContext,0)


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
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.stmt_assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.stmt_break()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.stmt_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
                self.stmt_con()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 178
                self.stmt_do()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 179
                self.stmt_for()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 180
                self.stmt_if()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 181
                self.stmt_ret()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 182
                self.stmt_while()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_assignContext(ParserRuleContext):

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
            return BKITParser.RULE_stmt_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assign" ):
                return visitor.visitStmt_assign(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assign(self):

        localctx = BKITParser.Stmt_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.variable()
            self.state = 186
            self.match(BKITParser.AS)
            self.state = 187
            self.exp()
            self.state = 188
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_stmt_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_if" ):
                return visitor.visitStmt_if(self)
            else:
                return visitor.visitChildren(self)




    def stmt_if(self):

        localctx = BKITParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stmt_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(BKITParser.IF)
            self.state = 191
            self.exp()
            self.state = 192
            self.match(BKITParser.THEN)
            self.state = 193
            self.stmt_list()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 194
                self.match(BKITParser.ELSEIF)
                self.state = 195
                self.exp()
                self.state = 196
                self.match(BKITParser.THEN)
                self.state = 197
                self.stmt_list()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 204
                self.match(BKITParser.ELSE)
                self.state = 205
                self.stmt_list()


            self.state = 208
            self.match(BKITParser.ENDIF)
            self.state = 209
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_forContext(ParserRuleContext):

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
            return BKITParser.RULE_stmt_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_for" ):
                return visitor.visitStmt_for(self)
            else:
                return visitor.visitChildren(self)




    def stmt_for(self):

        localctx = BKITParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(BKITParser.FOR)
            self.state = 212
            self.match(BKITParser.LP)
            self.state = 213
            self.for_loop_con()
            self.state = 214
            self.match(BKITParser.RP)
            self.state = 215
            self.match(BKITParser.DO)
            self.state = 216
            self.stmt_list()
            self.state = 217
            self.match(BKITParser.ENDFOR)
            self.state = 218
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
        self.enterRule(localctx, 26, self.RULE_for_loop_con)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BKITParser.ID)
            self.state = 221
            self.match(BKITParser.AS)
            self.state = 222
            self.exp()
            self.state = 223
            self.match(BKITParser.CM)
            self.state = 224
            self.exp()
            self.state = 225
            self.match(BKITParser.CM)
            self.state = 226
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_whileContext(ParserRuleContext):

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
            return BKITParser.RULE_stmt_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_while" ):
                return visitor.visitStmt_while(self)
            else:
                return visitor.visitChildren(self)




    def stmt_while(self):

        localctx = BKITParser.Stmt_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(BKITParser.WHILE)
            self.state = 229
            self.exp()
            self.state = 230
            self.match(BKITParser.DO)
            self.state = 231
            self.stmt_list()
            self.state = 232
            self.match(BKITParser.ENDWHILE)
            self.state = 233
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_doContext(ParserRuleContext):

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
            return BKITParser.RULE_stmt_do

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_do" ):
                return visitor.visitStmt_do(self)
            else:
                return visitor.visitChildren(self)




    def stmt_do(self):

        localctx = BKITParser.Stmt_doContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt_do)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(BKITParser.DO)
            self.state = 236
            self.stmt_list()
            self.state = 237
            self.match(BKITParser.WHILE)
            self.state = 238
            self.exp()
            self.state = 239
            self.match(BKITParser.ENDDO)
            self.state = 240
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_breakContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_stmt_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_break" ):
                return visitor.visitStmt_break(self)
            else:
                return visitor.visitChildren(self)




    def stmt_break(self):

        localctx = BKITParser.Stmt_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(BKITParser.BREAK)
            self.state = 243
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_conContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_stmt_con

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_con" ):
                return visitor.visitStmt_con(self)
            else:
                return visitor.visitChildren(self)




    def stmt_con(self):

        localctx = BKITParser.Stmt_conContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt_con)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(BKITParser.CONTINUE)
            self.state = 246
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_stmt_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_call" ):
                return visitor.visitStmt_call(self)
            else:
                return visitor.visitChildren(self)




    def stmt_call(self):

        localctx = BKITParser.Stmt_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.call()
            self.state = 249
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_retContext(ParserRuleContext):

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
            return BKITParser.RULE_stmt_ret

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_ret" ):
                return visitor.visitStmt_ret(self)
            else:
                return visitor.visitChildren(self)




    def stmt_ret(self):

        localctx = BKITParser.Stmt_retContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt_ret)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(BKITParser.RETURN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ID))) != 0):
                self.state = 252
                self.exp()


            self.state = 255
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
        self.enterRule(localctx, 40, self.RULE_exp)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.exp1(0)
                self.state = 258
                self.relational()
                self.state = 259
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.exp11(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 267
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 268
                    self.logical()
                    self.state = 269
                    self.exp11(0) 
                self.state = 275
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp11, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.exp12(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp11Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp11)
                    self.state = 279
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 280
                    self.adding()
                    self.state = 281
                    self.exp12(0) 
                self.state = 287
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp12, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.exp2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 297
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp12Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp12)
                    self.state = 291
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 292
                    self.multiplying()
                    self.state = 293
                    self.exp2() 
                self.state = 299
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

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBF(self):
            return self.getToken(BKITParser.SUBF, 0)

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
        self.enterRule(localctx, 48, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(BKITParser.NOT)
                self.state = 301
                self.exp2()
                pass
            elif token in [BKITParser.SUB, BKITParser.SUBF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBF):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 303
                self.exp2()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT, BKITParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.exp3()
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

        def ele_exp(self):
            return self.getTypedRuleContext(BKITParser.Ele_expContext,0)


        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = BKITParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp3)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.ele_exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 52, self.RULE_exp4)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
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
        self.enterRule(localctx, 54, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(BKITParser.ID)
            self.state = 316
            self.match(BKITParser.LP)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUBF) | (1 << BKITParser.NOT) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT) | (1 << BKITParser.ID))) != 0):
                self.state = 317
                self.exp()
                self.state = 322
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 318
                    self.match(BKITParser.CM)
                    self.state = 319
                    self.exp()
                    self.state = 324
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 327
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
        self.enterRule(localctx, 56, self.RULE_operands)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LB, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.lit()
                pass
            elif token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(BKITParser.LP)
                self.state = 331
                self.exp()
                self.state = 332
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
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

        def ele_exp(self):
            return self.getTypedRuleContext(BKITParser.Ele_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_variable)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.ele_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ele_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_ele_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEle_exp" ):
                return visitor.visitEle_exp(self)
            else:
                return visitor.visitChildren(self)




    def ele_exp(self):

        localctx = BKITParser.Ele_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ele_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 341
                self.call()
                pass

            elif la_ == 2:
                self.state = 342
                self.match(BKITParser.ID)
                pass


            self.state = 345
            self.index_op()
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
        self.enterRule(localctx, 62, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(BKITParser.LR)
            self.state = 348
            self.exp()
            self.state = 349
            self.match(BKITParser.RR)
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 350
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
        self.enterRule(localctx, 64, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
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
        self.enterRule(localctx, 66, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
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
        self.enterRule(localctx, 68, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
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
        self.enterRule(localctx, 70, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
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
        self.enterRule(localctx, 72, self.RULE_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(BKITParser.LB)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.LB) | (1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.STRINGLIT))) != 0):
                self.state = 362
                self.lit()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 363
                    self.match(BKITParser.CM)
                    self.state = 364
                    self.lit()
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 372
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
        self.enterRule(localctx, 74, self.RULE_primitive)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.boollit()
                pass
            elif token in [BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
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
        self.enterRule(localctx, 76, self.RULE_lit)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.primitive()
                pass
            elif token in [BKITParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
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
        self.enterRule(localctx, 78, self.RULE_boollit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
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
        self._predicates[21] = self.exp1_sempred
        self._predicates[22] = self.exp11_sempred
        self._predicates[23] = self.exp12_sempred
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
         




