#!/usr/bin/python3
# 101-locked_class.py
"""Def a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attrib
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
