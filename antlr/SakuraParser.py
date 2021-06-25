# Generated from .\Sakura.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\7\2\"\n\2\f\2\16\2%\13\2\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7>\n\7\3\7\7\7A\n\7\f")
        buf.write("\7\16\7D\13\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7L\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\5\bU\n\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\7\f")
        buf.write("h\n\f\f\f\16\fk\13\f\3\f\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\2\3\3\2(+\2s\2#\3\2\2\2\4&\3\2\2\2")
        buf.write("\6(\3\2\2\2\b,\3\2\2\2\n\62\3\2\2\2\fB\3\2\2\2\16M\3\2")
        buf.write("\2\2\20V\3\2\2\2\22Y\3\2\2\2\24]\3\2\2\2\26b\3\2\2\2\30")
        buf.write("\"\7\5\2\2\31\"\7%\2\2\32\"\5\6\4\2\33\"\5\b\5\2\34\"")
        buf.write("\5\n\6\2\35\"\5\20\t\2\36\"\5\22\n\2\37\"\5\24\13\2 \"")
        buf.write("\5\26\f\2!\30\3\2\2\2!\31\3\2\2\2!\32\3\2\2\2!\33\3\2")
        buf.write("\2\2!\34\3\2\2\2!\35\3\2\2\2!\36\3\2\2\2!\37\3\2\2\2!")
        buf.write(" \3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\3\3\2\2\2%#")
        buf.write("\3\2\2\2&\'\t\2\2\2\'\5\3\2\2\2()\7\3\2\2)*\7*\2\2*+\7")
        buf.write("\r\2\2+\7\3\2\2\2,-\7\3\2\2-.\7*\2\2./\7\17\2\2/\60\5")
        buf.write("\4\3\2\60\61\7\r\2\2\61\t\3\2\2\2\62\63\7*\2\2\63\64\7")
        buf.write("\17\2\2\64\65\5\4\3\2\65\66\7\r\2\2\66\13\3\2\2\2\678")
        buf.write("\7\3\2\28>\7*\2\29:\7\3\2\2:;\7*\2\2;<\7\17\2\2<>\5\4")
        buf.write("\3\2=\67\3\2\2\2=9\3\2\2\2>?\3\2\2\2?A\7\13\2\2@=\3\2")
        buf.write("\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CK\3\2\2\2DB\3\2\2\2")
        buf.write("EF\7\3\2\2FL\7*\2\2GH\7\3\2\2HI\7*\2\2IJ\7\17\2\2JL\5")
        buf.write("\4\3\2KE\3\2\2\2KG\3\2\2\2L\r\3\2\2\2MN\7\4\2\2NO\7*\2")
        buf.write("\2OP\7\t\2\2PQ\5\f\7\2QT\7\n\2\2RS\7\37\2\2SU\7*\2\2T")
        buf.write("R\3\2\2\2TU\3\2\2\2U\17\3\2\2\2VW\5\16\b\2WX\7\r\2\2X")
        buf.write("\21\3\2\2\2YZ\7\6\2\2Z[\5\4\3\2[\\\7\r\2\2\\\23\3\2\2")
        buf.write("\2]^\5\16\b\2^_\7\26\2\2_`\5\2\2\2`a\7\27\2\2a\25\3\2")
        buf.write("\2\2bc\7*\2\2ci\7\26\2\2de\5\4\3\2ef\7\13\2\2fh\3\2\2")
        buf.write("\2gd\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2jl\3\2\2\2k")
        buf.write("i\3\2\2\2lm\5\4\3\2mn\7\27\2\2no\7\r\2\2o\27\3\2\2\2\t")
        buf.write("!#=BKTi")
        return buf.getvalue()


