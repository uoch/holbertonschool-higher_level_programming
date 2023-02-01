#!/usr/bin/python3
"""4-print_square.py"""


def print_square(size):
    """4-print_square.py"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TabError(("size must be an integer"))
    for i in range(size):
        print(size*'#')
