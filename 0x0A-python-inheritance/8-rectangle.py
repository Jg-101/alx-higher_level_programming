#!/usr/bin/python3
# 8-rectangle.py
"""Def a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rep a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Init a new Rectangle.
        Args:
            width (int): The w of the new Rectangle.
            height (int): The h of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height 
