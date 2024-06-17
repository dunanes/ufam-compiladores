from antlr4 import *
from HtmlLexer import HtmlLexer
from HtmlParser import HtmlParser
from Visitor import Visitor

def main():
    # Abrindo o arquivo
    with open("entrada.txt", "r") as f:
        input_stream = InputStream(f.read())

    lexer = HtmlLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = HtmlParser(token_stream)
    tree = parser.root()
    visitor = Visitor()
    visitor.visit(tree)

    # Gerando um arquivo de saída
    output_filename = "saida.html"
    with open(output_filename, "w") as f:
        f.write(visitor.html.conteudo)

if __name__ == "__main__":
    main()