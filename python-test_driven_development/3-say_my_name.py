#!/usr/bin/python3
"""this module is made for
a function that say my name
like mohamed Ali
did in his combact
"""


def say_my_name(first_name, last_name=""):
    """this function take two input
the test them if they are strings
then print them respectevly"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
