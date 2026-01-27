#!/usr/bin/python3
"""This module provides a function to lookup object attributes and methods."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj (any): The object to be inspected.

    Returns:
        list: A list of strings containing the names of the object's 
        attributes and methods.
    """
    return dir(obj)
