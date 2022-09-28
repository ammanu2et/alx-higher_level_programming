#!/usr/bin/python3
"""module that returns an object represented by json"""
import json


def from_json_string(my_str):
    """
    my_str: the string or object
    Return: the json representation of an object
    """
    return json.loads(my_str)
