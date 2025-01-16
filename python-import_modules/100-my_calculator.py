#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    if len() != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int([1])
    op = [2]
    b = int([3])

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
        result = div(a, b)
        print(f"{a} / {b} = {result}")
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    print(f"{a} {op} {b} = {result}")


if __name__ == "__main__":
    main()