#!/usr/bin/env python2

class Node (object):
    temp_count = 0

    def __init__(self, operator, child1, child2):
        self.operator = operator
        self.child1 = child1
        self.child2 = child2

    def generate(self):
        child1_temp = self.child1.generate()
        child2_temp = self.child2.generate()

        if self.operator == '+':
            Node.temp_count += 1
            temp_var = "temp_" + str(Node.temp_count)

            print temp_var , "=", child1_temp, '+', child2_temp
            return temp_var

        elif self.operator == '*':
            Node.temp_count += 1
            temp_var = "temp_" + str(Node.temp_count)

            print temp_var , "=", child1_temp, '*', child2_temp
            return temp_var

        elif self.operator == '=':
            print child1_temp, '=', child2_temp


class Leaf (object):
    def __init__(self, token):
        self.token = token

    def generate(self):
        return str(self.token)
