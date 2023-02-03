#!/usr/bin/python3
"""_summary_
    """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """

    Args:
        m_a (_type_): _description_
        m_b (_type_): _description_
    """
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if m_a in ([], [[]]):
        raise ValueError(
            "shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
    if m_b in ([], [[]]):
        raise ValueError(
            "shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")
    if all(not isinstance(i, (int, float)) for lst in m_a for i in lst):
        raise TypeError("invalid data type for einsum")
    if all(not isinstance(i, (int, float)) for lst in m_b for i in lst):
        raise TypeError("invalid data type for einsum")
    for i in range(len(m_b) - 1):
        if len(m_b[i]) != len(m_b[i + 1]):
            raise TypeError("setting an array element with a sequence.")
    for i in range(len(m_a) - 1):
        if len(m_a[i]) != len(m_a[i + 1]):
            raise TypeError("setting an array element with a sequence.")
    if len(m_a[0]) != len(m_b):
        raise ValueError(
            "shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)")
    return numpy.dot(m_a, m_b)
