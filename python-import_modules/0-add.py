#!/usr/bin/python3

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return a + b

if __name__ == "__main__":
	__import__('0-add')
	a = 1
	b = 2
	result = add(a, b)
	print("{} + {} = {}".format(a, b, result))
