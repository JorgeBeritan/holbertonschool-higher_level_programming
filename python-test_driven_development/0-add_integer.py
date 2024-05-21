#!/usr/bin/python3
"""Is a function to add a and b
"""
def add_integer(a, b=98):


    """Add two integers.
    Return a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    # Convert to integer if a is float
    if type(a) is float:
        a = int(a)
    # Convert to integer if b is float
    if type(b) is float:
        b = int(b)

    return a + b
