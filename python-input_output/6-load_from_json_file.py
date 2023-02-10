#!/usr/bin/python3
"""6-load_from_json
_file.py"""
import json


def load_from_json_file(filename):
    """load_from_json_file

    Args:
            filename (_type_): json_file

    Returns:
            _type_: python objects
    """
    with open(filename, 'r', encoding="utf-8")as f:
        return json.load(f)
