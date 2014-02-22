#!/usr/bin/env python2

from tag import Tag

class Token (object):
    def __init__(self, tag):
        self.tag = tag

class Num (Token):
    def __init__(self, value):
        super(Num, self).__init__(Tag.NUM)
        self.value = value

    def __str__(self):
        return str(self.value)

class Real (Token):
    def __init__(self, value):
        super(Num, self).__init__(Tag.REAL)
        self.value = value

    def __str__(self):
        return str(value)

class Word (Token):

    def __init__(self, lexeme, tag):
        self.lexeme = lexeme
        self.tag = tag

    def __str__(self):
        return str(self.lexeme)
