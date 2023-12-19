#!/usr/bin/python3
"""
This is the "Single Linked List" module.
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or type(value) is Node):
            raise TypeError("next must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __repr__(self):
        temp = self.__head
        total = ""
        while temp:
            total += "{:d}".format(temp.data)
            temp = temp.next_node
            if temp:
                total += "\n"
        return total

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            curr = self.__head
            prev = None
            while curr and value > curr.data:
                prev = curr
                curr = curr.next_node
            if curr is None:
                prev.next_node = Node(value)
            elif curr is self.__head and prev is None:
                self.__head = Node(value, curr)
            else:
                newNode = Node(value, curr)
                prev.next_node = newNode
