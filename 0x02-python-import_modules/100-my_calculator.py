#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    count = len(argv)

    if count != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

def not_found():
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

def my_add():
    result = add(num1, num2)
    print("{:d} + {:d} = {:d}".format(num1, num2, result))
    return result

def my_sub():
    result = sub(num1, num2)
    print("{:d} - {:d} = {:d}".format(num1, num2, result))
    return result

def my_mul():
    result = mul(num1, num2)
    print("{:d} * {:d} = {:d}".format(num1, num2, result))
    return result

def my_div():
    result = div(num1, num2)
    print("{:d} / {:d} = {:d}".format(num1, num2, result))
    return result

options = { 
        "+": my_add,
        "-": my_sub,
        "*": my_mul,
        "/": my_div
        }
options.get(op, not_found)()
