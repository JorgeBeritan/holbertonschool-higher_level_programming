#!/usr/bin/python3
"""A function to print a name and last name
"""


def say_my_name(first_name, last_name=""):
    """In function we implemtent case border threatment
    """

    if type(first_name) is not str:
        raise ValueError("first_name must be a string")
    if type(last_name) is not str:
        raise ValueError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
