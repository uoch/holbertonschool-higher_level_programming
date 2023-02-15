#!/usr/bin/python3
"""base.py"""
import json
import os


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
    def load_from_file(cls):
        """load_from_file"""
        file = cls.__name__ + ".json"
        if not os.path.isfile(file):
            return []
        with open(file, 'r') as f:
            k = f.read()
            data = from_json_string(k)
        return (cls.create(**d)for d in data)
