#!/usr/bin/python3
"""_summary_

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """


class Node:
    """_summary_
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def data(self):
        return __data

    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__data = value
        return self.__data

    def next_node(self):
        return __next_node

    def next_node(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__next_node = value
        return __next_node


class SinglyLinkedList:
    pass
