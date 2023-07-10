#!/usr/bin/python3
# 0-lookup.py
"""Defs an obj attr lookup func."""


def lookup(obj):
    """Return a list of an obj's available attrs."""
    return (dir(obj))
