#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return (None)
    j = 0
    k = sorted(a_dictionary.keys())
    for i in a_dictionary.values():
        print("{}: {}".format(k[j], i))
        j += 1
