#!/usr/bin/env python3
"""Module for Animal hierarchy using Abstract Base Classes."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing a generic animal.

    This class defines the interface that all subclasses must implement.
    """

    @abstractmethod
    def sound(self):
        """Returns the sound made by the animal.

        Returns:
            str: The sound representation (e.g., 'Bark').
        """
        ...


class Dog(Animal):
    """Represents a dog, inheriting from Animal."""

    def sound(self):
        """Provides the sound of a dog.

        Returns:
            str: The string 'Bark'.
        """
        return "Bark"


class Cat(Animal):
    """Represents a cat, inheriting from Animal."""

    def sound(self):
        """Provides the sound of a cat.

        Returns:
            str: The string 'Meow'.
        """
        return "Meow"
