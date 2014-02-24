#!/usr/bin/env python2

class EndOfFileError(Exception):
    def __str__(self):
        return repr("End of File")

class CompilerSyntaxError(Exception):

    def __init__(self, line):
        self.line = line

    def __str__(self):
        return ("Syntax error at line " + str(self.line))

class CompilerLexError (Exception):

    def __init__(self, line):
        self.line = line

    def __str__(self):
        return ("Syntax error at line " + str(self.line))

class TypeNarrowError (Exception):
    def __str__(self):
        return repr("Type narrowing!")
