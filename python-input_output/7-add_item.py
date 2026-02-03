#!/usr/bin/python3
"""A script that adds all arguments to a Python list and saves them to a file.

This script loads a list from a JSON file, appends any command-line arguments
provided to that list, and then saves the updated list back to the file.
If the file does not exist, it starts with an empty list.
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
files = 'add_item.json'

try:
    my_list = load_from_json_file(files)
except (FileNotFoundError, ValueError):
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, files)
