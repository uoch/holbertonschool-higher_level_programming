#!/usr/bin/python3
""" 
The del statement is used to delete an element, a variable or an object from memory. 
It can be used to delete a variable, 
list element, dictionary item or an item of an object.
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    del my_list[idx]
    return my_list
