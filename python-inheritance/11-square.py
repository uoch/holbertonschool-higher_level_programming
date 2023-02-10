#!/usr/bin/python3


"""
a class Square that inherits from Rectangle (9-rectangle.py):
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    *Instantiation with size: def __init__(self, size)::
    *size must be private. No getter or setter
    *size must be a positive integer, validated by integer_validator
    *the area() method must be implemented
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)