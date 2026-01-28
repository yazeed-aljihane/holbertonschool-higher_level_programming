#!/usr/bin/python3
"""Module for Rectangle class."""
base_geometry = __import__('7-base_geometry')


class Rectangle(base_geometry.BaseGeometry):
    """A representation of a rectangle that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle, kept private.
        __height (int): The height of the rectangle, kept private.
    """

    def __init__(self, width, height):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Note:
            Both width and height are validated using the `integer_validator`
            method inherited from BaseGeometry before assignment.
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle instance.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Provides a string representation of the Rectangle instance.

        Returns:
            str: A formatted string in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
