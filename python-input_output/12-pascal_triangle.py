#!/usr/bin/python3
"""
* Create a function def pascal_triangle(n): that
 returns a list of lists of
 integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    * Returns an empty list if n <= 0
    * You can assume n will be always
    an integer
    * Representing the pascal's triangle of n. """
    if (n <= 0):
        return []

    t = []
    for i in range(n):
        if i == 0:
            t.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(t[i-1][j-1] + t[i-1][j])
            row.append(1)
            t.append(row)
    return t
