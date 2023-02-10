#!/usr/bin/python3
"""4-from_json_string.py"""
import json


def from_json_string(my_str):
    """from_json_string

    Args:
        my_str (_type_): json string

    Returns:
        _type_: python objet
    """
    return json.loads(my_str)
