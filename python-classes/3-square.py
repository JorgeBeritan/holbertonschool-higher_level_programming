#!/usr/bin/python3
"""Empty class 'Square'"""
class Square:
    """Definition of 'Square'"""
    def __init__(self, size=0):
        """Instance of Size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Definition of public method 'area'"""
        return self.__size ** 2