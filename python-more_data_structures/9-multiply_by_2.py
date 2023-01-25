#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is none:
        return None
    n = a_dictionary.copy()
    for key in n.keys():
        n[key] *= 2
    return n
