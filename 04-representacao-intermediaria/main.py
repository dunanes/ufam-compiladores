import sys
from antlr4 import *
from miniCLexer import miniCLexer
from miniCParser import miniCParser
from Visitor import ThreeAddressCodeGenerator

def main(argv):
    input_file = argv[1]

    input_stream = FileStream(input_file)
    lexer = miniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = miniCParser(stream)
    tree = parser.program()

    generator = ThreeAddressCodeGenerator()
    code = generator.generate_code(tree)

    for line in code:
        print(line)

if __name__ == '__main__':
    main(sys.argv)
