#!/usr/bin/python3
"""Is a Square Class
"""

class Square:
    """Represents a square.

Attributes:
size (int): The size of one side of the square.
position (tuple): The position of the square.

"""
    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position
    """Initializes a new square.

        Args:
            size (int): The size of one side of the square.
            position (tuple): The position of the square.

    """
    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size 
    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is negative.

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("ize must be >= 0")
        self.__size = value
    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position
    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If the position is not a tuple of two positive integers.

        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
    def my_print(self):
        """Prints the square using the `#` character with the offsets
        defined in the position.

        """
        if self.__size == 0:
            print("")
        
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print("_", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
