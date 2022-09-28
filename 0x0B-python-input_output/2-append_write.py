#!/usr/bin/python3
""" this module append a string at the end of a
    textfile and returns the number of characters added """


def append_write(filename="", text=""):
    """
    filename: the name of the file.
    text: the text
    Return: the number of appended characters
    """
    with open(filename, 'a', encoding="utf-8") as t:
        return t.write(text)
