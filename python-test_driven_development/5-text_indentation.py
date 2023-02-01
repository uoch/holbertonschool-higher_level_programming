#!/usr/bin/python3
"""5-text_indentation.py"""


def text_indentation(text):
    """5-text_indentation.py"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i == '.':
            print()
        if i == '?':
            print()
        if i == ':':
            print()
