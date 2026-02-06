#!/usr/bin/python3
"""Basic serialization module for JSON data."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): A Python dictionary containing data to be serialized.
        filename (str): The name of the destination JSON file.
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(data, my_file)


def load_and_deserialize(filename):
    """Loads a JSON file and deserializes it into a Python dictionary.

    Args:
        filename (str): The name of the source JSON file.

    Returns:
        dict: A Python dictionary containing the deserialized JSON data.
    """
    with open(filename, mode='r', encoding='utf-8') as my_file:
        return json.load(my_file)
