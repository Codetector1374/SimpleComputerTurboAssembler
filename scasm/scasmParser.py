# Generated from /home/codetector/projects/ece2031-scasm/scasm.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("u\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\5\2&\n")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\5\3.\n\3\3\3\5\3\61\n\3\3\4")
        buf.write("\5\4\64\n\4\3\4\3\4\5\48\n\4\3\5\3\5\3\5\3\6\3\6\3\6\5")
        buf.write("\6@\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\5\nP\n\n\3\13\3\13\3\13\5\13U\n\13\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\5\16^\n\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16g\n\16\3\17\3\17\3\17\3\17\5\17m\n")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\2\2\23\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"\2\4\3\2\r\16\3\2\3")
        buf.write("\5\2o\2%\3\2\2\2\4\60\3\2\2\2\6\63\3\2\2\2\b9\3\2\2\2")
        buf.write("\n?\3\2\2\2\fA\3\2\2\2\16D\3\2\2\2\20G\3\2\2\2\22O\3\2")
        buf.write("\2\2\24T\3\2\2\2\26V\3\2\2\2\30Y\3\2\2\2\32f\3\2\2\2\34")
        buf.write("l\3\2\2\2\36n\3\2\2\2 p\3\2\2\2\"r\3\2\2\2$&\5\6\4\2%")
        buf.write("$\3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\5\4\3\2()\7\2\2\3)\3")
        buf.write("\3\2\2\2*\61\3\2\2\2+-\7\7\2\2,.\5\6\4\2-,\3\2\2\2-.\3")
        buf.write("\2\2\2./\3\2\2\2/\61\5\4\3\2\60*\3\2\2\2\60+\3\2\2\2\61")
        buf.write("\5\3\2\2\2\62\64\5\b\5\2\63\62\3\2\2\2\63\64\3\2\2\2\64")
        buf.write("\67\3\2\2\2\658\5\n\6\2\668\5\26\f\2\67\65\3\2\2\2\67")
        buf.write("\66\3\2\2\28\7\3\2\2\29:\7\'\2\2:;\7\b\2\2;\t\3\2\2\2")
        buf.write("<@\5\f\7\2=@\5\16\b\2>@\5\20\t\2?<\3\2\2\2?=\3\2\2\2?")
        buf.write(">\3\2\2\2@\13\3\2\2\2AB\7\20\2\2BC\5\30\r\2C\r\3\2\2\2")
        buf.write("DE\7\21\2\2EF\5\30\r\2F\17\3\2\2\2GH\5\b\5\2HI\7\17\2")
        buf.write("\2IJ\5\30\r\2J\21\3\2\2\2KP\3\2\2\2LM\5\30\r\2MN\5\24")
        buf.write("\13\2NP\3\2\2\2OK\3\2\2\2OL\3\2\2\2P\23\3\2\2\2QR\7\f")
        buf.write("\2\2RU\5\22\n\2SU\3\2\2\2TQ\3\2\2\2TS\3\2\2\2U\25\3\2")
        buf.write("\2\2VW\7\22\2\2WX\5\22\n\2X\27\3\2\2\2YZ\5\32\16\2Z\31")
        buf.write("\3\2\2\2[^\5\"\22\2\\^\5 \21\2][\3\2\2\2]\\\3\2\2\2^_")
        buf.write("\3\2\2\2_`\5\34\17\2`g\3\2\2\2ab\7\n\2\2bc\5\32\16\2c")
        buf.write("d\7\13\2\2de\5\34\17\2eg\3\2\2\2f]\3\2\2\2fa\3\2\2\2g")
        buf.write("\33\3\2\2\2hm\3\2\2\2ij\5\36\20\2jk\5\32\16\2km\3\2\2")
        buf.write("\2lh\3\2\2\2li\3\2\2\2m\35\3\2\2\2no\t\2\2\2o\37\3\2\2")
        buf.write("\2pq\7\'\2\2q!\3\2\2\2rs\t\3\2\2s#\3\2\2\2\r%-\60\63\67")
        buf.write("?OT]fl")
        return buf.getvalue()


