#!/usr/bin/python3
"""This module contains the square class with size have been defined.
    end calculate the area of the square
    """


class Square:
    """A class with first private attribute with try except to handal size value
        as integer and positive then calculate the area of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int) or\
                (value[0] < 0 or value[1] < 0) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
        return self.__position

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print((self.__position[0]-1)*' ', self.__size*'#')
                else:
                    print(self.__size*'#')

