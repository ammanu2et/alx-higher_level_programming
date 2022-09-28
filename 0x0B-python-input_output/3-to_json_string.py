#!/usr/bin/python3
""" module that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """
    my_obj: object
    Return: the json representation of an object
    """
    return json.dumps(my_obj)