class scasmParser ( Parser ):

    grammarFileName = "scasm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':'", "';'", "'('", "')'", 
                     "','", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "INT_HEX", "INT_BIN", "INT_DEC", "White_Space", 
                      "EOL", "COLON", "SEMI", "LPARN", "RPARN", "COMMA", 
                      "ADD", "SUB", "DIR_EQU", "DIR_DW", "DIR_ORG", "OpCode", 
                      "OpNOP", "OpLOAD", "OpSTORE", "OpADD", "OpSUB", "OpJUMP", 
                      "OpJNEG", "OpJPOS", "OpJZERO", "OpAND", "OpOR", "OpXOR", 
                      "OpSHIFT", "OpADDI", "OpILOAD", "OpISTORE", "OpCALL", 
                      "OpRETURN", "OpIN", "OpOUT", "ID" ]

    RULE_scasmProg = 0
    RULE_scasmLines = 1
    RULE_scasmLine = 2
    RULE_label = 3
    RULE_directive = 4
    RULE_directiveDW = 5
    RULE_directiveORG = 6
    RULE_directiveEQU = 7
    RULE_argList = 8
    RULE_argListTail = 9
    RULE_instruction = 10
    RULE_constantArgument = 11
    RULE_expr = 12
    RULE_exprTail = 13
    RULE_binaryOperator = 14
    RULE_labelRef = 15
    RULE_integer = 16

    ruleNames =  [ "scasmProg", "scasmLines", "scasmLine", "label", "directive", 
                   "directiveDW", "directiveORG", "directiveEQU", "argList", 
                   "argListTail", "instruction", "constantArgument", "expr", 
                   "exprTail", "binaryOperator", "labelRef", "integer" ]

    EOF = Token.EOF
    INT_HEX=1
    INT_BIN=2
    INT_DEC=3
    White_Space=4
    EOL=5
    COLON=6
    SEMI=7
    LPARN=8
    RPARN=9
    COMMA=10
    ADD=11
    SUB=12
    DIR_EQU=13
    DIR_DW=14
    DIR_ORG=15
    OpCode=16
    OpNOP=17
    OpLOAD=18
    OpSTORE=19
    OpADD=20
    OpSUB=21
    OpJUMP=22
    OpJNEG=23
    OpJPOS=24
    OpJZERO=25
    OpAND=26
    OpOR=27
    OpXOR=28
    OpSHIFT=29
    OpADDI=30
    OpILOAD=31
    OpISTORE=32
    OpCALL=33
    OpRETURN=34
    OpIN=35
    OpOUT=36
    ID=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScasmProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scasmLines(self):
            return self.getTypedRuleContext(scasmParser.ScasmLinesContext,0)


        def EOF(self):
            return self.getToken(scasmParser.EOF, 0)

        def scasmLine(self):
            return self.getTypedRuleContext(scasmParser.ScasmLineContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_scasmProg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScasmProg" ):
                listener.enterScasmProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScasmProg" ):
                listener.exitScasmProg(self)




    def scasmProg(self):

        localctx = scasmParser.ScasmProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_scasmProg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scasmParser.DIR_DW) | (1 << scasmParser.DIR_ORG) | (1 << scasmParser.OpCode) | (1 << scasmParser.ID))) != 0):
                self.state = 34
                self.scasmLine()


            self.state = 37
            self.scasmLines()
            self.state = 38
            self.match(scasmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScasmLinesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOL(self):
            return self.getToken(scasmParser.EOL, 0)

        def scasmLines(self):
            return self.getTypedRuleContext(scasmParser.ScasmLinesContext,0)


        def scasmLine(self):
            return self.getTypedRuleContext(scasmParser.ScasmLineContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_scasmLines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScasmLines" ):
                listener.enterScasmLines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScasmLines" ):
                listener.exitScasmLines(self)




    def scasmLines(self):

        localctx = scasmParser.ScasmLinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scasmLines)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.EOF]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [scasmParser.EOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(scasmParser.EOL)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scasmParser.DIR_DW) | (1 << scasmParser.DIR_ORG) | (1 << scasmParser.OpCode) | (1 << scasmParser.ID))) != 0):
                    self.state = 42
                    self.scasmLine()


                self.state = 45
                self.scasmLines()
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


    class ScasmLineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directive(self):
            return self.getTypedRuleContext(scasmParser.DirectiveContext,0)


        def instruction(self):
            return self.getTypedRuleContext(scasmParser.InstructionContext,0)


        def label(self):
            return self.getTypedRuleContext(scasmParser.LabelContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_scasmLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScasmLine" ):
                listener.enterScasmLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScasmLine" ):
                listener.exitScasmLine(self)




    def scasmLine(self):

        localctx = scasmParser.ScasmLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_scasmLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 48
                self.label()


            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.DIR_DW, scasmParser.DIR_ORG, scasmParser.ID]:
                self.state = 51
                self.directive()
                pass
            elif token in [scasmParser.OpCode]:
                self.state = 52
                self.instruction()
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


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(scasmParser.ID, 0)

        def COLON(self):
            return self.getToken(scasmParser.COLON, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)




    def label(self):

        localctx = scasmParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(scasmParser.ID)
            self.state = 56
            self.match(scasmParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directiveDW(self):
            return self.getTypedRuleContext(scasmParser.DirectiveDWContext,0)


        def directiveORG(self):
            return self.getTypedRuleContext(scasmParser.DirectiveORGContext,0)


        def directiveEQU(self):
            return self.getTypedRuleContext(scasmParser.DirectiveEQUContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirective" ):
                listener.enterDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirective" ):
                listener.exitDirective(self)




    def directive(self):

        localctx = scasmParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.DIR_DW]:
                self.state = 58
                self.directiveDW()
                pass
            elif token in [scasmParser.DIR_ORG]:
                self.state = 59
                self.directiveORG()
                pass
            elif token in [scasmParser.ID]:
                self.state = 60
                self.directiveEQU()
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


    class DirectiveDWContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIR_DW(self):
            return self.getToken(scasmParser.DIR_DW, 0)

        def constantArgument(self):
            return self.getTypedRuleContext(scasmParser.ConstantArgumentContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_directiveDW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveDW" ):
                listener.enterDirectiveDW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveDW" ):
                listener.exitDirectiveDW(self)




    def directiveDW(self):

        localctx = scasmParser.DirectiveDWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_directiveDW)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(scasmParser.DIR_DW)
            self.state = 64
            self.constantArgument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveORGContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIR_ORG(self):
            return self.getToken(scasmParser.DIR_ORG, 0)

        def constantArgument(self):
            return self.getTypedRuleContext(scasmParser.ConstantArgumentContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_directiveORG

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveORG" ):
                listener.enterDirectiveORG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveORG" ):
                listener.exitDirectiveORG(self)




    def directiveORG(self):

        localctx = scasmParser.DirectiveORGContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_directiveORG)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(scasmParser.DIR_ORG)
            self.state = 67
            self.constantArgument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveEQUContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(scasmParser.LabelContext,0)


        def DIR_EQU(self):
            return self.getToken(scasmParser.DIR_EQU, 0)

        def constantArgument(self):
            return self.getTypedRuleContext(scasmParser.ConstantArgumentContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_directiveEQU

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirectiveEQU" ):
                listener.enterDirectiveEQU(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirectiveEQU" ):
                listener.exitDirectiveEQU(self)




    def directiveEQU(self):

        localctx = scasmParser.DirectiveEQUContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_directiveEQU)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.label()
            self.state = 70
            self.match(scasmParser.DIR_EQU)
            self.state = 71
            self.constantArgument()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constantArgument(self):
            return self.getTypedRuleContext(scasmParser.ConstantArgumentContext,0)


        def argListTail(self):
            return self.getTypedRuleContext(scasmParser.ArgListTailContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)




    def argList(self):

        localctx = scasmParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argList)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.EOF, scasmParser.EOL]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [scasmParser.INT_HEX, scasmParser.INT_BIN, scasmParser.INT_DEC, scasmParser.LPARN, scasmParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.constantArgument()
                self.state = 75
                self.argListTail()
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


    class ArgListTailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(scasmParser.COMMA, 0)

        def argList(self):
            return self.getTypedRuleContext(scasmParser.ArgListContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_argListTail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgListTail" ):
                listener.enterArgListTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgListTail" ):
                listener.exitArgListTail(self)




    def argListTail(self):

        localctx = scasmParser.ArgListTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argListTail)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(scasmParser.COMMA)
                self.state = 80
                self.argList()
                pass
            elif token in [scasmParser.EOF, scasmParser.EOL]:
                self.enterOuterAlt(localctx, 2)

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


    class InstructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpCode(self):
            return self.getToken(scasmParser.OpCode, 0)

        def argList(self):
            return self.getTypedRuleContext(scasmParser.ArgListContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = scasmParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(scasmParser.OpCode)
            self.state = 85
            self.argList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(scasmParser.ExprContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_constantArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantArgument" ):
                listener.enterConstantArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantArgument" ):
                listener.exitConstantArgument(self)




    def constantArgument(self):

        localctx = scasmParser.ConstantArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constantArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprTail(self):
            return self.getTypedRuleContext(scasmParser.ExprTailContext,0)


        def integer(self):
            return self.getTypedRuleContext(scasmParser.IntegerContext,0)


        def labelRef(self):
            return self.getTypedRuleContext(scasmParser.LabelRefContext,0)


        def LPARN(self):
            return self.getToken(scasmParser.LPARN, 0)

        def expr(self):
            return self.getTypedRuleContext(scasmParser.ExprContext,0)


        def RPARN(self):
            return self.getToken(scasmParser.RPARN, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = scasmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.INT_HEX, scasmParser.INT_BIN, scasmParser.INT_DEC, scasmParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [scasmParser.INT_HEX, scasmParser.INT_BIN, scasmParser.INT_DEC]:
                    self.state = 89
                    self.integer()
                    pass
                elif token in [scasmParser.ID]:
                    self.state = 90
                    self.labelRef()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 93
                self.exprTail()
                pass
            elif token in [scasmParser.LPARN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(scasmParser.LPARN)
                self.state = 96
                self.expr()
                self.state = 97
                self.match(scasmParser.RPARN)
                self.state = 98
                self.exprTail()
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


    class ExprTailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binaryOperator(self):
            return self.getTypedRuleContext(scasmParser.BinaryOperatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(scasmParser.ExprContext,0)


        def getRuleIndex(self):
            return scasmParser.RULE_exprTail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprTail" ):
                listener.enterExprTail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprTail" ):
                listener.exitExprTail(self)




    def exprTail(self):

        localctx = scasmParser.ExprTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprTail)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [scasmParser.EOF, scasmParser.EOL, scasmParser.RPARN, scasmParser.COMMA]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [scasmParser.ADD, scasmParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.binaryOperator()
                self.state = 104
                self.expr()
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


    class BinaryOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(scasmParser.ADD, 0)

        def SUB(self):
            return self.getToken(scasmParser.SUB, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_binaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOperator" ):
                listener.enterBinaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOperator" ):
                listener.exitBinaryOperator(self)




    def binaryOperator(self):

        localctx = scasmParser.BinaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_binaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not(_la==scasmParser.ADD or _la==scasmParser.SUB):
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


    class LabelRefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(scasmParser.ID, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_labelRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelRef" ):
                listener.enterLabelRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelRef" ):
                listener.exitLabelRef(self)




    def labelRef(self):

        localctx = scasmParser.LabelRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_labelRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(scasmParser.ID)
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

        def INT_HEX(self):
            return self.getToken(scasmParser.INT_HEX, 0)

        def INT_DEC(self):
            return self.getToken(scasmParser.INT_DEC, 0)

        def INT_BIN(self):
            return self.getToken(scasmParser.INT_BIN, 0)

        def getRuleIndex(self):
            return scasmParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = scasmParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << scasmParser.INT_HEX) | (1 << scasmParser.INT_BIN) | (1 << scasmParser.INT_DEC))) != 0)):
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





