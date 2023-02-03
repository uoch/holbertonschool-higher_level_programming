#!/usr/bin/python3
import numpy
"""_summary_
    """


def lazy_matrix_mul(m_a, m_b):
    """

    Args:
        m_a (_type_): _description_
        m_b (_type_): _description_
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a in ([], [[]]):
        raise ValueError("a_m can't be empty")
    if m_b in ([], [[]]):
        raise ValueError("b_m can't be empty")
    if all(not isinstance(i, (int, float)) for lst in m_a for i in lst):
        raise TypeError("m_a should contain only integers or floats")
    if all(not isinstance(i, (int, float)) for lst in m_b for i in lst):
        raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_b) - 1):
        if len(m_b[i]) != len(m_b[i + 1]):
            raise TypeError("each row of m_b must be of the same size")
    for i in range(len(m_a) - 1):
        if len(m_a[i]) != len(m_a[i + 1]):
            raise TypeError("each row of m_a must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return numpy.dot(m_a, m_b)

try:
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[3, 4]]))
except Exception as e:
    print(e)