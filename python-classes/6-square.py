#!/usr/bin/python3
"""
Class Square
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
    def position(self, position):
        """check error 
        """

        if type(position) is not tuple  or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) is not int or position[1]:
            raise("position must be a tuple of 2 positive integers")
        self.__position = position
    def my_print(self):
        """
        Print a square
        """
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")