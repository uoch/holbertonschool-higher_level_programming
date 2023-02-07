#!/usr/bin/python3
"""3-is_kind_of_class.py"""


def is_kind_of_class(obj, a_class):
    """_summary_

    Args:
        obj (_type_): input
        a_class (_type_): input

    Returns:
        _type_: return true if they are instince of class
    """
    if isinstance(obj, a_class):
        return True
    if type(obj) == type(a_class):
        return True
    return False
