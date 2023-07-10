#!/usr/bin/python3
# 4-inherits_from.py
"""Defs an inherited class-checking func."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of object to.
    Returns:
        If object is an inherited instance of a_class - True.
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
