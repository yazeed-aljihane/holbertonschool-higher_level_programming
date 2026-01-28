#!/usr/bin/env python3

class SwimMixin:
    """Provides swimming behavior to a class.

    This mixin is intended to be used with classes that require
    aquatic movement capabilities.

    Attributes:
        None
    """

    def swim(self):
        """Prints a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying behavior to a class.

    This mixin is intended to be used with classes that require
    aerial movement capabilities.

    Attributes:
        None
    """

    def fly(self):
        """Prints a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a dragon with multiple capabilities.

    A Dragon is a complex entity that inherits movement behaviors
    from both SwimMixin and FlyMixin, while adding its own
    unique actions.

    Attributes:
        None
    """

    def roar(self):
        """Prints a message indicating the dragon is roaring."""
        print("The dragon roars!")
