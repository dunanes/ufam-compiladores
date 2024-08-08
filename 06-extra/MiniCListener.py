# Generated from MiniC.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#program.
    def enterProgram(self, ctx:MiniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParser#program.
    def exitProgram(self, ctx:MiniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParser#definition.
    def enterDefinition(self, ctx:MiniCParser.DefinitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#definition.
    def exitDefinition(self, ctx:MiniCParser.DefinitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#data_definition.
    def enterData_definition(self, ctx:MiniCParser.Data_definitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#data_definition.
    def exitData_definition(self, ctx:MiniCParser.Data_definitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#declarator.
    def enterDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#declarator.
    def exitDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#function_definition.
    def enterFunction_definition(self, ctx:MiniCParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#function_definition.
    def exitFunction_definition(self, ctx:MiniCParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#function_header.
    def enterFunction_header(self, ctx:MiniCParser.Function_headerContext):
        pass

    # Exit a parse tree produced by MiniCParser#function_header.
    def exitFunction_header(self, ctx:MiniCParser.Function_headerContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameter_list.
    def enterParameter_list(self, ctx:MiniCParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameter_list.
    def exitParameter_list(self, ctx:MiniCParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:MiniCParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:MiniCParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#function_body.
    def enterFunction_body(self, ctx:MiniCParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by MiniCParser#function_body.
    def exitFunction_body(self, ctx:MiniCParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by MiniCParser#block.
    def enterBlock(self, ctx:MiniCParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniCParser#block.
    def exitBlock(self, ctx:MiniCParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniCParser#statement.
    def enterStatement(self, ctx:MiniCParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#statement.
    def exitStatement(self, ctx:MiniCParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#expression.
    def enterExpression(self, ctx:MiniCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#expression.
    def exitExpression(self, ctx:MiniCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#binary.
    def enterBinary(self, ctx:MiniCParser.BinaryContext):
        pass

    # Exit a parse tree produced by MiniCParser#binary.
    def exitBinary(self, ctx:MiniCParser.BinaryContext):
        pass


    # Enter a parse tree produced by MiniCParser#unary.
    def enterUnary(self, ctx:MiniCParser.UnaryContext):
        pass

    # Exit a parse tree produced by MiniCParser#unary.
    def exitUnary(self, ctx:MiniCParser.UnaryContext):
        pass


    # Enter a parse tree produced by MiniCParser#primary.
    def enterPrimary(self, ctx:MiniCParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MiniCParser#primary.
    def exitPrimary(self, ctx:MiniCParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MiniCParser#argument_list.
    def enterArgument_list(self, ctx:MiniCParser.Argument_listContext):
        pass

    # Exit a parse tree produced by MiniCParser#argument_list.
    def exitArgument_list(self, ctx:MiniCParser.Argument_listContext):
        pass



del MiniCParser