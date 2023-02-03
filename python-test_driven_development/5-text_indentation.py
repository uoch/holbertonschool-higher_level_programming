#!/usr/bin/python3
"""5-text_indentation.py"""


def text_indentation(text):
    """5-text_indentation.py"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in " ".join(text.split()):
        print(i, end="")
        if i in (':', '.', '?'):
            print("\n", end="\n")
    print()

text_indentation("Holberton. School? How are you:    John")
