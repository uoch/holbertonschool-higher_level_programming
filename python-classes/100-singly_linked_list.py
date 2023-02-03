#!/usr/bin/python3
"""liklist task
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
    """0-SinglyLinkedList implimentation"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value, self.__head)
        c = self.__head
        p = None
        while c and c.data < value:
            p = c
            c = c.next_node
        if p:
            p = new
        else:
            self.__head = new
        new.next_node = c

    def __str__(self):
        r = ""
        node = self.__head
        while node:
            r += str(node.data) + "\n"
            node = node.next_node
        return r
