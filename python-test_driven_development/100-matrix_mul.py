#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a in ([],[[]]):
        raise ValueError("a_m can't be empty")
    if m_b in ([],[[]]):
        raise ValueError("b_m can't be empty")
    if all(not isinstance(i, (int,float)) for lst in m_a for i in lst):
        raise TypeError("m_a should contain only integers or floats")
    if all(not isinstance(i, (int,float)) for lst in m_b for i in lst):
        raise TypeError("m_b should contain only integers or floats")
    for i in range(len(m_b) - 1):
        if len(m_b[i]) != len(m_b[i + 1]):
            raise TypeError("each row of m_b must be of the same size")
    for i in range(len(m_a) - 1):
        if len(m_a[i]) != len(m_a[i + 1]):
            raise TypeError("each row of m_a must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
try:
    print(matrix_mul([[1, '2']], [[3, 4], [5, 6]]))
except Exception as e:
    print(e)