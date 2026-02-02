#!/usr/bin/python3
"""Module for JSON string conversion operations."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted into a Python object.

    Returns:
        any: The Python object representation the JSON string (dict, list).

    Note:
        This function does not handle exceptions if the JSON string is invalid.
        The `json.loads` method is used for the conversion.
    """
    return json.loads(my_str)
