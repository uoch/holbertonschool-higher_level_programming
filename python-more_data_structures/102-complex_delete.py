#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    for key in sorted(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
