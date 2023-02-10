#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file
    Args:
        my_obj (_type_): object to be written in json string
        filename (_type_): the file to store it
    """
    def save_to_json_file(items, filename):
        with open(filename, "w") as f:
            json.dump(items, f)

