#!/usr/bin/python3
"""Is a function to add a and b

"""
def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of the two numbers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be a integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be a integer")
    # Convert to integer if a is float
    if type(a) is float:
        a = int(a)
     # Convert to integer if b is float
    if type(b) is float:
        b = int(b)
    return a + b
