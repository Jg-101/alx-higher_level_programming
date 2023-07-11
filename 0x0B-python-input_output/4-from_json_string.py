#!/usr/bin/python3
# 6-from_json_string.py
"""Defs a JSON-to-obj func."""
import json


def from_json_string(my_str):
    """Return the Python object rep of a JSON str."""
    return json.loads(my_str)
