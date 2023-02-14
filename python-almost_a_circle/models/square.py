#!/usr/bin/python3
"""rectangle.py
is a class inherteds
from Base"""

from models.base import Base
from models.rectangle import Rectangle


class Square (Rectangle):
    """Square

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return (self.__size)

    @width.setter
    def width(self, value):
        self.strictly_greater_than_zero("size", value)
        self.__size = value