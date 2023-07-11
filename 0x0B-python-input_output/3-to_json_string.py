#!/usr/bin/python3
# 5-to_json_string.py
"""Defs a string-to-JSON func."""
import json


def to_json_string(my_obj):
    """Return the JSON rep of a str obj."""
    return json.dumps(my_obj)
