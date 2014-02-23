#!/usr/bin/env python2

import sys

def process_arguments():
    if len(sys.argv) != 2:
        print "Usage:\n     " , sys.argv[0] , "<input_file>\n"
        sys.exit(1);

    filename = sys.argv[1]

    return filename

def main():
    filename = process_arguments()

    with open(filename) as filebuffer:
        for line in filebuffer:
            stack = []
            for token in line.split():
                if token == "+":
                    v = stack.pop() + stack.pop()
                    stack.append(v)
                elif token == "*":
                    v = stack.pop() * stack.pop()
                    stack.append(v)
                else:
                    stack.append(int(token))
            print line, "=",  stack.pop() , "\n"

if __name__ == '__main__':
    main()
