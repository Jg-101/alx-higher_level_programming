#!/usr/bin/python3
# 3-write_file.py
"""Defs a file-writing func."""


def write_file(filename="", text=""):
    """Write a str to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The num of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
