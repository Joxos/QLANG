# Generated from .\Sakura.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SakuraParser import SakuraParser
else:
    from SakuraParser import SakuraParser

# This class defines a complete generic visitor for a parse tree produced by SakuraParser.

class SakuraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SakuraParser#block.
    def visitBlock(self, ctx:SakuraParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#literalValue.
    def visitLiteralValue(self, ctx:SakuraParser.LiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#expr.
    def visitExpr(self, ctx:SakuraParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#decvar.
    def visitDecvar(self, ctx:SakuraParser.DecvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#defvar.
    def visitDefvar(self, ctx:SakuraParser.DefvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#assvar.
    def visitAssvar(self, ctx:SakuraParser.AssvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#funcArgs.
    def visitFuncArgs(self, ctx:SakuraParser.FuncArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#funcHead.
    def visitFuncHead(self, ctx:SakuraParser.FuncHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#decfunc.
    def visitDecfunc(self, ctx:SakuraParser.DecfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#funcReturn.
    def visitFuncReturn(self, ctx:SakuraParser.FuncReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#defunc.
    def visitDefunc(self, ctx:SakuraParser.DefuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#callfunc.
    def visitCallfunc(self, ctx:SakuraParser.CallfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#ifcon.
    def visitIfcon(self, ctx:SakuraParser.IfconContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#elifcon.
    def visitElifcon(self, ctx:SakuraParser.ElifconContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#elsecon.
    def visitElsecon(self, ctx:SakuraParser.ElseconContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#fullIf.
    def visitFullIf(self, ctx:SakuraParser.FullIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#switchcon.
    def visitSwitchcon(self, ctx:SakuraParser.SwitchconContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#casecon.
    def visitCasecon(self, ctx:SakuraParser.CaseconContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#defaultcon.
    def visitDefaultcon(self, ctx:SakuraParser.DefaultconContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SakuraParser#fullSwitch.
    def visitFullSwitch(self, ctx:SakuraParser.FullSwitchContext):
        return self.visitChildren(ctx)



del SakuraParser