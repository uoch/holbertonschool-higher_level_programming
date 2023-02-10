#!/usr/bin/python3
"""3-to_json_string.py"""
import json


def to_json_string(my_obj):
    """to_json_string

    Args:
        my_obj (_type_): the data to be serialized

    Returns:
        _type_: str(obj)
    """
    with open('f.json', 'w') as fp:
        json.dump(my_obj, fp)

    with open('f.json', 'r') as fp:
        return str(json.load(fp))

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))