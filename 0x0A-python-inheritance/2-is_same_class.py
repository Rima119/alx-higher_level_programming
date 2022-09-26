#!/usr/bin/python3
"""is_same_class"""


def is_same_class(obj, a_class):
    """function that returns True if the object
    is exactly an instance of the specified class; otherwise False
    Args:
        obj: an abject
        a_class: a class
    """
    return type(obj) == a_class
