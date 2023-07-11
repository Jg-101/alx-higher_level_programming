#!/usr/bin/python3
# 7-save_to_json_file.py
"""Defs a JSON file-writing func."""
import json


def save_to_json_file(my_obj, filename):
    """Write an obj to a text file using JSON rep."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
