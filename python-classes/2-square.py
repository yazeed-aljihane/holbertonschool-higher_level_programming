#!/usr/bin/python3
"""This module defines a Square class with size validation.

The module ensures that any Square instance created has a valid integer
size and enforces data integrity through private attributes and
proper error handling.
"""


class Square:
    """A class used to represent a Square.

    This class stores the size of a square and validates the input
    to ensure it meets geometric and technical requirements.

    Attributes:
        __size (int): The side length of the square, kept private.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The dimension of the square's side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
