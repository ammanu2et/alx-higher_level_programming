#!/usr/bin/python3
"""module that returns the list of available attributes
    and methods of an object"""


def lookup(obj):
    """
    obj: the object
    Return: available attributes and methods
    """
    return dir(obj)
