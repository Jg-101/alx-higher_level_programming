#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defs a class and inherited class-checking func."""


def is_kind_of_class(obj, a_class):
    """Check if an obj is an instance or inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If object is an instance or inherited instance of a_class - True.
        Else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
