#!/usr/bin/python3
# 11-student.py
"""Defs a class Student."""


class Student:
    """Rep a student."""

    def __init__(self, first_name, last_name, age):
        """Init a new Student.
        Args:
            first_name (str): The first name of the student in prog.
            last_name (str): The last name of the student in prog.
            age (int): The age of the student in prog.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary rep of the Student."""
        return self.
