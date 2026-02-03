#!/usr/bin/python3
"""Module for class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure.

    This function extracts the __dict__ attribute of an object to provide
    a serializable dictionary representation of the class instance.

    Args:
        obj (any): An instance of a Class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
