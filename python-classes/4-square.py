#!/usr/bin/python3
"""This module contains the square class with size have been defined.
    end calculate the area of the square
    """


class Square:
    """A class with a private attribute `size` to represent 
        the size of the square, and
        methods to handle the size value as an integer and positive,
        here we impliment the propriety and setter for the attrubute setter 
        and calculate the area of the square.
    """
    jls_extract_var

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2
