#!/usr/bin/python3
"""5-base_geometry.py"""


class BaseGeometry:
    """area() is not implemented
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("age must be greater than 0")


bg = BaseGeometry()

try:
    bg.integer_validator("age", 13.5)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
