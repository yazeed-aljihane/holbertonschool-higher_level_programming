#!/usr/bin/python3
"""Module for file appending operations."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF-8).

    Args:
        filename (str): The name of the file to append to. an empty string.
        text (str): The string to be added to the file. an empty string.

    Returns:
        int: The number of characters added to the file.

    Note:
        The function uses the 'a' mode, which means it will create the file
        if it doesn't exist, and it will not overwrite existing content.
    """
    with open(filename, mode='a', encoding='utf-8') as my_file:
        return my_file.write(text)
