#!/usr/bin/python3
"""2-is_same_class.py"""


def is_same_class(obj, a_class):
    """is-same_clase

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        _type_: _description_
    """
    if type(obj) == a_class:
        return True
    return False
