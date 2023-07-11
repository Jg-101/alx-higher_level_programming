#!/usr/bin/python3
# 8-load_from_json_file.py
"""Defs a JSON file-reading func."""
import json


def load_from_json_file(filename):
    """Create a Py obj from a JSON file."""
    with open(filename) as f:
        return json.load(f)
