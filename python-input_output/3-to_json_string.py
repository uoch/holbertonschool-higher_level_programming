#!/usr/bin/python3
"""3-to_json_string.py"""
import json


def to_json_string(my_obj):
    """to_json_string

    Args:
        my_obj (_type_): the data to be serialized

    Returns:
        _type_: str(obj)
    """
    with open('f.json', 'w') as fp:
        json.dump(my_obj, fp)

    with open('f.json', 'r') as fp:
        return str(json.load(fp))
