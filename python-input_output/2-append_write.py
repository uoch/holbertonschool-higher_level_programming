#!/usr/bin/python3
"""2-append_write.py"""


def append_write(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): file exist append if don't exist create
        text (str, optional): _description_. Defaults to "".

    Returns:
        _type_: len of text
    """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
