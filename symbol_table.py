#!/usr/bin/env python2

class SymbolTable (object):
    def __init__(self):
        self.table = {}

    def put(self, token, id):
        self.table[token] = id

    def get(self, token):
        return self.table.get(token)
