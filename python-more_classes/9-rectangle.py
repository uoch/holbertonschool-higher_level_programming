#!/usr/bin/python3
"""1-rectangle.py"""


class Rectangle:
    """0-rectangle.py"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
            r += ((self.__width*str(self.print_symbol) + '\n'))
        r += ((self.__width*str(self.print_symbol)))
        return r

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
