#!/usr/bin/python3
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

    def area(self):
        return (self.__height*self.__width)

    def perimeter(self):
        return ((self.__height+self.__width)*2)
