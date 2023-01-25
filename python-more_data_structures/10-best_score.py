#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 1:
        return list(a_dictionary.items())[0][0]
    for key in a_dictionary.keys():
        for k in a_dictionary.keys():
            if a_dictionary[key] < a_dictionary[k]:
                return k
