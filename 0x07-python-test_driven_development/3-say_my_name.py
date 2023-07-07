#!/usr/bin/python3
# 3-say_my_name.py
"""Def a name-printing func."""


def say_my_name(first_name, last_name=""):
    """Print a name.
    Args:
        first_name (str): The first name to print in prog.
        last_name (str): The last name to print in the prog.
    Raises:
        TypeError: If either of first_name or last_name are not strs.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
