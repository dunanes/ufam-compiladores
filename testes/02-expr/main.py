from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

# Carregar a entrada do terminal
input_stream = InputStream(input('? '))
# Criar um lexer
lexer = ExprLexer(input_stream)
# Criar um fluxo de tokens a partir do lexer - CommonTokenStream eh uma classe de antlr4
token_stream = CommonTokenStream(lexer)
# Criar um parser com o fluxo de tokens
parser = ExprParser(token_stream)
# Chamar o método inicial do parser
tree = parser.root()
# Imprimir a Arvore de Parser da entrada
print(tree.toStringTree(recog=parser))
