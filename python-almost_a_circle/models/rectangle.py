#!/usr/bin/python3
"""rectangle.py
is a class inherteds
from Base"""

from models.base import Base


class Rectangle (Base):
    """Rectangle

    Args:
        Base (_type_): _description_
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        self.strictly_greater_than_zero("width", width)
        self.strictly_greater_than_zero("height", height)
        self.greater_than_zero("x", x)
        self.greater_than_zero("y", y)

    def strictly_greater_than_zero(self, string, value):
        """strictly_greater_than_zero

        Args:
            string (_type_): string
            value (_type_): number to test it
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(string))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(string))

    def greater_than_zero(self, string, value):
        """greater_than_zero

                Args:
                string (_type_): string
                value (_type_): number to test it
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(string))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(string))

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.strictly_greater_than_zero("height", value)
        self.__height = value

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.strictly_greater_than_zero("width", value)
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.greater_than_zero("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.greater_than_zero("y", value)
        self.__y = value

    def area(self):
        """
        that returns the area value of the Rectangle instance.
        """
        return (self.__height*self.__width)

    def display(self):
        """display"""
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x*" "+"#"*self.__width)

    def __str__(self):
        """rapport"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """update
        """
        if args:
            for i in range(len(args)):
                if i == 0:
                    super().__init__(args[0])
                if i == 1:
                    self.__width = args[1]
                if i == 2:
                    self.__height = args[2]
                if i == 3:
                    self.__x = args[3]
                if i == 4:
                    self.__y = args[4]
        else:
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']
            if 'id' in kwargs:
                super().__init__(kwargs['id'])

    def to_dictionary(self):
        """to_dictionary

        Returns:
            dic: dictionnary presntation
        """
        return {'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y}
