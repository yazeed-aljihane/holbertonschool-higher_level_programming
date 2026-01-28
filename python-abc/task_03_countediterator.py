#!/usr/bin/python3

class CountedIterator:
    """A wrapper class for iterator that keeps of the number of items iterated.

    Attributes:
        iterable (iterator): The iterator object initialized from the input.
        count (int): The number items that have been fetched from the iterator.
    """

    def __init__(self, iterable):
        """Initializes CountedIterator with an iterable and a counter.

        Args:
            iterable (iterable): The collection or stream to be iterated over.
        """
        self.iterable = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current count of items iterated.

        Returns:
            int: The total number of items retrieved so far.
        """
        return self.count

    def __next__(self):
        """Fetches the next item from the iterator and increments the counter.

        Returns:
            any: The next item from the original iterator.

        Raises:
            StopIteration: When there are no more items to iterate.
        """
        item = next(self.iterable)
        self.count += 1
        return item
