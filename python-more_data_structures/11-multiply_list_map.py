#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x*number, my_list.copy()))


"""
The map() function takes two arguments, first one is a function, and the second one is an iterable 
(such as a list, tuple, etc.) and applies the function to each element of the iterable,
 and returns an iterator that produces the output.
"""
