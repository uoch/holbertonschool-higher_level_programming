#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """write_file

    Args:
        filename (str, optional):  if file did'nt exist the "w"
        will created
        text (str, optional): the text to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
