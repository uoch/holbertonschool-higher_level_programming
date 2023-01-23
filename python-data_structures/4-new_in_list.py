#!/usr/bin/python3
"""
It is important to note that in python lists are mutable objects, 
so if you modify the original list, it will change the copy too,
so it's important to use the .copy() method to create a new list and prevent modifying the original list
"""
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
