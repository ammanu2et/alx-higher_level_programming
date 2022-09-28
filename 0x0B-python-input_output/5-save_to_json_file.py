#!/usr/bin/python3
"""module that writes an object to a text file using json repr"""
import json


def save_to_json_file(my_obj, filename):
    """
    my_obj: object
    filename: name of file
    Return: JSON representation of an object
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
