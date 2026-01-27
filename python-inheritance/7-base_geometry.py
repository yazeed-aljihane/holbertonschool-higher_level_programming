#!/usr/bin/python3
"""Module that defines the BaseGeometry class.

This module serves as the foundation for future geometry-related
classes and operations.
"""


class BaseGeometry:
    """A base class for geometry objects.

    This class currently acts as a placeholder for more specific
    geometric shapes that will inherit from it.
    """

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: Always, because area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as a positive integer.

        Args:
            name (str): The name of the value, always a string.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
