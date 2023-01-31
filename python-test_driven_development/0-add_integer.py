#!/usr/bin/python3
"""add_int to be tested
    as i undrestand is that the doc.txt
    works as it is our terminal and we should give the exact result like 
    the given from the intrepreter
    python3
    """


def add_integer(a, b=98):
    """first we have to check if the given data is a intger
    else we have to raise a typerror
    to tell the user he must put intger value 
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a+b)
