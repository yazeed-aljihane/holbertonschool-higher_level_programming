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

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int): The dimension of the square's side. Defaults to 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: Gets or sets the current size of the square.

        The setter validates that the value is an integer and non-negative.
        """
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple " +
                                "of 2 positive integers")
        self.__position = value

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
        return self.size * self.size

    def my_print(self):
        """Prints the square with the '#' character to stdout.

        If size is equal to 0, it prints an empty line.
        """
        if self.size == 0:
            print()
            return
        if self.position[1] > 0:
            for j in range(self.position[1]):
                print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
