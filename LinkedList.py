# Author: Alec Ilstrup
# GitHub username: ailstrup
# Date: 11/11/2025
# Description: Implementation of a LinkedList class with recursive methods for adding,
# removing, inserting, reversing, and searching nodes. Includes a Node class
# to represent individual elements in the linked list.

class Node:
    """
    Represents a node in a linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT with recursive methods
    """

    def __init__(self):
        self._head = None

    def get_head(self):
        """
        Returns the first Node object in the list
        """
        return self._head

    def _rec_add(self, node, val):
        """
        Recursive helper for add method
        """
        if node.next is None:
            node.next = Node(val)
        else:
            self._rec_add(node.next, val)

    def add(self, val):
        """
        Recursively adds a node containing val to the end of the linked list
        """
        if self._head is None:
            self._head = Node(val)
        else:
            self._rec_add(self._head, val)

    def _rec_remove(self, node, val):
        """
        Recursive helper for remove method
        Returns the node that should be linked to
        """
        if node is None:
            return None

        if node.data == val:
            return node.next

        node.next = self._rec_remove(node.next, val)
        return node

    def remove(self, val):
        """
        Recursively removes the first node containing val from the linked list
        """
        self._head = self._rec_remove(self._head, val)

    def _rec_contains(self, node, key):
        """
        Recursive helper for contains method
        """
        if node is None:
            return False

        if node.data == key:
            return True

        return self._rec_contains(node.next, key)

    def contains(self, key):
        """
        Recursively checks if the linked list contains key
        Returns True if found, False otherwise
        """
        return self._rec_contains(self._head, key)

    def _rec_insert(self, node, val, pos, current_pos=0):
        """
        Recursive helper for insert method
        Returns the node that should be linked to
        """
        if current_pos == pos:
            new_node = Node(val)
            new_node.next = node
            return new_node

        if node is None:
            return None

        node.next = self._rec_insert(node.next, val, pos, current_pos + 1)
        return node

    def insert(self, val, pos):
        """
        Recursively inserts val at position pos in the linked list
        If pos is greater than the length of the list, insert at the end
        """
        if pos == 0:
            new_node = Node(val)
            new_node.next = self._head
            self._head = new_node
        else:
            self._head = self._rec_insert(self._head, val, pos)

    def _rec_reverse(self, node, prev=None):
        """
        Recursive helper for reverse method
        Returns the new head of the reversed list
        """
        if node is None:
            return prev

        next_node = node.next
        node.next = prev
        return self._rec_reverse(next_node, node)

    def reverse(self):
        """
        Recursively reverses the linked list by rearranging nodes
        """
        self._head = self._rec_reverse(self._head)

    def _rec_to_plain_list(self, node):
        """
        Recursive helper for to_plain_list method
        """
        if node is None:
            return []

        return [node.data] + self._rec_to_plain_list(node.next)

    def to_plain_list(self):
        """
        Recursively converts the linked list to a regular Python list
        Returns a list with the same values in the same order
        """
        return self._rec_to_plain_list(self._head)

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()