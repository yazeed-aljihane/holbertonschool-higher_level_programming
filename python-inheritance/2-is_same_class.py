#!/usr/bin/python3
""" here we difaine a function is_same_class

    this function help to know if the object is instance from specifc class
"""


def is_same_class(obj, a_class):
    """is_same_class: help to know if the object is instance from specifc class

    Args:
    obj(any): instance from class
    a_class(type): class

    Returns: true if instance from class or false otherwise
    """
    return type(obj) is a_class
