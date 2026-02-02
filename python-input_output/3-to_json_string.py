#!/usr/bin/python3
"""Defines a JSON-to-string conversion function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized into JSON format.

    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
