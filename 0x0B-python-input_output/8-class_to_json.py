"""Defs a Py class-to-JSON func."""


def class_to_json(obj):
    """Return the dictionary rep of a simple data struc."""
    return obj.__dict__
