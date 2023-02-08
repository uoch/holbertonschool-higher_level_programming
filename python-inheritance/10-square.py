#!/usr/bin/python3

"""t
his task is for implimenting squar 
from Rectangle
"""

class BaseGeometry:
    """area() is not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle (BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (is a class): that created in module 7-base_geometry
        with the function integer_validator
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """the class square is a subclass from
rectangle

    Args:
            Rectangle (_type_): _description_
    """

    def __init__(self, size):
    	self.integer_validator("size", size)
    	super().__init__(size, size)
