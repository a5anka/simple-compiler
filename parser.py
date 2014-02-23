#!/usr/bin/env python2

from tag import Tag
from errors import CompilerSyntaxError

class Parser (object):
    def __init__(self, lexer):
        self.lex = lexer
        self.move()

    def move(self):
        self.look = self.lex.scan()

    def match(self, tag):
        if self.look.tag == tag:
            self.move()
            return
        else:
            raise CompilerSyntaxError(self.lex.line)

    def P(self):
        self.D()
        self.L()

    def D(self):
        self.B()
        self.N()
        self.match(Tag.END)
        try:
            self.D()
        except CompilerSyntaxError:
            pass

    def B(self):
            self.match(Tag.BASIC)

    def N(self):
        self.match(Tag.ID)
        self.N1()

    def N1(self):
        try:
            self.match(Tag.COMMA)
            self.match(Tag.ID)
            self.N1()
        except CompilerSyntaxError:
            pass

    def L(self):
        self.S()
        self.match(Tag.END)
        try:
            self.L()
        except CompilerSyntaxError:
            pass

    def S(self):
        try:
            self.match(Tag.ID)
            self.match(Tag.ASSIGN)
            self.E()
        except CompilerSyntaxError:
            self.E()

    def E(self):
        self.T()
        self.E1()

    def E1(self):
        try:
            self.match(Tag.ADD)
            self.T()
            self.E1()
        except CompilerSyntaxError:
            pass

    def T(self):
        self.F()
        self.T1()

    def T1(self):
        try:
            self.match(Tag.MUL)
            self.F()
            self.T1()
        except CompilerSyntaxError:
            pass

    def F(self):
        try:
            self.match(Tag.OPEN_PARAN)
            self.E()
            self.match(Tag.CLOSE_PARAN)
        except CompilerSyntaxError:
            try:
                self.match(Tag.NUM)
            except:
                self.match(Tag.ID)
