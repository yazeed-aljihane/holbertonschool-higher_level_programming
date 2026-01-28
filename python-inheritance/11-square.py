#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square's sides, kept private.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.

        Note:
            The size is validated using the `integer_validator` method
            inherited from BaseGeometry. We also call the super()
            initializer to maintain the Rectangle structure.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the Square instance.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def __str__(self):
        """Provides a string representation of the Square instance.

        Returns:
            str: A formatted string in the format [Square] <size>/<size>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
