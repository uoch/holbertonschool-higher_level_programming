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
from /home/uoch/holbertonschool-higher_level_programming/python-import_modules/0-add.py import add

if __name__ == "__main__":
	
	a = 1
	b = 2
	result = add(a, b)
	print("{} + {} = {}".format(a, b, result))
