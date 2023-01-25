#!/usr/bin/python3
def common_elements(set_1, set_2):
    k = []
    j = 0
    if (set_1 is None) or (set_2 is None):
        return None
    for i in set_1:
        for j in set_2:
            if i == j:
                k.append(i)
    return (k)
