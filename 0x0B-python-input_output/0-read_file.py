#!/usr/bin/python3
def read_file(filename=""):
    """
    read_file -  mode
    Return: read the file.
    """
    with open(filename, encoding="utf-8") as read_file:
        print(read_file.read())
