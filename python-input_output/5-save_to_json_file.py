#!/usr/bin/python3
"""Module for JSON file saving operations."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (any): The Python object to be serialized and saved.
        filename (str): The name of the file where the JSON string.

    Returns:
        None: This function does not return any value.

    Note:
        The function uses the 'with' statement for proper file handling and
        specifies 'utf-8' encoding. It uses `json.dumps` to create the
        JSON string before writing it to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json_string = json.dumps(my_obj)
        my_file.write(json_string)
