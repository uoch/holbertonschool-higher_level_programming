#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    new = my_list.copy()

    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            new[idx] = element
            return (new)
