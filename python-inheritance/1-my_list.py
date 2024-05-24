#!/usr/bin/python3
"""Descripcion of class MyList
"""


class MyList(list):
    """In this class we can sort a list of integer number
    """

    def print_sorted(self):
        list = self[:]
        print(sorted(list))
