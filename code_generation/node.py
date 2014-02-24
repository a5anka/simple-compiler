#!/usr/bin/env python2

from lexer.token import Type, ReservedWords
from errors import TypeNarrowError

class Node (object):
    temp_count = 0

    def __init__(self, operator, child1, child2):
        self.operator = operator
        self.child1 = child1
        self.child2 = child2
        self.generated = False
        self.temp_var = "ERROR"
        self.data_type = Type.max(child1.data_type, child2.data_type)

    def generate(self):
        child1_temp = self.child1.generate()
        child2_temp = self.child2.generate()

        if self.operator == '=':
            if (self.child1.data_type == self.child2.data_type):
                print child1_temp, '=', child2_temp
            elif (self.child1.data_type == ReservedWords.Float and
                  self.child2.data_type == ReservedWords.Int):
                Node.temp_count += 1
                temp_cast = "temp_" + str(Node.temp_count)

                print temp_cast, "= (float)", child2_temp
                print child1_temp, '=', temp_cast
            else:
                raise TypeNarrowError()

        if self.generated:
            return self.temp_var

        self.generated = True

        if self.operator == '+':
            Node.temp_count += 1
            self.temp_var = "temp_" + str(Node.temp_count)

            print self.temp_var , "=", child1_temp, '+', child2_temp
            return self.temp_var

        elif self.operator == '*':
            Node.temp_count += 1
            self.temp_var = "temp_" + str(Node.temp_count)

            print self.temp_var , "=", child1_temp, '*', child2_temp
            return self.temp_var


class Leaf (object):
    def __init__(self, token):
        self.token = token
        self.data_type = None

    def generate(self):
        return str(self.token)

    def __eq__(self, other):
        return str(self.token) == str(other.token)
