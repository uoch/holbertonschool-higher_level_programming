#!/usr/bin/python3
"""base.py"""
import json


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
        file = cls.__name__+".json"
        with open(file, 'w', encoding="utf-8") as f:
            list_dicts = [i.to_dictionary() for i in list_objs]
            k = cls.to_json_string(list_dicts)
            f.write(k)
