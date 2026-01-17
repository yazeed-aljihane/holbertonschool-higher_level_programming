#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == '+':
        result = add(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3],
              result))
    elif sys.argv[2] == '-':
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3],
              result))
    elif sys.argv[2] == '*':
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3],
              result))
    elif sys.argv[2] == '/':
        result = div(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3],
              result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
