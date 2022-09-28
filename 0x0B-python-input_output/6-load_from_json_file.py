#!/usr/bin/python3
"""module that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """
    filename: name of the file
    Return: an object created from json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
