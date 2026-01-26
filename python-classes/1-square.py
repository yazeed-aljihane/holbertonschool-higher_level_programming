#!/usr/bin/python3
"""This module defines a Square class for geometric operations.

The module provides a specialized class to handle properties and
behaviors of squares, ensuring data integrity through private attributes.
"""


class Square:
    """A class used to represent a Square.

    This class provides a foundation for creating square objects with a
    specific size, ensuring that the attribute is kept private to
    prevent unauthorized modification.

    Attributes:
        __size (int): The dimension of one side of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square's side. Defaults to 0.
        """
        self.__size = size
