#!/usr/bin/env python2

import sys

from lexer import Lexer
from errors import EndOfFileError, CompilerSyntaxError
from parser import Parser

def process_arguments():
    if len(sys.argv) != 2:
        print "Usage:\n     " , sys.argv[0] , "<input_file>\n"
        sys.exit(1);

    filename = sys.argv[1]

    return filename

def main():
    filename = process_arguments()

    with open(filename) as filebuffer:

        try:
            lex = Lexer(filebuffer)
            parser = Parser(lex)
            parser.P()

        except EndOfFileError:
            print "Syntax error at line " + str(lex.line)

        except CompilerSyntaxError as e:
            print e

if __name__ == '__main__':
    main()
