#!/usr/bin/python3
"""Module for a verbose list that notifies users of changes."""


class VerboseList(list):
    """A custom list class that prints notifications on modifications.

    This class inherits from the built-in list and overrides methods that
    add or remove items to provide real-time feedback in the console.
    """

    def append(self, item):
        """Adds an item to the end of the list with a notification.

        Args:
            item: The object to be added to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extends the list by appending elements from the iterable.

        Args:
            items (iterable): The collection of items to add to the list.
        """
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Removes the first occurrence of an item with a notification.

        Args:
            item: The object to be removed from the list.

        Note:
            The notification is printed before the removal occurs.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Removes and returns an item at a given index with a notification.

        Args:
            index (int, optional): The index of the item to be removed.
                Defaults to -1 (the last item).

        Returns:
            The value of the popped item.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
