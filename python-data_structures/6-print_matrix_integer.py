#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        print("{}".format(" ".join(map(str, matrix[i]))))
