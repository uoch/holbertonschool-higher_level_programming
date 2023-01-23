#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        row = " ".join(str(x) for x in matrix[i])
        print("{:s}".format(row), end='')
        if i<len(matrix)-1:
            print()
