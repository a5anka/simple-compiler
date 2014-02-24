#!/usr/bin/env python2

class Node (object):
    temp_count = 0

    def __init__(self, operator, child1, child2):
        self.operator = operator
        self.child1 = child1
        self.child2 = child2
        self.generated = False
        self.temp_var = "ERROR"

    def generate(self):
        child1_temp = self.child1.generate()
        child2_temp = self.child2.generate()

        if self.operator == '=':
            print child1_temp, '=', child2_temp

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

    def generate(self):
        return str(self.token)

    def __eq__(self, other):
        return str(self.token) == str(other.token)
