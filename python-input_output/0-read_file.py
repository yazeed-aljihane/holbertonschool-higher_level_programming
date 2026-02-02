#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    Returns:
        None: This function does not return any value.

    Note:
        The function uses a 'with' statement to ensure the file is properly 
        closed after reading, and it specifies 'utf-8' encoding to handle 
        various character sets correctly.
    """
    with open(filename, mode='r', encoding='utf-8') as my_file:
        print("{}".format(my_file.read()), end="")
