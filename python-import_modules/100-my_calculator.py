#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == '+':
        result = add(a, b)
        print(f"{a} + {b} = {result}")
    elif op == '-':
        result = sub(a, b)
        print(f"{a} - {b} = {result}")
    elif op == '*':
        result = mul(a, b)
        print(f"{a} * {b} = {result}")
    elif op == '/':
        if b == 0:
            print("Error: Division the zéro")
            exit(1)
        result = div(a, b)
        print(f"{a} / {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
