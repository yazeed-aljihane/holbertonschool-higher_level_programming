#!/usr/bin/python3
"""Module that contains the function inherits_from.

This module provides a way to check if an object is a subclass
instance specifically, excluding the class itself.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of class that inherited from a_class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
