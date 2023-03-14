#!/usr/bin/python3
"""base.py"""
import json
import os
import turtle

class Base:
    """Base : Track to duplicting the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """rectangle.py"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file

        Args:
        list_objs (_type_): _description_
        """
        if list_objs is None:
            list_objs = []
        file = cls.__name__+".json"
        with open(file, 'w', encoding="utf-8") as f:
            list_dicts = [i.to_dictionary() for i in list_objs]
            k = cls.to_json_string(list_dicts)
            f.write(k)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string

        Args:
            json_string (_type_): _description_
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """Draw using turtle."""
        s = turtle.getscreen()
        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(0, 2):
                t.forward(rect.height)
                t.left(90)
                t.forward(rect.width)
                t.left(90)

        for sqr in list_squares:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(0, 4):
                t.forward(sqr.size)
                t.left(90)