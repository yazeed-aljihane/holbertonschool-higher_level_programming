#!/usr/bin/python3
"""This module defines a Rectangle class.

This module provides a basic template for rectangle objects,
including area, perimeter calculations, and various representations.
"""


class Rectangle:
    """A class used to represent a Rectangle.

    This class defines a rectangle by its width and height,
    ensuring data integrity through property setters. It also
    tracks the number of instances created.

    Attributes:
        number_of_instances (int): The total number of Rectangle instances.
        __width (int): The horizontal dimension of the rectangle.
        __height (int): The vertical dimension of the rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates the rectangle area.

        Returns:
            int: The area of the rectangle (height * width).
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the rectangle perimeter.

        Returns:
            int: The perimeter of the rectangle (2 * (height + width)).
            If width or height is 0, the perimeter is 0.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        The rectangle is represented by the '#' character.
        If width or height is 0, an empty string is returned.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Returns a string representation of the rectangle.

        The string is formatted to be a valid Python expression
        that can recreate a new instance using eval().

        Returns:
            str: A string in the format 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted.

        Also decrements the class attribute number_of_instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
