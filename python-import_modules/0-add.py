#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    a = 10
    b = 5
    result1 = add(a, b)
    result2 = div(a, b)
    result3 = mul(a, b)
    result4 = sub(a, b)
    print("{} + {} = {}".format(a, b, result1))
    print("{} - {} = {}".format(a, b, result4))
    print("{} * {} = {}".format(a, b, result3))
    print("{} / {} = {}".format(a, b, result2))
