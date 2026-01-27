#!/usr/bin/python3
"""This module defines a Rectangle class.

This module provides a basic template for rectangle objects,
including area, perimeter calculations, representations, and a
factory method for squares.
"""


class Rectangle:
    """A class used to represent a Rectangle.

    Attributes:
        number_of_instances (int): The total number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
        __width (int): The horizontal dimension of the rectangle.
        __height (int): The vertical dimension of the rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: Gets or sets the width of the rectangle."""
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
        """int: Gets or sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the rectangle perimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = [str(self.print_symbol) * self.__width
                 for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Returns a string representation for recreation."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on their area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the square sides. Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance representing a square.
        """
        return cls(size, size)
