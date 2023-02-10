#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file
    Args:
        my_obj (_type_): object to be written in json string
        filename (_type_): the file to store it
    """
    if type(my_obj) == set:
        k = str(my_obj)
    else:
        k = json.dumps(my_obj)
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(k)

