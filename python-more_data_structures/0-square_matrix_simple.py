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


"""
n this example, the outer map function is applied to the new_matrix variable, 
which is a two-dimensional list (a list of lists). Each element in this outer list represents a row in the matrix.
 The lambda function passed to the outer map function takes each row, which is also a one-dimensional list and applies the inner map function to it.
The inner map function is applied to each element in the row, which is also a one-dimensional list.
The lambda function passed to the inner map function takes each element, squares it, and returns the new value.
After the inner map function is applied to all elements in the row, 
it returns a new one-dimensional list with the squared elements. This new list is then passed back to the outer map function.

The outer map function then applies the same process to all the rows of the matrix and collects the results in a new matrix, 
where each element is squared. The result is assigned to the new_matrix variable, which is then returned by the function.

It is important to note that the input matrix (matrix=[] ) is a two-dimensional matrix, 
but the lambda function passed to the outer map function is applied to each row of the matrix, 
which is a one-dimensional list.
"""