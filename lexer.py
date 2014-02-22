#!/usr/bin/env python2

from errors import EndOfFileError, CompilerSyntaxError
from token import Word, Num
from tag import Tag

class Lexer:
    def __init__(self, filebuffer):
        self.filebuffer = filebuffer
        self.line = 1
        self.peek = ' '
        self.words = {}
        self.reserve(Word('=', Tag.ASSIGN))
        self.reserve(Word('*', Tag.MUL))
        self.reserve(Word('+', Tag.ADD))

    def reserve(self, w):
        self.words[w.lexeme] = w

    def read_char(self):
        self.peek = self.filebuffer.read(1)
        if not self.peek: raise EndOfFileError

    def read_and_check(self, expected):
        read_char()

        if peek != expected:
            return False

        self.peek = ' '
        return True

    def scan(self):
        while True:
            self.read_char()
            if self.peek == ' ' or self.peek == '\t': continue
            elif self.peek == '\n': self.line = self.line + 1
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

            return Real(v)


        if self.peek.isalpha():
            b = str(self.peek)
            self.peek = ' '

            w = self.words.get(b)
            if w:
                return w

            w = Word(b, Tag.ID)
            self.words[b] = w

            return w

        raise CompilerSyntaxError(self.line)
