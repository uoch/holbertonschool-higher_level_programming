#!/usr/bin/python3
"""This module contains the square class with size have been defined."""


class Square:
    """A class with first private attribute with try except to handal size value
        as integer and positive
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
