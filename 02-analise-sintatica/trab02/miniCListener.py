# Generated from miniC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .miniCParser import miniCParser
else:
    from miniCParser import miniCParser

# This class defines a complete listener for a parse tree produced by miniCParser.
class miniCListener(ParseTreeListener):

    # Enter a parse tree produced by miniCParser#program.
    def enterProgram(self, ctx:miniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by miniCParser#program.
    def exitProgram(self, ctx:miniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by miniCParser#definition.
    def enterDefinition(self, ctx:miniCParser.DefinitionContext):
        pass

    # Exit a parse tree produced by miniCParser#definition.
    def exitDefinition(self, ctx:miniCParser.DefinitionContext):
        pass


    # Enter a parse tree produced by miniCParser#data_definition.
    def enterData_definition(self, ctx:miniCParser.Data_definitionContext):
        pass

    # Exit a parse tree produced by miniCParser#data_definition.
    def exitData_definition(self, ctx:miniCParser.Data_definitionContext):
        pass


    # Enter a parse tree produced by miniCParser#declarator.
    def enterDeclarator(self, ctx:miniCParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by miniCParser#declarator.
    def exitDeclarator(self, ctx:miniCParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by miniCParser#function_definition.
    def enterFunction_definition(self, ctx:miniCParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by miniCParser#function_definition.
    def exitFunction_definition(self, ctx:miniCParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by miniCParser#type.
    def enterType(self, ctx:miniCParser.TypeContext):
        pass

    # Exit a parse tree produced by miniCParser#type.
    def exitType(self, ctx:miniCParser.TypeContext):
        pass


    # Enter a parse tree produced by miniCParser#function_header.
    def enterFunction_header(self, ctx:miniCParser.Function_headerContext):
        pass

    # Exit a parse tree produced by miniCParser#function_header.
    def exitFunction_header(self, ctx:miniCParser.Function_headerContext):
        pass


    # Enter a parse tree produced by miniCParser#parameter_list.
    def enterParameter_list(self, ctx:miniCParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by miniCParser#parameter_list.
    def exitParameter_list(self, ctx:miniCParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by miniCParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:miniCParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by miniCParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:miniCParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by miniCParser#function_body.
    def enterFunction_body(self, ctx:miniCParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by miniCParser#function_body.
    def exitFunction_body(self, ctx:miniCParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by miniCParser#statement.
    def enterStatement(self, ctx:miniCParser.StatementContext):
        pass

    # Exit a parse tree produced by miniCParser#statement.
    def exitStatement(self, ctx:miniCParser.StatementContext):
        pass


    # Enter a parse tree produced by miniCParser#block.
    def enterBlock(self, ctx:miniCParser.BlockContext):
        pass

    # Exit a parse tree produced by miniCParser#block.
    def exitBlock(self, ctx:miniCParser.BlockContext):
        pass


    # Enter a parse tree produced by miniCParser#expression.
    def enterExpression(self, ctx:miniCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by miniCParser#expression.
    def exitExpression(self, ctx:miniCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by miniCParser#binary.
    def enterBinary(self, ctx:miniCParser.BinaryContext):
        pass

    # Exit a parse tree produced by miniCParser#binary.
    def exitBinary(self, ctx:miniCParser.BinaryContext):
        pass


    # Enter a parse tree produced by miniCParser#unary.
    def enterUnary(self, ctx:miniCParser.UnaryContext):
        pass

    # Exit a parse tree produced by miniCParser#unary.
    def exitUnary(self, ctx:miniCParser.UnaryContext):
        pass


    # Enter a parse tree produced by miniCParser#primary.
    def enterPrimary(self, ctx:miniCParser.PrimaryContext):
        pass

    # Exit a parse tree produced by miniCParser#primary.
    def exitPrimary(self, ctx:miniCParser.PrimaryContext):
        pass


    # Enter a parse tree produced by miniCParser#argument_list.
    def enterArgument_list(self, ctx:miniCParser.Argument_listContext):
        pass

    # Exit a parse tree produced by miniCParser#argument_list.
    def exitArgument_list(self, ctx:miniCParser.Argument_listContext):
        pass



del miniCParser