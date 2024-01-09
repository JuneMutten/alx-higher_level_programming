#!/usr/bin/python3

"""To JSON string"""
import json
"""JSON module"""


def to_json_string(my_obj):
    """
     Returns the JSON representation of an object (string)
     no need to manage exceptions if the object can’t be serialized
    """
    return json.dumps(my_obj)
