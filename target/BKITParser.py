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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u01cc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\7\2h")
        buf.write("\n\2\f\2\16\2k\13\2\3\2\7\2n\n\2\f\2\16\2q\13\2\3\2\7")
        buf.write("\2t\n\2\f\2\16\2w\13\2\3\2\7\2z\n\2\f\2\16\2}\13\2\3\2")
        buf.write("\7\2\u0080\n\2\f\2\16\2\u0083\13\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\5\4\u008f\n\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\u0097\n\4\5\4\u0099\n\4\3\5\3\5\5\5\u009d\n\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00ab")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00b2\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u00b9\n\t\3\n\5\n\u00bc\n\n\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\5\f\u00c4\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00cd\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u00d6")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00e1\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\3\23\5\23\u00ed\n\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u00f8\n\24\3\25\5\25\u00fb\n\25\3")
        buf.write("\25\7\25\u00fe\n\25\f\25\16\25\u0101\13\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\5\27\u010d\n\27")
        buf.write("\3\27\3\27\5\27\u0111\n\27\3\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0121")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\5\37\u014b\n")
        buf.write("\37\3\37\3\37\3\37\3 \3 \5 \u0152\n \3 \3 \3!\3!\3!\5")
        buf.write("!\u0159\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u0162\n\"\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\7#\u016b\n#\f#\16#\u016e\13#\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\7$\u0177\n$\f$\16$\u017a\13$\3%\3%\3%")
        buf.write("\3%\3%\3%\3%\7%\u0183\n%\f%\16%\u0186\13%\3&\3&\3&\5&")
        buf.write("\u018b\n&\3\'\3\'\3\'\3\'\5\'\u0191\n\'\3(\3(\3(\3(\3")
        buf.write("(\7(\u0198\n(\f(\16(\u019b\13(\3)\3)\3)\3)\3)\3)\5)\u01a3")
        buf.write("\n)\3*\3*\3*\3*\3*\5*\u01aa\n*\3+\3+\5+\u01ae\n+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01c6\n\62\3")
        buf.write("\63\3\63\5\63\u01ca\n\63\3\63\2\6DFHN\64\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bd\2\t\3\2?A\3\2\26\27\3\2!%\3\2\35 \3\2")
        buf.write("\37 \3\2\'(\3\2)\63\2\u01cb\2i\3\2\2\2\4\u0086\3\2\2\2")
        buf.write("\6\u0098\3\2\2\2\b\u009c\3\2\2\2\n\u009e\3\2\2\2\f\u00aa")
        buf.write("\3\2\2\2\16\u00b1\3\2\2\2\20\u00b8\3\2\2\2\22\u00bb\3")
        buf.write("\2\2\2\24\u00bf\3\2\2\2\26\u00c1\3\2\2\2\30\u00cc\3\2")
        buf.write("\2\2\32\u00ce\3\2\2\2\34\u00d1\3\2\2\2\36\u00d7\3\2\2")
        buf.write("\2 \u00e0\3\2\2\2\"\u00e2\3\2\2\2$\u00ec\3\2\2\2&\u00f7")
        buf.write("\3\2\2\2(\u00fa\3\2\2\2*\u0102\3\2\2\2,\u0107\3\2\2\2")
        buf.write(".\u0120\3\2\2\2\60\u0122\3\2\2\2\62\u012b\3\2\2\2\64\u0133")
        buf.write("\3\2\2\2\66\u013a\3\2\2\28\u0141\3\2\2\2:\u0144\3\2\2")
        buf.write("\2<\u0147\3\2\2\2>\u014f\3\2\2\2@\u0155\3\2\2\2B\u0161")
        buf.write("\3\2\2\2D\u0163\3\2\2\2F\u016f\3\2\2\2H\u017b\3\2\2\2")
        buf.write("J\u018a\3\2\2\2L\u0190\3\2\2\2N\u0192\3\2\2\2P\u01a2\3")
        buf.write("\2\2\2R\u01a9\3\2\2\2T\u01ad\3\2\2\2V\u01af\3\2\2\2X\u01b1")
        buf.write("\3\2\2\2Z\u01b3\3\2\2\2\\\u01b5\3\2\2\2^\u01b7\3\2\2\2")
        buf.write("`\u01b9\3\2\2\2b\u01c5\3\2\2\2d\u01c9\3\2\2\2fh\7E\2\2")
        buf.write("gf\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2jo\3\2\2\2ki\3")
        buf.write("\2\2\2ln\5\4\3\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2")
        buf.write("\2pu\3\2\2\2qo\3\2\2\2rt\7E\2\2sr\3\2\2\2tw\3\2\2\2us")
        buf.write("\3\2\2\2uv\3\2\2\2v{\3\2\2\2wu\3\2\2\2xz\5\32\16\2yx\3")
        buf.write("\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\u0081\3\2\2\2}{")
        buf.write("\3\2\2\2~\u0080\7E\2\2\177~\3\2\2\2\u0080\u0083\3\2\2")
        buf.write("\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3")
        buf.write("\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\7\2\2\3\u0085\3")
        buf.write("\3\2\2\2\u0086\u0087\7\4\2\2\u0087\u0088\7\65\2\2\u0088")
        buf.write("\u0089\5\6\4\2\u0089\u008a\7\64\2\2\u008a\5\3\2\2\2\u008b")
        buf.write("\u008e\5\b\5\2\u008c\u008d\7>\2\2\u008d\u008f\5\16\b\2")
        buf.write("\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\3")
        buf.write("\2\2\2\u0090\u0091\7\67\2\2\u0091\u0092\5\6\4\2\u0092")
        buf.write("\u0099\3\2\2\2\u0093\u0096\5\b\5\2\u0094\u0095\7>\2\2")
        buf.write("\u0095\u0097\5\16\b\2\u0096\u0094\3\2\2\2\u0096\u0097")
        buf.write("\3\2\2\2\u0097\u0099\3\2\2\2\u0098\u008b\3\2\2\2\u0098")
        buf.write("\u0093\3\2\2\2\u0099\7\3\2\2\2\u009a\u009d\7\3\2\2\u009b")
        buf.write("\u009d\5\n\6\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\t\3\2\2\2\u009e\u009f\7\3\2\2\u009f\u00a0\5\f\7")
        buf.write("\2\u00a0\13\3\2\2\2\u00a1\u00a2\7:\2\2\u00a2\u00a3\5\22")
        buf.write("\n\2\u00a3\u00a4\7;\2\2\u00a4\u00a5\5\f\7\2\u00a5\u00ab")
        buf.write("\3\2\2\2\u00a6\u00a7\7:\2\2\u00a7\u00a8\5\22\n\2\u00a8")
        buf.write("\u00a9\7;\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a1\3\2\2\2")
        buf.write("\u00aa\u00a6\3\2\2\2\u00ab\r\3\2\2\2\u00ac\u00ad\5\20")
        buf.write("\t\2\u00ad\u00ae\7\67\2\2\u00ae\u00af\5\16\b\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00b2\5\20\t\2\u00b1\u00ac\3\2\2\2\u00b1")
        buf.write("\u00b0\3\2\2\2\u00b2\17\3\2\2\2\u00b3\u00b9\5\26\f\2\u00b4")
        buf.write("\u00b9\5\22\n\2\u00b5\u00b9\7B\2\2\u00b6\u00b9\5\24\13")
        buf.write("\2\u00b7\u00b9\7D\2\2\u00b8\u00b3\3\2\2\2\u00b8\u00b4")
        buf.write("\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\21\3\2\2\2\u00ba\u00bc\7\37\2\2\u00bb")
        buf.write("\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00be\t\2\2\2\u00be\23\3\2\2\2\u00bf\u00c0\t\3")
        buf.write("\2\2\u00c0\25\3\2\2\2\u00c1\u00c3\7<\2\2\u00c2\u00c4\5")
        buf.write("\30\r\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00c6\7=\2\2\u00c6\27\3\2\2\2\u00c7")
        buf.write("\u00c8\5\20\t\2\u00c8\u00c9\7\67\2\2\u00c9\u00ca\5\30")
        buf.write("\r\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd\5\20\t\2\u00cc\u00c7")
        buf.write("\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\31\3\2\2\2\u00ce\u00cf")
        buf.write("\5\34\17\2\u00cf\u00d0\5\"\22\2\u00d0\33\3\2\2\2\u00d1")
        buf.write("\u00d2\7\20\2\2\u00d2\u00d3\7\65\2\2\u00d3\u00d5\7\3\2")
        buf.write("\2\u00d4\u00d6\5\36\20\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6")
        buf.write("\3\2\2\2\u00d6\35\3\2\2\2\u00d7\u00d8\7\22\2\2\u00d8\u00d9")
        buf.write("\7\65\2\2\u00d9\u00da\5 \21\2\u00da\37\3\2\2\2\u00db\u00dc")
        buf.write("\5\b\5\2\u00dc\u00dd\7\67\2\2\u00dd\u00de\5 \21\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00e1\5\b\5\2\u00e0\u00db\3\2\2\2")
        buf.write("\u00e0\u00df\3\2\2\2\u00e1!\3\2\2\2\u00e2\u00e3\7\5\2")
        buf.write("\2\u00e3\u00e4\7\65\2\2\u00e4\u00e5\5(\25\2\u00e5\u00e6")
        buf.write("\7\13\2\2\u00e6\u00e7\7\66\2\2\u00e7#\3\2\2\2\u00e8\u00e9")
        buf.write("\5\4\3\2\u00e9\u00ea\5$\23\2\u00ea\u00ed\3\2\2\2\u00eb")
        buf.write("\u00ed\5\4\3\2\u00ec\u00e8\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed%\3\2\2\2\u00ee\u00f8\5*\26\2\u00ef\u00f8\5,\27")
        buf.write("\2\u00f0\u00f8\5\60\31\2\u00f1\u00f8\5\64\33\2\u00f2\u00f8")
        buf.write("\5\66\34\2\u00f3\u00f8\58\35\2\u00f4\u00f8\5:\36\2\u00f5")
        buf.write("\u00f8\5<\37\2\u00f6\u00f8\5> \2\u00f7\u00ee\3\2\2\2\u00f7")
        buf.write("\u00ef\3\2\2\2\u00f7\u00f0\3\2\2\2\u00f7\u00f1\3\2\2\2")
        buf.write("\u00f7\u00f2\3\2\2\2\u00f7\u00f3\3\2\2\2\u00f7\u00f4\3")
        buf.write("\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\'")
        buf.write("\3\2\2\2\u00f9\u00fb\5$\23\2\u00fa\u00f9\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb\u00ff\3\2\2\2\u00fc\u00fe\5&\24\2")
        buf.write("\u00fd\u00fc\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3")
        buf.write("\2\2\2\u00ff\u0100\3\2\2\2\u0100)\3\2\2\2\u0101\u00ff")
        buf.write("\3\2\2\2\u0102\u0103\5N(\2\u0103\u0104\7>\2\2\u0104\u0105")
        buf.write("\5B\"\2\u0105\u0106\7\64\2\2\u0106+\3\2\2\2\u0107\u0108")
        buf.write("\7\21\2\2\u0108\u0109\5B\"\2\u0109\u010a\7\24\2\2\u010a")
        buf.write("\u010c\5(\25\2\u010b\u010d\5.\30\2\u010c\u010b\3\2\2\2")
        buf.write("\u010c\u010d\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010f\7")
        buf.write("\t\2\2\u010f\u0111\5(\25\2\u0110\u010e\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7\f\2\2\u0113")
        buf.write("\u0114\7\66\2\2\u0114-\3\2\2\2\u0115\u0116\7\n\2\2\u0116")
        buf.write("\u0117\5B\"\2\u0117\u0118\7\24\2\2\u0118\u0119\5(\25\2")
        buf.write("\u0119\u011a\5.\30\2\u011a\u0121\3\2\2\2\u011b\u011c\7")
        buf.write("\n\2\2\u011c\u011d\5B\"\2\u011d\u011e\7\24\2\2\u011e\u011f")
        buf.write("\5(\25\2\u011f\u0121\3\2\2\2\u0120\u0115\3\2\2\2\u0120")
        buf.write("\u011b\3\2\2\2\u0121/\3\2\2\2\u0122\u0123\7\17\2\2\u0123")
        buf.write("\u0124\78\2\2\u0124\u0125\5\62\32\2\u0125\u0126\79\2\2")
        buf.write("\u0126\u0127\7\b\2\2\u0127\u0128\5(\25\2\u0128\u0129\7")
        buf.write("\r\2\2\u0129\u012a\7\66\2\2\u012a\61\3\2\2\2\u012b\u012c")
        buf.write("\7\3\2\2\u012c\u012d\7>\2\2\u012d\u012e\5B\"\2\u012e\u012f")
        buf.write("\7\67\2\2\u012f\u0130\5B\"\2\u0130\u0131\7\67\2\2\u0131")
        buf.write("\u0132\5B\"\2\u0132\63\3\2\2\2\u0133\u0134\7\25\2\2\u0134")
        buf.write("\u0135\5B\"\2\u0135\u0136\7\b\2\2\u0136\u0137\5(\25\2")
        buf.write("\u0137\u0138\7\16\2\2\u0138\u0139\7\66\2\2\u0139\65\3")
        buf.write("\2\2\2\u013a\u013b\7\b\2\2\u013b\u013c\5(\25\2\u013c\u013d")
        buf.write("\7\25\2\2\u013d\u013e\5B\"\2\u013e\u013f\7\30\2\2\u013f")
        buf.write("\u0140\7\66\2\2\u0140\67\3\2\2\2\u0141\u0142\7\6\2\2\u0142")
        buf.write("\u0143\7\64\2\2\u01439\3\2\2\2\u0144\u0145\7\7\2\2\u0145")
        buf.write("\u0146\7\64\2\2\u0146;\3\2\2\2\u0147\u0148\7\3\2\2\u0148")
        buf.write("\u014a\78\2\2\u0149\u014b\5R*\2\u014a\u0149\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\79\2\2")
        buf.write("\u014d\u014e\7\64\2\2\u014e=\3\2\2\2\u014f\u0151\7\23")
        buf.write("\2\2\u0150\u0152\5B\"\2\u0151\u0150\3\2\2\2\u0151\u0152")
        buf.write("\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\7\64\2\2\u0154")
        buf.write("?\3\2\2\2\u0155\u0156\7\3\2\2\u0156\u0158\78\2\2\u0157")
        buf.write("\u0159\5R*\2\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("\u015a\3\2\2\2\u015a\u015b\79\2\2\u015bA\3\2\2\2\u015c")
        buf.write("\u015d\5D#\2\u015d\u015e\5^\60\2\u015e\u015f\5D#\2\u015f")
        buf.write("\u0162\3\2\2\2\u0160\u0162\5D#\2\u0161\u015c\3\2\2\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162C\3\2\2\2\u0163\u0164\b#\1\2\u0164")
        buf.write("\u0165\5F$\2\u0165\u016c\3\2\2\2\u0166\u0167\f\4\2\2\u0167")
        buf.write("\u0168\5\\/\2\u0168\u0169\5F$\2\u0169\u016b\3\2\2\2\u016a")
        buf.write("\u0166\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016dE\3\2\2\2\u016e\u016c\3\2\2")
        buf.write("\2\u016f\u0170\b$\1\2\u0170\u0171\5H%\2\u0171\u0178\3")
        buf.write("\2\2\2\u0172\u0173\f\4\2\2\u0173\u0174\5X-\2\u0174\u0175")
        buf.write("\5H%\2\u0175\u0177\3\2\2\2\u0176\u0172\3\2\2\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("G\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\b%\1\2\u017c")
        buf.write("\u017d\5J&\2\u017d\u0184\3\2\2\2\u017e\u017f\f\4\2\2\u017f")
        buf.write("\u0180\5V,\2\u0180\u0181\5J&\2\u0181\u0183\3\2\2\2\u0182")
        buf.write("\u017e\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185I\3\2\2\2\u0186\u0184\3\2\2")
        buf.write("\2\u0187\u0188\7&\2\2\u0188\u018b\5J&\2\u0189\u018b\5")
        buf.write("L\'\2\u018a\u0187\3\2\2\2\u018a\u0189\3\2\2\2\u018bK\3")
        buf.write("\2\2\2\u018c\u018d\5Z.\2\u018d\u018e\5L\'\2\u018e\u0191")
        buf.write("\3\2\2\2\u018f\u0191\5N(\2\u0190\u018c\3\2\2\2\u0190\u018f")
        buf.write("\3\2\2\2\u0191M\3\2\2\2\u0192\u0193\b(\1\2\u0193\u0194")
        buf.write("\5P)\2\u0194\u0199\3\2\2\2\u0195\u0196\f\4\2\2\u0196\u0198")
        buf.write("\5b\62\2\u0197\u0195\3\2\2\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019aO\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019c\u01a3\5@!\2\u019d\u019e\78\2\2\u019e")
        buf.write("\u019f\5B\"\2\u019f\u01a0\79\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u01a3\5T+\2\u01a2\u019c\3\2\2\2\u01a2\u019d\3\2\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3Q\3\2\2\2\u01a4\u01a5\5B\"\2\u01a5")
        buf.write("\u01a6\7\67\2\2\u01a6\u01a7\5R*\2\u01a7\u01aa\3\2\2\2")
        buf.write("\u01a8\u01aa\5B\"\2\u01a9\u01a4\3\2\2\2\u01a9\u01a8\3")
        buf.write("\2\2\2\u01aaS\3\2\2\2\u01ab\u01ae\7\3\2\2\u01ac\u01ae")
        buf.write("\5\20\t\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("U\3\2\2\2\u01af\u01b0\t\4\2\2\u01b0W\3\2\2\2\u01b1\u01b2")
        buf.write("\t\5\2\2\u01b2Y\3\2\2\2\u01b3\u01b4\t\6\2\2\u01b4[\3\2")
        buf.write("\2\2\u01b5\u01b6\t\7\2\2\u01b6]\3\2\2\2\u01b7\u01b8\t")
        buf.write("\b\2\2\u01b8_\3\2\2\2\u01b9\u01ba\5d\63\2\u01ba\u01bb")
        buf.write("\5b\62\2\u01bba\3\2\2\2\u01bc\u01bd\7:\2\2\u01bd\u01be")
        buf.write("\5B\"\2\u01be\u01bf\7;\2\2\u01bf\u01c0\5b\62\2\u01c0\u01c6")
        buf.write("\3\2\2\2\u01c1\u01c2\7:\2\2\u01c2\u01c3\5B\"\2\u01c3\u01c4")
        buf.write("\7;\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01bc\3\2\2\2\u01c5")
        buf.write("\u01c1\3\2\2\2\u01c6c\3\2\2\2\u01c7\u01ca\7\3\2\2\u01c8")
        buf.write("\u01ca\5@!\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("e\3\2\2\2)iou{\u0081\u008e\u0096\u0098\u009c\u00aa\u00b1")
        buf.write("\u00b8\u00bb\u00c3\u00cc\u00d5\u00e0\u00ec\u00f7\u00fa")
        buf.write("\u00ff\u010c\u0110\u0120\u014a\u0151\u0158\u0161\u016c")
        buf.write("\u0178\u0184\u018a\u0190\u0199\u01a2\u01a9\u01ad\u01c5")
        buf.write("\u01c9")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Var'", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'int'", "'float'", 
                     "'boolean'", "'string'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'>='", "'<='", 
                     "'=/='", "'<.'", "'>.'", "'>=.'", "'<=.'", "';'", "':'", 
                     "'.'", "','", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "ID", "VAR", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "WHILE", "TRUE", "FALSE", "ENDDO", 
                      "INT_TYPE", "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
                      "ADD", "ADD_F", "SUB", "SUB_F", "MULTI", "MULTI_F", 
                      "DIV", "DIV_F", "MOD", "NOT", "ANDAND", "OROR", "EQUAL", 
                      "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "NOT_EQUAL_F", "LESS_THAN_F", "GREATER_THAN_F", 
                      "GREATER_EQUAL_F", "LESS_EQUAL_F", "SEMI", "COLON", 
                      "DOT", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACKET", 
                      "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "ASSIGN", 
                      "DECIMAL_INTEGER", "HEX_INTEGER", "OCT_INTEGER", "FLOAT", 
                      "BOOLEAN", "STRING", "SKIP_", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_variable_decl = 1
    RULE_variable_list = 2
    RULE_variable = 3
    RULE_array_decl = 4
    RULE_dimension = 5
    RULE_init_value = 6
    RULE_literal = 7
    RULE_integer = 8
    RULE_boolean_literal = 9
    RULE_array = 10
    RULE_array_list = 11
    RULE_body_decl = 12
    RULE_init_body = 13
    RULE_parameter = 14
    RULE_parameter_list = 15
    RULE_body = 16
    RULE_var_list = 17
    RULE_stmt = 18
    RULE_stmt_list = 19
    RULE_assign_stmt = 20
    RULE_if_stmt = 21
    RULE_else_if = 22
    RULE_for_stmt = 23
    RULE_for_condition = 24
    RULE_while_stmt = 25
    RULE_do_while_stmt = 26
    RULE_break_stmt = 27
    RULE_continue_stmt = 28
    RULE_call_stmt = 29
    RULE_return_stmt = 30
    RULE_function_call = 31
    RULE_exp = 32
    RULE_exp1 = 33
    RULE_exp2 = 34
    RULE_exp3 = 35
    RULE_exp4 = 36
    RULE_exp5 = 37
    RULE_exp6 = 38
    RULE_exp7 = 39
    RULE_exp_list = 40
    RULE_operands = 41
    RULE_multiplying_operators = 42
    RULE_adding_operators = 43
    RULE_sign_operators = 44
    RULE_boolean_operators = 45
    RULE_relational_operators = 46
    RULE_element_exp = 47
    RULE_index_operators = 48
    RULE_expr_index = 49

    ruleNames =  [ "program", "variable_decl", "variable_list", "variable", 
                   "array_decl", "dimension", "init_value", "literal", "integer", 
                   "boolean_literal", "array", "array_list", "body_decl", 
                   "init_body", "parameter", "parameter_list", "body", "var_list", 
                   "stmt", "stmt_list", "assign_stmt", "if_stmt", "else_if", 
                   "for_stmt", "for_condition", "while_stmt", "do_while_stmt", 
                   "break_stmt", "continue_stmt", "call_stmt", "return_stmt", 
                   "function_call", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp_list", "operands", "multiplying_operators", 
                   "adding_operators", "sign_operators", "boolean_operators", 
                   "relational_operators", "element_exp", "index_operators", 
                   "expr_index" ]

    EOF = Token.EOF
    ID=1
    VAR=2
    BODY=3
    BREAK=4
    CONTINUE=5
    DO=6
    ELSE=7
    ELSEIF=8
    ENDBODY=9
    ENDIF=10
    ENDFOR=11
    ENDWHILE=12
    FOR=13
    FUNCTION=14
    IF=15
    PARAMETER=16
    RETURN=17
    THEN=18
    WHILE=19
    TRUE=20
    FALSE=21
    ENDDO=22
    INT_TYPE=23
    FLOAT_TYPE=24
    BOOLEAN_TYPE=25
    STRING_TYPE=26
    ADD=27
    ADD_F=28
    SUB=29
    SUB_F=30
    MULTI=31
    MULTI_F=32
    DIV=33
    DIV_F=34
    MOD=35
    NOT=36
    ANDAND=37
    OROR=38
    EQUAL=39
    NOT_EQUAL=40
    LESS_THAN=41
    GREATER_THAN=42
    GREATER_EQUAL=43
    LESS_EQUAL=44
    NOT_EQUAL_F=45
    LESS_THAN_F=46
    GREATER_THAN_F=47
    GREATER_EQUAL_F=48
    LESS_EQUAL_F=49
    SEMI=50
    COLON=51
    DOT=52
    COMMA=53
    LEFT_PAREN=54
    RIGHT_PAREN=55
    LEFT_BRACKET=56
    RIGHT_BRACKET=57
    LEFT_BRACE=58
    RIGHT_BRACE=59
    ASSIGN=60
    DECIMAL_INTEGER=61
    HEX_INTEGER=62
    OCT_INTEGER=63
    FLOAT=64
    BOOLEAN=65
    STRING=66
    SKIP_=67
    ERROR_CHAR=68
    UNCLOSE_STRING=69
    ILLEGAL_ESCAPE=70
    UNTERMINATED_COMMENT=71

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

        def SKIP_(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SKIP_)
            else:
                return self.getToken(BKITParser.SKIP_, i)

        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declContext,i)


        def body_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Body_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Body_declContext,i)


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
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 100
                    self.match(BKITParser.SKIP_) 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 106
                self.variable_decl()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 112
                    self.match(BKITParser.SKIP_) 
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 118
                self.body_decl()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.SKIP_:
                self.state = 124
                self.match(BKITParser.SKIP_)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = BKITParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variable_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BKITParser.VAR)
            self.state = 133
            self.match(BKITParser.COLON)
            self.state = 134
            self.variable_list()
            self.state = 135
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def init_value(self):
            return self.getTypedRuleContext(BKITParser.Init_valueContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = BKITParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_list)
        self._la = 0 # Token type
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.variable()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.ASSIGN:
                    self.state = 138
                    self.match(BKITParser.ASSIGN)
                    self.state = 139
                    self.init_value()


                self.state = 142
                self.match(BKITParser.COMMA)
                self.state = 143
                self.variable_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.variable()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.ASSIGN:
                    self.state = 146
                    self.match(BKITParser.ASSIGN)
                    self.state = 147
                    self.init_value()


                pass


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

        def array_decl(self):
            return self.getTypedRuleContext(BKITParser.Array_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.array_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(BKITParser.DimensionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = BKITParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(BKITParser.ID)
            self.state = 157
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

        def LEFT_BRACKET(self):
            return self.getToken(BKITParser.LEFT_BRACKET, 0)

        def integer(self):
            return self.getTypedRuleContext(BKITParser.IntegerContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BKITParser.RIGHT_BRACKET, 0)

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
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 160
                self.integer()
                self.state = 161
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 162
                self.dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 165
                self.integer()
                self.state = 166
                self.match(BKITParser.RIGHT_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def init_value(self):
            return self.getTypedRuleContext(BKITParser.Init_valueContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_value" ):
                return visitor.visitInit_value(self)
            else:
                return visitor.visitChildren(self)




    def init_value(self):

        localctx = BKITParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_init_value)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.literal()
                self.state = 171
                self.match(BKITParser.COMMA)
                self.state = 172
                self.init_value()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def integer(self):
            return self.getTypedRuleContext(BKITParser.IntegerContext,0)


        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(BKITParser.Boolean_literalContext,0)


        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.array()
                pass
            elif token in [BKITParser.SUB, BKITParser.DECIMAL_INTEGER, BKITParser.HEX_INTEGER, BKITParser.OCT_INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.integer()
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.boolean_literal()
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 181
                self.match(BKITParser.STRING)
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


    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_INTEGER(self):
            return self.getToken(BKITParser.DECIMAL_INTEGER, 0)

        def HEX_INTEGER(self):
            return self.getToken(BKITParser.HEX_INTEGER, 0)

        def OCT_INTEGER(self):
            return self.getToken(BKITParser.OCT_INTEGER, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_integer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = BKITParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.SUB:
                self.state = 184
                self.match(BKITParser.SUB)


            self.state = 187
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.DECIMAL_INTEGER) | (1 << BKITParser.HEX_INTEGER) | (1 << BKITParser.OCT_INTEGER))) != 0)):
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


    class Boolean_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = BKITParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(BKITParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(BKITParser.RIGHT_BRACE, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(BKITParser.LEFT_BRACE)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (BKITParser.TRUE - 20)) | (1 << (BKITParser.FALSE - 20)) | (1 << (BKITParser.SUB - 20)) | (1 << (BKITParser.LEFT_BRACE - 20)) | (1 << (BKITParser.DECIMAL_INTEGER - 20)) | (1 << (BKITParser.HEX_INTEGER - 20)) | (1 << (BKITParser.OCT_INTEGER - 20)) | (1 << (BKITParser.FLOAT - 20)) | (1 << (BKITParser.STRING - 20)))) != 0):
                self.state = 192
                self.array_list()


            self.state = 195
            self.match(BKITParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKITParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_list)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.literal()
                self.state = 198
                self.match(BKITParser.COMMA)
                self.state = 199
                self.array_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_body(self):
            return self.getTypedRuleContext(BKITParser.Init_bodyContext,0)


        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_body_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_decl" ):
                return visitor.visitBody_decl(self)
            else:
                return visitor.visitChildren(self)




    def body_decl(self):

        localctx = BKITParser.Body_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_body_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.init_body()
            self.state = 205
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def parameter(self):
            return self.getTypedRuleContext(BKITParser.ParameterContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_body" ):
                return visitor.visitInit_body(self)
            else:
                return visitor.visitChildren(self)




    def init_body(self):

        localctx = BKITParser.Init_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_init_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(BKITParser.FUNCTION)
            self.state = 208
            self.match(BKITParser.COLON)
            self.state = 209
            self.match(BKITParser.ID)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 210
                self.parameter()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(BKITParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BKITParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(BKITParser.PARAMETER)
            self.state = 214
            self.match(BKITParser.COLON)
            self.state = 215
            self.parameter_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(BKITParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = BKITParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_parameter_list)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.variable()
                self.state = 218
                self.match(BKITParser.COMMA)
                self.state = 219
                self.parameter_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.variable()
                pass


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

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(BKITParser.BODY)
            self.state = 225
            self.match(BKITParser.COLON)
            self.state = 226
            self.stmt_list()
            self.state = 227
            self.match(BKITParser.ENDBODY)
            self.state = 228
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(BKITParser.Variable_declContext,0)


        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_list)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.variable_decl()
                self.state = 231
                self.var_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.variable_decl()
                pass


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


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 241
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 242
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 243
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 244
                self.return_stmt()
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

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


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
        self.enterRule(localctx, 38, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 247
                self.var_list()


            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 250
                    self.stmt() 
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.exp6(0)
            self.state = 257
            self.match(BKITParser.ASSIGN)
            self.state = 258
            self.exp()
            self.state = 259
            self.match(BKITParser.SEMI)
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

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def else_if(self):
            return self.getTypedRuleContext(BKITParser.Else_ifContext,0)


        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(BKITParser.IF)
            self.state = 262
            self.exp()
            self.state = 263
            self.match(BKITParser.THEN)
            self.state = 264
            self.stmt_list()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSEIF:
                self.state = 265
                self.else_if()


            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 268
                self.match(BKITParser.ELSE)
                self.state = 269
                self.stmt_list()


            self.state = 272
            self.match(BKITParser.ENDIF)
            self.state = 273
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_ifContext(ParserRuleContext):

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


        def else_if(self):
            return self.getTypedRuleContext(BKITParser.Else_ifContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if" ):
                return visitor.visitElse_if(self)
            else:
                return visitor.visitChildren(self)




    def else_if(self):

        localctx = BKITParser.Else_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_if)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(BKITParser.ELSEIF)
                self.state = 276
                self.exp()
                self.state = 277
                self.match(BKITParser.THEN)
                self.state = 278
                self.stmt_list()
                self.state = 279
                self.else_if()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(BKITParser.ELSEIF)
                self.state = 282
                self.exp()
                self.state = 283
                self.match(BKITParser.THEN)
                self.state = 284
                self.stmt_list()
                pass


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

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def for_condition(self):
            return self.getTypedRuleContext(BKITParser.For_conditionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

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
        self.enterRule(localctx, 46, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(BKITParser.FOR)
            self.state = 289
            self.match(BKITParser.LEFT_PAREN)
            self.state = 290
            self.for_condition()
            self.state = 291
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 292
            self.match(BKITParser.DO)
            self.state = 293
            self.stmt_list()
            self.state = 294
            self.match(BKITParser.ENDFOR)
            self.state = 295
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = BKITParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(BKITParser.ID)
            self.state = 298
            self.match(BKITParser.ASSIGN)
            self.state = 299
            self.exp()
            self.state = 300
            self.match(BKITParser.COMMA)
            self.state = 301
            self.exp()
            self.state = 302
            self.match(BKITParser.COMMA)
            self.state = 303
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
        self.enterRule(localctx, 50, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(BKITParser.WHILE)
            self.state = 306
            self.exp()
            self.state = 307
            self.match(BKITParser.DO)
            self.state = 308
            self.stmt_list()
            self.state = 309
            self.match(BKITParser.ENDWHILE)
            self.state = 310
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):

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
            return BKITParser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(BKITParser.DO)
            self.state = 313
            self.stmt_list()
            self.state = 314
            self.match(BKITParser.WHILE)
            self.state = 315
            self.exp()
            self.state = 316
            self.match(BKITParser.ENDDO)
            self.state = 317
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

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BKITParser.BREAK)
            self.state = 320
            self.match(BKITParser.SEMI)
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

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(BKITParser.CONTINUE)
            self.state = 323
            self.match(BKITParser.SEMI)
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

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(BKITParser.ID)
            self.state = 326
            self.match(BKITParser.LEFT_PAREN)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE) | (1 << BKITParser.DECIMAL_INTEGER) | (1 << BKITParser.HEX_INTEGER) | (1 << BKITParser.OCT_INTEGER))) != 0) or _la==BKITParser.FLOAT or _la==BKITParser.STRING:
                self.state = 327
                self.exp_list()


            self.state = 330
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 331
            self.match(BKITParser.SEMI)
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

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

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
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(BKITParser.RETURN)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE) | (1 << BKITParser.DECIMAL_INTEGER) | (1 << BKITParser.HEX_INTEGER) | (1 << BKITParser.OCT_INTEGER))) != 0) or _la==BKITParser.FLOAT or _la==BKITParser.STRING:
                self.state = 334
                self.exp()


            self.state = 337
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(BKITParser.ID)
            self.state = 340
            self.match(BKITParser.LEFT_PAREN)
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE) | (1 << BKITParser.DECIMAL_INTEGER) | (1 << BKITParser.HEX_INTEGER) | (1 << BKITParser.OCT_INTEGER))) != 0) or _la==BKITParser.FLOAT or _la==BKITParser.STRING:
                self.state = 341
                self.exp_list()


            self.state = 344
            self.match(BKITParser.RIGHT_PAREN)
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


        def relational_operators(self):
            return self.getTypedRuleContext(BKITParser.Relational_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.exp1(0)
                self.state = 347
                self.relational_operators()
                self.state = 348
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
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

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def boolean_operators(self):
            return self.getTypedRuleContext(BKITParser.Boolean_operatorsContext,0)


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
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 356
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 357
                    self.boolean_operators()
                    self.state = 358
                    self.exp2(0) 
                self.state = 364
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def adding_operators(self):
            return self.getTypedRuleContext(BKITParser.Adding_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 368
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 369
                    self.adding_operators()
                    self.state = 370
                    self.exp3(0) 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def multiplying_operators(self):
            return self.getTypedRuleContext(BKITParser.Multiplying_operatorsContext,0)


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
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 380
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 381
                    self.multiplying_operators()
                    self.state = 382
                    self.exp4() 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp4)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(BKITParser.NOT)
                self.state = 390
                self.exp4()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUB_F, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE, BKITParser.DECIMAL_INTEGER, BKITParser.HEX_INTEGER, BKITParser.OCT_INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.exp5()
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


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_operators(self):
            return self.getTypedRuleContext(BKITParser.Sign_operatorsContext,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp5)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.sign_operators()
                self.state = 395
                self.exp5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.exp6(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 407
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 404
                    self.index_operators() 
                self.state = 409
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp7)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
                self.match(BKITParser.LEFT_PAREN)
                self.state = 412
                self.exp()
                self.state = 413
                self.match(BKITParser.RIGHT_PAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 415
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = BKITParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp_list)
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.exp()
                self.state = 419
                self.match(BKITParser.COMMA)
                self.state = 420
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.exp()
                pass


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

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_operands)
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.match(BKITParser.ID)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.LEFT_BRACE, BKITParser.DECIMAL_INTEGER, BKITParser.HEX_INTEGER, BKITParser.OCT_INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.literal()
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


    class Multiplying_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTI(self):
            return self.getToken(BKITParser.MULTI, 0)

        def MULTI_F(self):
            return self.getToken(BKITParser.MULTI_F, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIV_F(self):
            return self.getToken(BKITParser.DIV_F, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_multiplying_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_operators" ):
                return visitor.visitMultiplying_operators(self)
            else:
                return visitor.visitChildren(self)




    def multiplying_operators(self):

        localctx = BKITParser.Multiplying_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_multiplying_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MULTI) | (1 << BKITParser.MULTI_F) | (1 << BKITParser.DIV) | (1 << BKITParser.DIV_F) | (1 << BKITParser.MOD))) != 0)):
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


    class Adding_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADD_F(self):
            return self.getToken(BKITParser.ADD_F, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_adding_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_operators" ):
                return visitor.visitAdding_operators(self)
            else:
                return visitor.visitChildren(self)




    def adding_operators(self):

        localctx = BKITParser.Adding_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_adding_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.ADD_F) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F))) != 0)):
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


    class Sign_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_sign_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_operators" ):
                return visitor.visitSign_operators(self)
            else:
                return visitor.visitChildren(self)




    def sign_operators(self):

        localctx = BKITParser.Sign_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_sign_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if not(_la==BKITParser.SUB or _la==BKITParser.SUB_F):
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


    class Boolean_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANDAND(self):
            return self.getToken(BKITParser.ANDAND, 0)

        def OROR(self):
            return self.getToken(BKITParser.OROR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_operators" ):
                return visitor.visitBoolean_operators(self)
            else:
                return visitor.visitChildren(self)




    def boolean_operators(self):

        localctx = BKITParser.Boolean_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_boolean_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            _la = self._input.LA(1)
            if not(_la==BKITParser.ANDAND or _la==BKITParser.OROR):
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


    class Relational_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKITParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(BKITParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(BKITParser.GREATER_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(BKITParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(BKITParser.LESS_EQUAL, 0)

        def NOT_EQUAL_F(self):
            return self.getToken(BKITParser.NOT_EQUAL_F, 0)

        def LESS_THAN_F(self):
            return self.getToken(BKITParser.LESS_THAN_F, 0)

        def GREATER_THAN_F(self):
            return self.getToken(BKITParser.GREATER_THAN_F, 0)

        def GREATER_EQUAL_F(self):
            return self.getToken(BKITParser.GREATER_EQUAL_F, 0)

        def LESS_EQUAL_F(self):
            return self.getToken(BKITParser.LESS_EQUAL_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relational_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operators" ):
                return visitor.visitRelational_operators(self)
            else:
                return visitor.visitChildren(self)




    def relational_operators(self):

        localctx = BKITParser.Relational_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_relational_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL) | (1 << BKITParser.LESS_THAN) | (1 << BKITParser.GREATER_THAN) | (1 << BKITParser.GREATER_EQUAL) | (1 << BKITParser.LESS_EQUAL) | (1 << BKITParser.NOT_EQUAL_F) | (1 << BKITParser.LESS_THAN_F) | (1 << BKITParser.GREATER_THAN_F) | (1 << BKITParser.GREATER_EQUAL_F) | (1 << BKITParser.LESS_EQUAL_F))) != 0)):
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


    class Element_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_index(self):
            return self.getTypedRuleContext(BKITParser.Expr_indexContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_element_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_exp" ):
                return visitor.visitElement_exp(self)
            else:
                return visitor.visitChildren(self)




    def element_exp(self):

        localctx = BKITParser.Element_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_element_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.expr_index()
            self.state = 440
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(BKITParser.LEFT_BRACKET, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BKITParser.RIGHT_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = BKITParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_index_operators)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 443
                self.exp()
                self.state = 444
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 445
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 448
                self.exp()
                self.state = 449
                self.match(BKITParser.RIGHT_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_index" ):
                return visitor.visitExpr_index(self)
            else:
                return visitor.visitChildren(self)




    def expr_index(self):

        localctx = BKITParser.Expr_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr_index)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.function_call()
                pass


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
        self._predicates[33] = self.exp1_sempred
        self._predicates[34] = self.exp2_sempred
        self._predicates[35] = self.exp3_sempred
        self._predicates[38] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




