# from antlr4 import *
# from HtmlLexer import HtmlLexer
# from HtmlParser import HtmlParser
# from HtmlVisitor import HtmlVisitor

# input_stream = InputStream(input('? '))
# lexer = HtmlLexer(input_stream)
# token_stream = CommonTokenStream(lexer)
# parser = HtmlParser(token_stream)
# tree = parser.root()
# visitor = HtmlVisitor()
# visitor.visit(tree)

from antlr4 import *
from HtmlLexer import HtmlLexer
from HtmlParser import HtmlParser
from Visitor import Visitor

def main():
  with open("entrada1.txt", "r") as f:
    input_stream = InputStream(f.read())

  lexer = HtmlLexer(input_stream)
  token_stream = CommonTokenStream(lexer)
  parser = HtmlParser(token_stream)
  tree = parser.root()
  visitor = Visitor()
  visitor.visit(tree)

if __name__ == "__main__":
  main()
