#!/usr/bin/python3
"""5-text_indentation.py"""


def text_indentation(text):
    if not isinstance(text,str):
        raise TypeError ("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in [".",":","?"]:
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1

text_indentation("Holberton. School? How are you:    John")