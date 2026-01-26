#!/usr/bin/python3
"""This module defines a Rectangle class.

This module provides a basic template for rectangle objects,
following the requirements for class definitions.
"""


class Rectangle:
    """A class used to represent a Rectangle.

    This class defines a rectangle by its width and height,
    ensuring data integrity through setters.

    Attributes:
        __width (int): The horizontal dimension of the rectangle.
        __height (int): The vertical dimension of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle.

        The setter ensures the value is an integer and non-negative.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Gets or sets the height of the rectangle.

        The setter ensures the value is an integer and non-negative.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
