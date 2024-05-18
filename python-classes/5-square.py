#!/usr/bin/python3
"""Empty class 'Square'"""
class Square:
    """Definition of 'Square'"""
    def __init__(self, size=0):
        """Instance of Size"""
        self.__size = size
    def area(self):
        """Definition of public method 'area'"""
        return self.__size ** 2
    @property
    def size(self):
        """get of __size
        Return: __size
        """
        return self.__size
    @size.setter
    def size(self, size):
        """Size of square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def my_print(self):
        """Print a square
        """
        print("\n".join(["#" * self.size] * self.size))