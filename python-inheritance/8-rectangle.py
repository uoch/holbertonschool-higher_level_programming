#!/usr/bin/python3
"""8-rectangle.py"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
