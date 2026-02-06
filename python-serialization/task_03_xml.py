#!/usr/bin/env python3
"""XML Serialization Module.

This module provides basic utility functions to convert Python dictionaries
to XML files and vice versa. It uses the standard library's
xml.etree.ElementTree for processing.

The module supports simple key-value structures. Note that nested
dictionaries are not handled by these specific implementations and
all values are treated as strings during deserialization.

Attributes:
    None
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary into an XML file.

    Iterates through dictionary key-value pairs, creates XML sub-elements
    under a root 'data' tag, and writes the resulting tree to a file.

    Args:
        dictionary (dict): The dictionary containing data to be serialized.
        filename (str): The path where the XML file will be saved.

    Returns:
        None
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Parses an XML file and reconstructs it into a dictionary.

    Args:
        filename (str): The path to the XML file to be parsed.

    Returns:
        dict: A dictionary containing the data extracted from the XML.
              Note: All values will be returned as strings by default.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data_dict = {}

        for child in root:
            data_dict[child.tag] = child.text

        return data_dict
    except FileNotFoundError:
        return None
