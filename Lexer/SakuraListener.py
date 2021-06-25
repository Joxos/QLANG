# Generated from .\Sakura.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SakuraParser import SakuraParser
else:
    from SakuraParser import SakuraParser

# This class defines a complete listener for a parse tree produced by SakuraParser.
class SakuraListener(ParseTreeListener):

    # Enter a parse tree produced by SakuraParser#block.
    def enterBlock(self, ctx:SakuraParser.BlockContext):
        pass

    # Exit a parse tree produced by SakuraParser#block.
    def exitBlock(self, ctx:SakuraParser.BlockContext):
        pass


    # Enter a parse tree produced by SakuraParser#literalValue.
    def enterLiteralValue(self, ctx:SakuraParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by SakuraParser#literalValue.
    def exitLiteralValue(self, ctx:SakuraParser.LiteralValueContext):
        pass


    # Enter a parse tree produced by SakuraParser#decvar.
    def enterDecvar(self, ctx:SakuraParser.DecvarContext):
        pass

    # Exit a parse tree produced by SakuraParser#decvar.
    def exitDecvar(self, ctx:SakuraParser.DecvarContext):
        pass


    # Enter a parse tree produced by SakuraParser#defvar.
    def enterDefvar(self, ctx:SakuraParser.DefvarContext):
        pass

    # Exit a parse tree produced by SakuraParser#defvar.
    def exitDefvar(self, ctx:SakuraParser.DefvarContext):
        pass


    # Enter a parse tree produced by SakuraParser#assvar.
    def enterAssvar(self, ctx:SakuraParser.AssvarContext):
        pass

    # Exit a parse tree produced by SakuraParser#assvar.
    def exitAssvar(self, ctx:SakuraParser.AssvarContext):
        pass


    # Enter a parse tree produced by SakuraParser#funcArgs.
    def enterFuncArgs(self, ctx:SakuraParser.FuncArgsContext):
        pass

    # Exit a parse tree produced by SakuraParser#funcArgs.
    def exitFuncArgs(self, ctx:SakuraParser.FuncArgsContext):
        pass


    # Enter a parse tree produced by SakuraParser#funcHead.
    def enterFuncHead(self, ctx:SakuraParser.FuncHeadContext):
        pass

    # Exit a parse tree produced by SakuraParser#funcHead.
    def exitFuncHead(self, ctx:SakuraParser.FuncHeadContext):
        pass


    # Enter a parse tree produced by SakuraParser#decfunc.
    def enterDecfunc(self, ctx:SakuraParser.DecfuncContext):
        pass

    # Exit a parse tree produced by SakuraParser#decfunc.
    def exitDecfunc(self, ctx:SakuraParser.DecfuncContext):
        pass


    # Enter a parse tree produced by SakuraParser#funcReturn.
    def enterFuncReturn(self, ctx:SakuraParser.FuncReturnContext):
        pass

    # Exit a parse tree produced by SakuraParser#funcReturn.
    def exitFuncReturn(self, ctx:SakuraParser.FuncReturnContext):
        pass


    # Enter a parse tree produced by SakuraParser#defunc.
    def enterDefunc(self, ctx:SakuraParser.DefuncContext):
        pass

    # Exit a parse tree produced by SakuraParser#defunc.
    def exitDefunc(self, ctx:SakuraParser.DefuncContext):
        pass


    # Enter a parse tree produced by SakuraParser#callfunc.
    def enterCallfunc(self, ctx:SakuraParser.CallfuncContext):
        pass

    # Exit a parse tree produced by SakuraParser#callfunc.
    def exitCallfunc(self, ctx:SakuraParser.CallfuncContext):
        pass



del SakuraParser