#!/usr/bin/python3
class Square:

    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size 
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("ize must be >= 0")
        self.__size = value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        return self.__size ** 2
    def my_print(self):
        if self.__size == 0:
            print("")
        
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print("_", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
