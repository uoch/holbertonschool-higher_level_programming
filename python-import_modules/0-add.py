#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    a = 10
    b = 5
    result1 = add(a, b)
    result2 = div(a, b)
    result3 = mul(a, b)
    result4 = sub(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result1))
    print("{:d} - {:d} = {:d}".format(a, b, result4))
    print("{:d} * {:d} = {:d}".format(a, b, result3))
    print("{:d} / {:d} = {:d}".format(a, b, result2))
