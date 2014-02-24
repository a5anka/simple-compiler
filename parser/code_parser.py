#!/usr/bin/env python2

from lexer.tag import Tag
from errors import CompilerSyntaxError, EndOfFileError
from code_generation.node import Leaf, Node

class CodeParser (object):
    def __init__(self, lexer):
        self.node_list = []
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
        b_type = self.B()
        self.N(b_type)
        self.match(Tag.END)
        try:
            self.D()
        except CompilerSyntaxError:
            pass

    def B(self):
            token = self.look
            self.match(Tag.BASIC)
            return token

    def N(self, inh):
        token = self.look
        self.match(Tag.ID)
        node = self.get_leaf(token)
        node.data_type = inh
        self.N1(inh)

    def N1(self, inh):
        try:
            self.match(Tag.COMMA)
        except CompilerSyntaxError:
            return

        token = self.look
        self.match(Tag.ID)
        node = self.get_leaf(token)
        node.data_type = inh

        self.N1(inh)

    def L(self):
        node = self.S()
        try:
            self.match(Tag.END)
        except EndOfFileError:
            node.generate()
            return

        node.generate()
        self.L()

    def S(self):
        token = self.look
        try:
            self.match(Tag.ID)
        except CompilerSyntaxError:
            node = self.E()
            return node

        self.match(Tag.ASSIGN)
        e_node = self.E()
        return self.get_node('=', self.get_leaf(token), e_node)

    def E(self):
        t_node = self.T()
        node = self.E1(t_node)
        return node

    def E1(self, inh):
        try:
            self.match(Tag.ADD)
        except CompilerSyntaxError:
            return inh

        t_node = self.T()
        node = self.E1(self.get_node('+', inh, t_node))
        return node

    def T(self):
        f_node = self.F()
        node = self.T1(f_node)
        return node

    def T1(self, inh):
        try:
            self.match(Tag.MUL)
        except CompilerSyntaxError:
            return inh

        f_node = self.F()
        node = self.T1(self.get_node('*', inh, f_node))
        return node

    def F(self):
        try:
            self.match(Tag.OPEN_PARAN)
        except CompilerSyntaxError:
            try:
                token = self.look
                self.match(Tag.NUM)
                node = self.get_leaf(token)
                node.data_type = token.data_type
            except CompilerSyntaxError:
                token = self.look
                self.match(Tag.ID)
                node = self.get_leaf(token)
            return node

        node = self.E()
        self.match(Tag.CLOSE_PARAN)
        return node

    def get_leaf(self, token):
        for i in self.node_list:
            if type(i) == Leaf and str(i.token) == str(token):
                return i

        node = Leaf(token)
        self.node_list.append(node)
        return node

    def get_node(self, op, l, r):
        for i in self.node_list:
            if (type(i) == Node and
                i.operator == op and
                type(i.child1) == type(l) and
                i.child1 == l and
                type(i.child2) == type(r) and
                i.child2 == r):
                return i

        node = Node(op, l, r)
        self.node_list.append(node)
        return node
