#!/usr/bin/python3
# 100-my_int.py
"""Defs a class MyInt that inherits from integer."""


class MyInt(int):
    """Invert int operators == and != in the prog."""

    def __eq__(self, value):
        """Override == operator with != behavior in the prog."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior in the prog."""
        return self.real == value
