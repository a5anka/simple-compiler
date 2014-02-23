#!/usr/bin/env python2

from errors import EndOfFileError, CompilerSyntaxError, CompilerLexError
from token import Word, Num, Type, ReservedWords
from tag import Tag

class Lexer (object):
    def __init__(self, filebuffer):
        self.filebuffer = filebuffer
        self.line = 1
        self.peek = ' '
        self.words = {}
        self.reserve(ReservedWords.Assign)
        self.reserve(ReservedWords.Mul)
        self.reserve(ReservedWords.Add)
        self.reserve(ReservedWords.End)
        self.reserve(ReservedWords.Comma)
        self.reserve(ReservedWords.OpenParan)
        self.reserve(ReservedWords.CloseParan)
        self.reserve(ReservedWords.Int)
        self.reserve(ReservedWords.Float)

    def reserve(self, w):
        self.words[w.lexeme] = w

    def read_char(self):
        self.peek = self.filebuffer.read(1)
        if not self.peek: raise EndOfFileError

    def read_and_check(self, expected):
        self.read_char()

        if self.peek != expected:
            return False

        self.peek = ' '
        return True

    def get_token_for(self, s):
        w = self.words.get(s)
        if w:
            return w

        w = Word(s, Tag.ID)
        self.words[s] = w

        return w

    def scan(self):
        while True:
            if self.peek == ' ' or self.peek == '\t':
                self.read_char()
                continue
            elif self.peek == '\n':
                self.line = self.line + 1
                self.read_char()
            else: break

        if self.peek == "=":
            self.peek = ' '
            return self.words['=']
        elif self.peek == "*":
            self.peek = ' '
            return self.words['*']
        elif self.peek == "+":
            self.peek = ' '
            return self.words['+']
        elif self.peek == ";":
            self.peek = ' '
            return self.words[';']
        elif self.peek == ",":
            self.peek = ' '
            return self.words[',']
        elif self.peek == "(":
            self.peek = ' '
            return self.words['(']
        elif self.peek == ")":
            self.peek = ' '
            return self.words[')']
        elif self.peek == "i":
            if self.read_and_check("n"):
                if self.read_and_check("t"):
                    return self.words["int"]
                else:
                    raise CompilerSyntaxError(self.line)
            else:
                return self.get_token_for("i")
        elif self.peek == "f":
            if self.read_and_check("l"):
                if (self.read_and_check("o") and
                    read_and_check("a") and
                    read_and_check("t")):
                    return self.words["float"]
                else:
                    raise CompilerSyntaxError(self.line)
            else:
                return self.get_token_for("f")

        if self.peek.isdigit():
            v = int(self.peek)
            self.read_char()
            while self.peek.isdigit():
                v = 10 * v + int(self.peek)
                read_char()

            if self.peek != '.': return Num(v)

            d = 10
            while True:
                read_char()
                if not self.peek.isdigit(): break
                v = v + float(self.peek) / d
                d = d * 10

            return Num(v)


        if self.peek.isalpha():
            b = str(self.peek)
            self.peek = ' '

            return self.get_token_for(b)

        raise CompilerLexError(self.line)
