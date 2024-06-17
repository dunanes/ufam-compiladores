# Pequena correção que faltou do slide
from ExprVisitor import ExprVisitor

class EvalVisitor(ExprVisitor):
    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))

    def visitValue(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitSum(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) + self.visit(l[2])

    def visitSub(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) - self.visit(l[2])

    def visitMul(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) * self.visit(l[2])

    def visitDiv(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) / self.visit(l[2])