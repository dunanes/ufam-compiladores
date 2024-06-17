import sys
from antlr4 import *
from miniCLexer import miniCLexer
from miniCParser import miniCParser

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            input_stream = InputStream(file.read())

        lexer = miniCLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = miniCParser(stream)
        tree = parser.program()

        print(tree.toStringTree(recog=parser))

    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
        sys.exit(1)

main()
