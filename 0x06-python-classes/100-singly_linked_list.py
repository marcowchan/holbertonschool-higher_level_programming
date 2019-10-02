#!/usr/bin/python3
"""Defines a 'Node' class for a linked list"""


class Node:
    """Definition of a node"""
    def __init__(self, data, next_node=None):
        """Inits Node with data and next_node."""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not (next_node is None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        """Gets the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data with a value.

        Args:
            value: value to assign to data.
        Raises:
            TypeError: value is not an integer.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of the node.

        Args:
            value: value to set the next_node
        """
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Inits SinglyLinkedList with a head."""
        self.__head = None

    def __str__(self):
        """Returns a string with all data in the list"""
        tmp = self.__head
        datas = []
        while (tmp is not None):
            datas.append("{:d}".format(tmp.data))
            tmp = tmp.next_node
        return "\n".join(datas)

    def sorted_insert(self, value):
        """Inserts a new node in sorted order"""
        tmp = self.__head
        new = Node(value)
        if tmp is None:
            self.__head = new
            return
        if value < tmp.data:
            new.next_node = tmp
            self.__head = new
            return
        while (tmp.next_node is not None and value > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
