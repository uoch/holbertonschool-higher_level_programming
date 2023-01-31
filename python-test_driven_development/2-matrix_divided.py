#!/usr/bin/python3
"""0-add_integer.py"""


def matrix_divided(matrix, div):
    """2-matrix_divided.py"""
    for r in matrix:
        for el in r:
            if not isinstance(el, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
