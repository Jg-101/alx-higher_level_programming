#!/usr/bin/python3
# 1-my_list.py
"""Defs an inherited list class MyList in the program."""


class MyList(list):
    """Implements sorted printing for the built-in list class in the program."""

    def print_sorted(self):
        """Print a list in sorted ascending order in the program."""
        print(sorted(self))
