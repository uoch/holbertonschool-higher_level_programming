#!/usr/bin/python3
"""
Write a class Student that defines a student by:
"""


class Student:
    """
    * Public instance attributes:
        - first_name
        - last_name
        - age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, a=None):
        if (a is None):
            obj_dict = self.__dict__
            return (obj_dict)
        else:
            d = {}
            for i in a:
                if i == 'first_name':
                    d[i] = self.first_name
                if i == 'last_name':
                    d[i] = self.last_name
                if i == 'age':
                    d[i] = self.age
        return (d)
    def reload_from_json(self, json):
        for i in json:
            if i == 'first_name':
                self.first_name = json[i]
            if at == 'last_name':
                self.last_name = json[i]
            if at == 'age':
                self.age = json[i]