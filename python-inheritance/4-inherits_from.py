#!/usr/bin/python3
"""4-inherits_from.py"""


def inherits_from(obj, a_class):
    """_summary_

    Args:
        obj (_type_): input
        a_class (_type_): input

    Returns:
        _type_: return true if they are instince of class
    """
    return issubclass(type(obj), a_class) and not (type(obj) is a_class)
