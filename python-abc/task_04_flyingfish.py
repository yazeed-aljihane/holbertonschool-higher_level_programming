#!/usr/bin/python3

class Fish:
    """Represents a generic fish with basic aquatic behaviors.

    Attributes:
        None
    """

    def swim(self):
        """Prints the swimming action of the fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the natural habitat of the fish."""
        print('The fish lives in water')


class Bird:
    """Represents a generic bird with basic aerial behaviors.

    Attributes:
        None
    """

    def fly(self):
        """Prints the flying action of the bird."""
        print('The bird is flying')

    def habitat(self):
        """Prints the natural habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish, inheriting from both Fish and Bird.

    This class demonstrates multiple inheritance where the flying fish
    overrides methods to reflect its unique dual-environment capabilities.

    Attributes:
        None
    """

    def fly(self):
        """Prints the unique soaring action of the flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints the unique swimming action of the flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints the dual habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
