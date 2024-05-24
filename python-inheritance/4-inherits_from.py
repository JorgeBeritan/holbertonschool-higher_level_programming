#!/usr/bin/python3
"""In this function we se a subsclass
"""


def inherits_from(obj, a_class):
    """With this function we see a subclass directly or indirectly
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
