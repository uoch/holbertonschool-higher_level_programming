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
		super().__init__(id)
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y

	def strictly_greater_than_zero(self, string, value):
        """strictly_greater_than_zero

        Args:
            string (_type_): string
            value (_type_): number to test it
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(string))
        if value <= 0:
            raise ValueError("{} must be > 0".format(string))

	def greater_than_zero(self, string, value):
        """greater_than_zero

        Args:
            string (_type_): string
            value (_type_): number to test it
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(string))
        if value < 0:
            raise ValueError("{} must be > 0".format(string))

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
