#!/usr/bin/python3
# 12-student.py
"""Defs a class Student."""


class Student:
    """Rep a student."""

    def __init__(self, first_name, last_name, age):
        """Init a new Student.
        Args:
            first_name (str): The first name of the student in the prog.
            last_name (str): The last name of the student in the prog.
            age (int): The age of the student in the prog.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary rep of the Student.
        If attrs is a list of strs, reps only those attrs
        included in the list.
        Args:
            attrs (list): (Optional) The attrs to rep.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
