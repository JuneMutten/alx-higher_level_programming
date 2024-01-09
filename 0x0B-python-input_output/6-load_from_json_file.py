#!/usr/bin/python3



import json
"""Provides the functions needed for converting"""


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'"""
    with open(filename) as file:
        return json.load(file)
