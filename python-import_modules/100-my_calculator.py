#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    operator_found = False
    op = ["+", "-", "/", "*"]
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in op:
        if sys.argv[2] == i:
            operator_found = True
            break
    if not operator_found:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == "+":
        r = add(a, b)
        print("{} + {} = {:d}".format(a, b, r))
    elif sys.argv[2] == "-":
        r = sub(a, b)
        print("{} - {} = {:d}".format(a, b, r))
    elif sys.argv[2] == "*":
        r = mul(a, b)
        print("{} * {} = {:d}".format(a, b, r))
    elif sys.argv[2] == "/":
        r = div(a, b)
        print("{} / {} = {:d}".format(a, b, r))
    else:
        exit(1)
