'''
Representação Intermediária - Trabalho de Compiladores

Integrantes: 
Arthur Matias
Bianka Vasconcelos
Micael Viana
Daniel Nunes

Segue abaixo a main com a chamada do Eval Visitor para realizar a análise semântica e a representação intermediária.
'''


import sys
from antlr4 import *
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from EvalVisitor import EvalVisitor
# Verifica se o usuário forneceu o nome do arquivo como argumento
if len(sys.argv) != 2:
    print("Uso: python main.py nome_do_arquivo")
    sys.exit(1)

# Obtém o nome do arquivo a partir dos argumentos da linha de comando
nome_arquivo = sys.argv[1]

# Lê o conteúdo do arquivo
try:
    with open(nome_arquivo, 'r') as file:
        data = file.read()
except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
    sys.exit(1)

# Cria um InputStream a partir dos dados lidos do arquivo
input_stream = InputStream(data)

# Inicializa o lexer e o parser
lexer = MiniCLexer(input_stream)


token_stream = CommonTokenStream(lexer)

parser = MiniCParser(token_stream)



# parser.getErrorListenerDispatch


# Realiza a análise sintática
tree = parser.program()

numero_erros = parser.getNumberOfSyntaxErrors()
# print("NUmero === ",numero_erros)


if numero_erros == 0 :
    visitor = EvalVisitor()
    visitor.visit(tree)
else:
    if numero_erros > 1:
        print(f"Há {numero_erros} erros.")
    else:
        print(f"Há {numero_erros} erro.")