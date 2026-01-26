#!/usr/bin/python3
"""This module defines a Square class with size properties and visualization.

The module provides a square representation that encapsulates size
and ensures all modifications adhere to type and value constraints,
along with methods to calculate area and print the square.
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
        """
        self.size = size

    @property
    def size(self):
        """int: Gets or sets the current size of the square.

        The setter validates that the value is an integer and non-negative.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the current square area.

        Returns:
            int: The area of the square, calculated as size squared.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the '#' character to stdout.

        If size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