class SakuraParser ( Parser ):

    grammarFileName = "Sakura.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'func'", "'pass'", "'return'", 
                     "'.'", "'*'", "'('", "')'", "','", "':'", "';'", "'**'", 
                     "'='", "'['", "']'", "'+'", "'-'", "'/'", "'%'", "'{'", 
                     "'}'", "'<'", "'>'", "'=='", "'>='", "'<='", "'!='", 
                     "'@'", "'->'", "'+='", "'-='", "'*='", "'/='", "'%='" ]

    symbolicNames = [ "<INVALID>", "VAR", "FUNC", "PASS", "RETURN", "DOT", 
                      "STAR", "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", 
                      "SEMI_COLON", "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", 
                      "ADD", "MINUS", "DIV", "MOD", "OPEN_BRACE", "CLOSE_BRACE", 
                      "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
                      "NOT_EQ", "AT", "ARROW", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MULT_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "Comment", 
                      "WS", "Newline", "Interger", "Decimal", "Identifier", 
                      "String" ]

    RULE_block = 0
    RULE_literalValue = 1
    RULE_decvar = 2
    RULE_defvar = 3
    RULE_assvar = 4
    RULE_funcArgs = 5
    RULE_funcHead = 6
    RULE_decfunc = 7
    RULE_funcReturn = 8
    RULE_defunc = 9
    RULE_callfunc = 10

    ruleNames =  [ "block", "literalValue", "decvar", "defvar", "assvar", 
                   "funcArgs", "funcHead", "decfunc", "funcReturn", "defunc", 
                   "callfunc" ]

    EOF = Token.EOF
    VAR=1
    FUNC=2
    PASS=3
    RETURN=4
    DOT=5
    STAR=6
    OPEN_PAREN=7
    CLOSE_PAREN=8
    COMMA=9
    COLON=10
    SEMI_COLON=11
    POWER=12
    ASSIGN=13
    OPEN_BRACK=14
    CLOSE_BRACK=15
    ADD=16
    MINUS=17
    DIV=18
    MOD=19
    OPEN_BRACE=20
    CLOSE_BRACE=21
    LESS_THAN=22
    GREATER_THAN=23
    EQUALS=24
    GT_EQ=25
    LT_EQ=26
    NOT_EQ=27
    AT=28
    ARROW=29
    ADD_ASSIGN=30
    SUB_ASSIGN=31
    MULT_ASSIGN=32
    DIV_ASSIGN=33
    MOD_ASSIGN=34
    Comment=35
    WS=36
    Newline=37
    Interger=38
    Decimal=39
    Identifier=40
    String=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASS(self, i:int=None):
            if i is None:
                return self.getTokens(SakuraParser.PASS)
            else:
                return self.getToken(SakuraParser.PASS, i)

        def Comment(self, i:int=None):
            if i is None:
                return self.getTokens(SakuraParser.Comment)
            else:
                return self.getToken(SakuraParser.Comment, i)

        def decvar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.DecvarContext)
            else:
                return self.getTypedRuleContext(SakuraParser.DecvarContext,i)


        def defvar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.DefvarContext)
            else:
                return self.getTypedRuleContext(SakuraParser.DefvarContext,i)


        def assvar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.AssvarContext)
            else:
                return self.getTypedRuleContext(SakuraParser.AssvarContext,i)


        def decfunc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.DecfuncContext)
            else:
                return self.getTypedRuleContext(SakuraParser.DecfuncContext,i)


        def funcReturn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.FuncReturnContext)
            else:
                return self.getTypedRuleContext(SakuraParser.FuncReturnContext,i)


        def defunc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.DefuncContext)
            else:
                return self.getTypedRuleContext(SakuraParser.DefuncContext,i)


        def callfunc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.CallfuncContext)
            else:
                return self.getTypedRuleContext(SakuraParser.CallfuncContext,i)


        def getRuleIndex(self):
            return SakuraParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = SakuraParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SakuraParser.VAR) | (1 << SakuraParser.FUNC) | (1 << SakuraParser.PASS) | (1 << SakuraParser.RETURN) | (1 << SakuraParser.Comment) | (1 << SakuraParser.Identifier))) != 0):
                self.state = 31
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.match(SakuraParser.PASS)
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.match(SakuraParser.Comment)
                    pass

                elif la_ == 3:
                    self.state = 24
                    self.decvar()
                    pass

                elif la_ == 4:
                    self.state = 25
                    self.defvar()
                    pass

                elif la_ == 5:
                    self.state = 26
                    self.assvar()
                    pass

                elif la_ == 6:
                    self.state = 27
                    self.decfunc()
                    pass

                elif la_ == 7:
                    self.state = 28
                    self.funcReturn()
                    pass

                elif la_ == 8:
                    self.state = 29
                    self.defunc()
                    pass

                elif la_ == 9:
                    self.state = 30
                    self.callfunc()
                    pass


                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Interger(self):
            return self.getToken(SakuraParser.Interger, 0)

        def Identifier(self):
            return self.getToken(SakuraParser.Identifier, 0)

        def String(self):
            return self.getToken(SakuraParser.String, 0)

        def Decimal(self):
            return self.getToken(SakuraParser.Decimal, 0)

        def getRuleIndex(self):
            return SakuraParser.RULE_literalValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralValue" ):
                listener.enterLiteralValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralValue" ):
                listener.exitLiteralValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralValue" ):
                return visitor.visitLiteralValue(self)
            else:
                return visitor.visitChildren(self)




    def literalValue(self):

        localctx = SakuraParser.LiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SakuraParser.Interger) | (1 << SakuraParser.Decimal) | (1 << SakuraParser.Identifier) | (1 << SakuraParser.String))) != 0)):
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


    class DecvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SakuraParser.VAR, 0)

        def Identifier(self):
            return self.getToken(SakuraParser.Identifier, 0)

        def SEMI_COLON(self):
            return self.getToken(SakuraParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return SakuraParser.RULE_decvar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecvar" ):
                listener.enterDecvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecvar" ):
                listener.exitDecvar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecvar" ):
                return visitor.visitDecvar(self)
            else:
                return visitor.visitChildren(self)




    def decvar(self):

        localctx = SakuraParser.DecvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(SakuraParser.VAR)
            self.state = 39
            self.match(SakuraParser.Identifier)
            self.state = 40
            self.match(SakuraParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SakuraParser.VAR, 0)

        def Identifier(self):
            return self.getToken(SakuraParser.Identifier, 0)

        def ASSIGN(self):
            return self.getToken(SakuraParser.ASSIGN, 0)

        def literalValue(self):
            return self.getTypedRuleContext(SakuraParser.LiteralValueContext,0)


        def SEMI_COLON(self):
            return self.getToken(SakuraParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return SakuraParser.RULE_defvar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefvar" ):
                listener.enterDefvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefvar" ):
                listener.exitDefvar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefvar" ):
                return visitor.visitDefvar(self)
            else:
                return visitor.visitChildren(self)




    def defvar(self):

        localctx = SakuraParser.DefvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_defvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(SakuraParser.VAR)
            self.state = 43
            self.match(SakuraParser.Identifier)
            self.state = 44
            self.match(SakuraParser.ASSIGN)
            self.state = 45
            self.literalValue()
            self.state = 46
            self.match(SakuraParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SakuraParser.Identifier, 0)

        def ASSIGN(self):
            return self.getToken(SakuraParser.ASSIGN, 0)

        def literalValue(self):
            return self.getTypedRuleContext(SakuraParser.LiteralValueContext,0)


        def SEMI_COLON(self):
            return self.getToken(SakuraParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return SakuraParser.RULE_assvar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssvar" ):
                listener.enterAssvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssvar" ):
                listener.exitAssvar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssvar" ):
                return visitor.visitAssvar(self)
            else:
                return visitor.visitChildren(self)




    def assvar(self):

        localctx = SakuraParser.AssvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SakuraParser.Identifier)
            self.state = 49
            self.match(SakuraParser.ASSIGN)
            self.state = 50
            self.literalValue()
            self.state = 51
            self.match(SakuraParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(SakuraParser.VAR)
            else:
                return self.getToken(SakuraParser.VAR, i)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(SakuraParser.Identifier)
            else:
                return self.getToken(SakuraParser.Identifier, i)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(SakuraParser.ASSIGN)
            else:
                return self.getToken(SakuraParser.ASSIGN, i)

        def literalValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.LiteralValueContext)
            else:
                return self.getTypedRuleContext(SakuraParser.LiteralValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SakuraParser.COMMA)
            else:
                return self.getToken(SakuraParser.COMMA, i)

        def getRuleIndex(self):
            return SakuraParser.RULE_funcArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncArgs" ):
                listener.enterFuncArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncArgs" ):
                listener.exitFuncArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncArgs" ):
                return visitor.visitFuncArgs(self)
            else:
                return visitor.visitChildren(self)




    def funcArgs(self):

        localctx = SakuraParser.FuncArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcArgs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        self.state = 53
                        self.match(SakuraParser.VAR)
                        self.state = 54
                        self.match(SakuraParser.Identifier)
                        pass

                    elif la_ == 2:
                        self.state = 55
                        self.match(SakuraParser.VAR)
                        self.state = 56
                        self.match(SakuraParser.Identifier)
                        self.state = 57
                        self.match(SakuraParser.ASSIGN)
                        self.state = 58
                        self.literalValue()
                        pass


                    self.state = 61
                    self.match(SakuraParser.COMMA) 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 67
                self.match(SakuraParser.VAR)
                self.state = 68
                self.match(SakuraParser.Identifier)
                pass

            elif la_ == 2:
                self.state = 69
                self.match(SakuraParser.VAR)
                self.state = 70
                self.match(SakuraParser.Identifier)
                self.state = 71
                self.match(SakuraParser.ASSIGN)
                self.state = 72
                self.literalValue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncHeadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(SakuraParser.FUNC, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(SakuraParser.Identifier)
            else:
                return self.getToken(SakuraParser.Identifier, i)

        def OPEN_PAREN(self):
            return self.getToken(SakuraParser.OPEN_PAREN, 0)

        def funcArgs(self):
            return self.getTypedRuleContext(SakuraParser.FuncArgsContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(SakuraParser.CLOSE_PAREN, 0)

        def ARROW(self):
            return self.getToken(SakuraParser.ARROW, 0)

        def getRuleIndex(self):
            return SakuraParser.RULE_funcHead

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncHead" ):
                listener.enterFuncHead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncHead" ):
                listener.exitFuncHead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncHead" ):
                return visitor.visitFuncHead(self)
            else:
                return visitor.visitChildren(self)




    def funcHead(self):

        localctx = SakuraParser.FuncHeadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcHead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(SakuraParser.FUNC)
            self.state = 76
            self.match(SakuraParser.Identifier)
            self.state = 77
            self.match(SakuraParser.OPEN_PAREN)
            self.state = 78
            self.funcArgs()
            self.state = 79
            self.match(SakuraParser.CLOSE_PAREN)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SakuraParser.ARROW:
                self.state = 80
                self.match(SakuraParser.ARROW)
                self.state = 81
                self.match(SakuraParser.Identifier)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcHead(self):
            return self.getTypedRuleContext(SakuraParser.FuncHeadContext,0)


        def SEMI_COLON(self):
            return self.getToken(SakuraParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return SakuraParser.RULE_decfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecfunc" ):
                listener.enterDecfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecfunc" ):
                listener.exitDecfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecfunc" ):
                return visitor.visitDecfunc(self)
            else:
                return visitor.visitChildren(self)




    def decfunc(self):

        localctx = SakuraParser.DecfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_decfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.funcHead()
            self.state = 85
            self.match(SakuraParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SakuraParser.RETURN, 0)

        def literalValue(self):
            return self.getTypedRuleContext(SakuraParser.LiteralValueContext,0)


        def SEMI_COLON(self):
            return self.getToken(SakuraParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return SakuraParser.RULE_funcReturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncReturn" ):
                listener.enterFuncReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncReturn" ):
                listener.exitFuncReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncReturn" ):
                return visitor.visitFuncReturn(self)
            else:
                return visitor.visitChildren(self)




    def funcReturn(self):

        localctx = SakuraParser.FuncReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcReturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(SakuraParser.RETURN)
            self.state = 88
            self.literalValue()
            self.state = 89
            self.match(SakuraParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcHead(self):
            return self.getTypedRuleContext(SakuraParser.FuncHeadContext,0)


        def OPEN_BRACE(self):
            return self.getToken(SakuraParser.OPEN_BRACE, 0)

        def block(self):
            return self.getTypedRuleContext(SakuraParser.BlockContext,0)


        def CLOSE_BRACE(self):
            return self.getToken(SakuraParser.CLOSE_BRACE, 0)

        def getRuleIndex(self):
            return SakuraParser.RULE_defunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefunc" ):
                listener.enterDefunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefunc" ):
                listener.exitDefunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefunc" ):
                return visitor.visitDefunc(self)
            else:
                return visitor.visitChildren(self)




    def defunc(self):

        localctx = SakuraParser.DefuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_defunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.funcHead()
            self.state = 92
            self.match(SakuraParser.OPEN_BRACE)
            self.state = 93
            self.block()
            self.state = 94
            self.match(SakuraParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SakuraParser.Identifier, 0)

        def OPEN_BRACE(self):
            return self.getToken(SakuraParser.OPEN_BRACE, 0)

        def literalValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SakuraParser.LiteralValueContext)
            else:
                return self.getTypedRuleContext(SakuraParser.LiteralValueContext,i)


        def CLOSE_BRACE(self):
            return self.getToken(SakuraParser.CLOSE_BRACE, 0)

        def SEMI_COLON(self):
            return self.getToken(SakuraParser.SEMI_COLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SakuraParser.COMMA)
            else:
                return self.getToken(SakuraParser.COMMA, i)

        def getRuleIndex(self):
            return SakuraParser.RULE_callfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallfunc" ):
                listener.enterCallfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallfunc" ):
                listener.exitCallfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallfunc" ):
                return visitor.visitCallfunc(self)
            else:
                return visitor.visitChildren(self)




    def callfunc(self):

        localctx = SakuraParser.CallfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_callfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(SakuraParser.Identifier)
            self.state = 97
            self.match(SakuraParser.OPEN_BRACE)
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.literalValue()
                    self.state = 99
                    self.match(SakuraParser.COMMA) 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 106
            self.literalValue()
            self.state = 107
            self.match(SakuraParser.CLOSE_BRACE)
            self.state = 108
            self.match(SakuraParser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





