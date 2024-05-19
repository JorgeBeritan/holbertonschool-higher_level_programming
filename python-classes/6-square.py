#!/usr/bin/python3
"""
Class Saquare
"""
class Square:
    """
    Definition of 'Square'
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instance of Size
        """
        self.size = size
        self.position = position
    def area(self):
        """
        Definition of public method 'area'
        """
        return self.__size ** 2
    @property
    def size(self):
        """
        get of __size
        Return: __size
        """
        return self.__size
    @size.setter
    def size(self, size):
        """
        Size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    @property
    def position(self):
        """
        get of poisition
        return position
        """
        return self.__position
    @position.setter
    def position(self, value):
        """check error 
        """

        if type(value) is not tuple  or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1]:
            raise("position must be a tuple of 2 positive integers")
        self.__position = value
    def my_print(self):
        """
        Print a square
        """
        if self.size:
            print("\n" * self.position[1], end="")
            print("\n".join([" " * self.position[0] + "#" * self.size] * self.size))
        else:
            print()