#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    n = my_list.copy()
    for i in range(len(n)):
        if n[i] == search:
            n[i] = replace
    return n
#result = list(map(lambda x: replace if x == search else x, my_list))
