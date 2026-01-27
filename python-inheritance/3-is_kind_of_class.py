#!/usr/bin/python3
"""Module containing the function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj is an instance or inherited from a_class, else False.
    """
    return isinstance(obj, a_class)
