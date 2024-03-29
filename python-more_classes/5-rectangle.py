#!/usr/bin/python3
"""1-rectangle.py"""


class Rectangle:
    """0-rectangle.py"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return self.__height

    def __str__(self):
        return self.my_print()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def area(self):
        return (self.__height*self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height+self.__width)*2)

    def my_print(self):
        r = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height-1):
            r += ((self.__width*'#') + '\n')
        r += ((self.__width*'#'))
        return r

    def __del__(self):
        print("Bye rectangle...")
        

