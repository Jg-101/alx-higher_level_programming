#!/usr/bin/python3
# 7-base_geometry.py
"""Defs a base geometry class BaseGeometry."""


class BaseGeometry:
    """Rep base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an int.
        Args:
            name (str): The name of the parameter.
            val (int): The parameter to validate.
        Raises:
            TypeError: If val is not an int.
            ValueError: If val is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
