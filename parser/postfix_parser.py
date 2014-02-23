#!/usr/bin/env python2

from lexer.tag import Tag
from errors import CompilerSyntaxError, EndOfFileError

class PostfixParser (object):
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
        except CompilerSyntaxError:
            return

        self.match(Tag.ID)
        self.N1()

    def L(self):
        self.S()
        try:
            self.match(Tag.END)
            print ""
        except EndOfFileError:
            pass

        try:
            self.L()
        except CompilerSyntaxError:
            pass

    def S(self):
        try:
            self.match(Tag.ID)
        except CompilerSyntaxError:
            self.E()
            return

        self.match(Tag.ASSIGN)
        self.E()

    def E(self):
        self.T()
        self.E1()

    def E1(self):
        try:
            self.match(Tag.ADD)
        except CompilerSyntaxError:
            return

        self.T()
        self.E1()
        print "+",

    def T(self):
        self.F()
        self.T1()

    def T1(self):
        try:
            self.match(Tag.MUL)
        except CompilerSyntaxError:
            return

        self.F()
        self.T1()
        print "*",

    def F(self):
        try:
            self.match(Tag.OPEN_PARAN)
        except CompilerSyntaxError:
            try:
                t = self.look
                self.match(Tag.NUM)
                print str(t),
            except CompilerSyntaxError:
                self.match(Tag.ID)
            return

        self.E()
        self.match(Tag.CLOSE_PARAN)
