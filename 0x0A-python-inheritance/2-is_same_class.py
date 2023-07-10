#!/usr/bin/python3
# 2-is_same_class.py
"""Defs a class-checking func."""


def is_same_class(obj, a_class):
    """Check if an obj is exactly an instance of a given class.
    Args:
        object (any): The obj to check.
        a_class (type): The class to match the type of object to.
    Returns:
        If obj is exactly an instance of a_class - True.
        else - False.
    """
    if type(obj) == a_class:
        return True
    return False
