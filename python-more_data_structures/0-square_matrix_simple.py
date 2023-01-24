#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    # create a copy of the input matrix
    new_matrix = matrix.copy()
    # use map to apply lambda function to each element in the matrix
    # the lambda function squares the element and returns the new value
    new_matrix = list(map(lambda row: list(
        map(lambda x: x**2, row)), new_matrix))
    return new_matrix
