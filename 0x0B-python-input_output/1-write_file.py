#!/usr/bin/python3
"""module that writes a string to a text file
    utf8 and return the number of characters"""


def write_file(filename="", text=""):
    """ Function that writes to a text file
    Args:
        filename: filename
        text: text to write
    Raises
        Exception: when the file can be opened
    """

    with open(filename, 'w', encoding="utf-8") as t:
        t.write(text)

    with open(filename, encoding="utf-8") as t:
        return len(text)
