import sys
from antlr4 import *
from URLLexer import URLLexer
from URLParser import URLParser

def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <arquivo>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            url_input = file.read()

        lexer = URLLexer(InputStream(url_input))
        stream = CommonTokenStream(lexer)
        parser = URLParser(stream)
        tree = parser.url()

        print(tree.toStringTree(recog=parser))

    except FileNotFoundError:
        print(f"Arquivo '{filename}' não encontrado.")
        sys.exit(1)

if __name__ == '__main__':
    main()
