#!/usr/bin/env python2

from tag import Tag

class Token (object):
    def __init__(self, tag):
        self.tag = tag

class Num (Token):
    def __init__(self, value, t):
        super(Num, self).__init__(Tag.NUM)
        self.value = value
        self.data_type = t

    def __str__(self):
        return str(self.value)

class Word (Token):

    def __init__(self, lexeme, tag):
        self.lexeme = lexeme
        self.tag = tag

    def __str__(self):
        return str(self.lexeme)

class Type (Word):
    def __init__(self, lexeme, width):
        super(Type, self).__init__(lexeme, Tag.BASIC)
        self.width = width

    @staticmethod
    def max(p1, p2):
        if p1 == ReservedWords.Float or p2 == ReservedWords.Float:
            return ReservedWords.Float
        else:
            return ReservedWords.Int

class ReservedWords:
    Assign = Word('=', Tag.ASSIGN)
    Mul = Word('*', Tag.MUL)
    Add = Word('+', Tag.ADD)
    End = Word(';', Tag.END)
    Comma = Word(",", Tag.COMMA)
    OpenParan = Word("(", Tag.OPEN_PARAN)
    CloseParan = Word(")", Tag.CLOSE_PARAN)
    Int = Type("int", 4)
    Float = Type("float", 8)

