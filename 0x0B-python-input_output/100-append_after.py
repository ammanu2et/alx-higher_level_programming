#!/usr/bin/python3
"""module that inserts a line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    filename: the name of the file
    search_string: string to search
    new_string: string to append
    """
    n_line = []
    with open(filename, 'r', encoding="utf-8") as t:
        for line in t:
            n_line += [line]
            if line.find(search_string) != -1:
                n_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as t:
        t.write("".join(n_line))
