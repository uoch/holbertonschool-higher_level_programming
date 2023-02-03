#!/usr/bin/python3
"""liklist task

    Raises:
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """
class Node:
    """this is a node class
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
        return self.__next_node


class SinglyLinkedList:
    """0-square.py"""

    def __init__(self):
    self.__head = None

    def print_list(self):
    if node.next_node == __head:
        while Node:
            print(Node.data)
            node = Node.next_node
