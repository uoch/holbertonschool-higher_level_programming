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
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int) or\
                (value[0] < 0 or value[1] < 0) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
        return self.__position

    def area(self):
        return self.__size**2

    def __str__(self):
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            if self.__position[1] > 0:
                result += "\n" * self.__position[1]
            for i in range(self.__size):
                if self.__position[0] > 0:
                    result += (self.__position[0]) * \
                        ' ' + self.__size*'#' + "\n"
                else:
                    result += self.__size*'#' + "\n"
        return result[:-1]

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print(end='\n')
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print((self.__position[0]-1)*' ', self.__size*'#')
                else:
                    print(self.__size*'#')

    def __eq__(self, other):
        """Return True if the area of self is equal
        to the area of other, else return False."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the area of self is not
        equal to the area of other, else return False."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Return True if the area of self is greater
        than the area of other, else return False."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if the area of self is greater
        than or equal to the area of other, else return False."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Return True if the area of self is less
        than the area of other, else return False."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if the area of self is less
        than or equal to the area of other, else return False."""
        return self.area() <= other.area()
