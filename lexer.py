#!/usr/bin/env python2

from errors import EndOfFileError

class Lexer:
    def __init__(self, filebuffer):
        self.filebuffer = filebuffer
        self.line = 1
        self.peek = ' '


    def scan(self):
        pass

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

        if self.peek.isdigit():
            v = self.peek
            self.read_char()
            while self.peek.isdigit():
                v = 10 * v + self.peek
                read_char()

            # TODO Handle floats
            print v
            return

        if self.peek.isalpha():
            b = "" + self.peek
            self.read_char()

            print b
            return

        print self.peek
        self.peek = ' '
        return
