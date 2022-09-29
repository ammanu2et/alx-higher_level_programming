#!/usr/bin/python3
"""module that prints the sorted list"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """
        self: name of the list
        Return: sorted list
        """
        print(sorted(self))
