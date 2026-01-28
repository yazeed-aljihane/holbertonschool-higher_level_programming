from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes.

    This class defines the interface for calculating area and perimeter
    that all concrete shape subclasses must implement.
    """

    @abstractmethod
    def area(self):
        """Calculates the area of the shape.

        Returns:
            float: The area of the shape.
        """
        ...

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        ...


class Circle(Shape):
    """Represents a circle shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius=0.0):
        """Initializes a Circle instance.

        Args:
            radius (float, optional): The radius the circle. Defaults to 0.0.
        """
        self.radius = radius

    def area(self):
        """Calculates the area the circle using pi * r^2.

        Returns:
            float: The calculated area.
        """
        return self.radius**2 * math.pi

    def perimeter(self):
        """Calculates the perimeter (circumference)the circle using 2 * pi * r.

        Returns:
            float: The calculated perimeter.
        """
        return abs(self.radius * math.pi * 2)


class Rectangle(Shape):
    """Represents a rectangle shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (float, optional): The width the rectangle. Defaults to 0.
            height (float, optional): The heightthe rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of the rectangle using width * height.

        Returns:
            float: The calculated area.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter the rectangle using 2 * (width + height).

        Returns:
            float: The calculated perimeter.
        """
        return abs(2 * (self.width + self.height))


def shape_info(obj):
    """Prints the area and perimeter a given shape object.

    Args:
        obj (Shape): An instance a class that inherits from Shape.
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
