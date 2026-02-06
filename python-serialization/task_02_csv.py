#!/usr/bin/env python3
"""Module for converting CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts data from a CSV file to a JSON format.

    Reads a CSV file, serializes its rows into a list of dictionaries,
    and writes the resulting JSON to 'data.json'.

    Args:
        csv_filename (str): The name of the source CSV file to read.

    Returns:
        bool: True if the conversion was successful, False if the file
              was not found.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as file:
            dic = csv.DictReader(file)
            lis = list(dic)
        with open('data.json', mode='w', encoding='utf-8') as file:
            json.dump(lis, file)
    except FileNotFoundError:
        return False
    return True
