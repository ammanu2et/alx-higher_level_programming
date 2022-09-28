#!/usr/bin/python3
""" module that contains a function that reads from a file"""


def read_file(filename=""):
    """
    read_file -  mode
    Return: read the file.
    """
    with open(filename, 'r', encoding="utf-8") as read_file:
        print(read_file.read(), end="")
