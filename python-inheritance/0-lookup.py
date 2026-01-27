#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of strings representing the object's attributes and methods.
    """
    return dir(obj)
