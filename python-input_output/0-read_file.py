#!/usr/bin/python3
"""0-read_file.py"""


def read_file(filename=""):
    """read_file

    Args:
        filename (str, optional): name of the file to be reading
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
