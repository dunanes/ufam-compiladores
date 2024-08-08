from antlr4 import *

class ThreeAddressCodeGenerator(ParseTreeVisitor):
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f't{self.temp_count}'

    def new_label(self):
        self.label_count += 1
        return f'L{self.label_count}'

    def generate_code(self, ctx):
        print("Starting code generation")
        self.visit(ctx)
        return self.code

    def visitProgram(self, ctx):
        print("Visiting Program")
        for child in ctx.definition():
            self.visit(child)

    def visitFunction_definition(self, ctx):
        print("Visiting FunctionDefinition")
        func_name = ctx.function_header().declarator().getText()
        self.code.append(f'{func_name}:')
        self.visit(ctx.function_body())

    def visitFunction_body(self, ctx):
        print("Visiting FunctionBody")
        for child in ctx.data_definition():
            self.visit(child)
        for child in ctx.statement():
            self.visit(child)

    def visitData_definition(self, ctx):
        print("Visiting DataDefinition")
        for declarator in ctx.declarator():
            var_name = declarator.getText()
            self.code.append(f'{var_name} = 0')  # Inicialização padrão, se necessário

    def visitStatement(self, ctx):
        print("Visiting Statement")
        if ctx.expression():
            self.visit(ctx.expression())
        elif ctx.getChild(0).getText() == 'return':
            expr_code = self.visit(ctx.expression())
            self.code.append(f'return {expr_code}')

    def visitExpression(self, ctx):
        print("Visiting Expression")
        return self.visit(ctx.binary())

    def visitBinary(self, ctx):
        print("Visiting Binary")
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            if op in ['+', '-', '*', '/']:
                temp = self.new_temp()
                self.code.append(f'{temp} = {left} {op} {right}')
                return temp
            elif op == '=':
                self.code.append(f'{left} = {right}')
                return left
        elif ctx.Identifier():
            return ctx.Identifier().getText()
        elif ctx.CONSTANT_INT():
            return ctx.CONSTANT_INT().getText()
        return None

    def visitPrimary(self, ctx):
        print("Visiting Primary")
        if ctx.Identifier():
            return ctx.Identifier().getText()
        elif ctx.CONSTANT_INT():
            return ctx.CONSTANT_INT().getText()
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None

    def visitTerminal(self, node):
        print(f"Visiting Terminal: {node.getText()}")
        return node.getText()

    def visitDeclarator(self, ctx):
        print(f"Visiting Declarator: {ctx.getText()}")
        return ctx.getText()

    def visitType(self, ctx):
        print(f"Visiting Type: {ctx.getText()}")
        return ctx.getText()

    def visitParameter_list(self, ctx):
        print(f"Visiting Parameter_list: {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitFunction_header(self, ctx):
        print(f"Visiting Function_header: {ctx.getText()}")
        return self.visitChildren(ctx)

    def visitUnary(self, ctx):
        print("Visiting Unary")
        return self.visit(ctx.primary())

