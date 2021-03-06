import argparse

from antlr4 import *
from loguru import logger
from antlr.QLANGLexer import QLANGLexer
from antlr.QLANGParser import QLANGParser
from antlr.QLANGVisitor import QLANGVisitor

parser = argparse.ArgumentParser(description="Interpreter for Sakura.")
parser.add_argument('file_name', type=str, help="file to compile")
args = parser.parse_args()


class MyQLANGVisitor(QLANGVisitor):

    # Visit a parse tree produced by QLANGParser#block.
    def visitBlock(self, ctx: QLANGParser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#statement.
    def visitStatement(self, ctx: QLANGParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#smallBlock.
    def visitSmallBlock(self, ctx: QLANGParser.SmallBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#literalValue.
    def visitLiteralValue(self, ctx: QLANGParser.LiteralValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#expression.
    def visitExpression(self, ctx: QLANGParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#declareVariable.
    def visitDeclareVariable(self, ctx: QLANGParser.DeclareVariableContext):
        logger.info(f"Declare variable {ctx.Identifier()} which type is {ctx.Identifier(1)}.")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#defineVariable.
    def visitDefineVariable(self, ctx: QLANGParser.DefineVariableContext):
        logger.info(f"Define variable {ctx.declareVariable()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#assignVariable.
    def visitAssignVariable(self, ctx: QLANGParser.AssignVariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#functionArgument.
    def visitFunctionArgument(self, ctx: QLANGParser.FunctionArgumentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#functionHead.
    def visitFunctionHead(self, ctx: QLANGParser.FunctionHeadContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#functionReturn.
    def visitFunctionReturn(self, ctx: QLANGParser.FunctionReturnContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#defineFunction.
    def visitDefineFunction(self, ctx: QLANGParser.DefineFunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#functionCall.
    def visitFunctionCall(self, ctx: QLANGParser.FunctionCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#ifCondition.
    def visitIfCondition(self, ctx: QLANGParser.IfConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#elifCondition.
    def visitElifCondition(self, ctx: QLANGParser.ElifConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#elseCondition.
    def visitElseCondition(self, ctx: QLANGParser.ElseConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#fullIf.
    def visitFullIf(self, ctx: QLANGParser.FullIfContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#fullEnumerate.
    def visitFullEnumerate(self, ctx: QLANGParser.FullEnumerateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#caseCondition.
    def visitCaseCondition(self, ctx: QLANGParser.CaseConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#defaultCondition.
    def visitDefaultCondition(self, ctx: QLANGParser.DefaultConditionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#whileLoop.
    def visitWhileLoop(self, ctx: QLANGParser.WhileLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#defineDecorator.
    def visitDefineDecorator(self, ctx: QLANGParser.DefineDecoratorContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by QLANGParser#callDecorator.
    def visitCallDecorator(self, ctx: QLANGParser.CallDecoratorContext):
        return self.visitChildren(ctx)


if __name__ == "__main__":
    lexer = QLANGLexer(FileStream(args.file_name))
    stream = CommonTokenStream(lexer)
    parser = QLANGParser(stream)
    tree = parser.prog()
    eval = ParseTreeVisitor()
    eval.visit(tree)
