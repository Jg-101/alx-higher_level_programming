#!/usr/bin/python3
# 0-read_file.py
"""Defs a text file-reading func."""


def read_file(filename=""):
    """Print the conts of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
