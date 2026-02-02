#!/usr/bin/python3
"""Module for file writing operations."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to an empty string.
        text (str): The string to be written to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.

    Note:
        This function uses the 'with' statement to ensure the file is closed 
        after writing. It will overwrite the file if it already exists or 
        create it if it does not.
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        return my_file.write(text)
