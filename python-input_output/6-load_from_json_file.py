#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The path to the JSON file to be read.

    Returns:
        any: The Python data structure (typically a dict or list)
            represented by the JSON string in the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        json_string = file.read()
        return json.loads(json_string)
