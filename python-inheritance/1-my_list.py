#!/usr/bin/python3
"""Module that defines a class MyList inheriting from list.

This module provides a specialized list with a sorted print method.
"""


class MyList(list):
    """A subclass of list with additional printing capabilities.

    Attributes:
        No new attributes added.
    """
    def print_sorted(self):
        """Prints the list in ascending sorted order.

        Assumes all elements are of type int.
        """
        print(sorted(self))
