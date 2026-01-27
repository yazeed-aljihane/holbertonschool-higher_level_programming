#!/usr/bin/python3
""" here we difaine a function is_same_class

    this function help to know if the object is instance from specifc class
"""


def is_same_class(obj, a_class):
    """is_same_class: help to know if the object is instance from specifc class

    Aurgemant:
    obj: instance from class
    a_class: class

    Return: true if instance from class or false otherwise
    """
    return isinstance(obj, a_class)
