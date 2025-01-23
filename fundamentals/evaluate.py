# Created for BADS 2018
# See README.md for details
# Python 3

import math
import sys

from fundamentals import Stack
from stdlib import isEmpty
from stdlib import readString
from stdlib import writeln


def evaluate():
    ops = Stack()
    vals = Stack()

    while not isEmpty():
        # Read token, push if operator
        s = readString()
        if s == "(":
            pass
        elif s == "+":
            ops.push(s)
        elif s == "-":
            ops.push(s)
        elif s == "*":
            ops.push(s)
        elif s == "/":
            ops.push(s)
        elif s == "sqrt":
            ops.push(s)
        elif s == ")":
            # Pop, evaluate and push result if token is ")"
            op = ops.pop()
            v = vals.pop()
            if op == "+":
                v = vals.pop() + v
            elif op == "-":
                v = vals.pop() - v
            elif op == "*":
                v = vals.pop() * v
            elif op == "/":
                v = vals.pop() / v
            elif op == "sqrt":
                v = math.sqrt(v)
            vals.push(v)
        else:
            vals.push(float(s))
    writeln(vals.pop())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")

    evaluate()
