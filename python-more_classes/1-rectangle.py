#!/usr/bin/python3
"""1-rectangle.py"""


class Rectangle:
    """0-rectangle.py"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(value, int) and value < 0:
            raise TypeError("width must be an integer")
        self.__width = value
        return self.__width

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int) and value < 0:
            raise TypeError("width must be an integer")
        self.__height = value
        return self.__height
