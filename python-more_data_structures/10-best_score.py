#!/usr/bin/python3
def best_score(a_dictionary):
    for key in a_dictionary.keys():
        for k in a_dictionary.keys():
            if a_dictionary[key] < a_dictionary[k]:
                return k
