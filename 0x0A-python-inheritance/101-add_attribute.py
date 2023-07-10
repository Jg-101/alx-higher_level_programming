#!/usr/bin/python3
# 101-add_attribute.py
"""Defs a func that adds attrs to objs."""


def add_attribute(obj, att, value):
    """Add a new attr to an obj if possible.
    Args:
        obj (any): The obj to add an att to.
        att (str): The name of the att to add to object.
        val (any): The val of att.
    Raises:
        TypeError: If the attr cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
