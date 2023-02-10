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
    * Instantiation with first_name, last_name and age:
    * def __init__(self, first_name, last_name, age):
    * Public method def to_json(self, attrs=None): that retrieves
     a dictionary representation of a Student instance
     (same as 8-class_to_json.py):
        - If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved
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
