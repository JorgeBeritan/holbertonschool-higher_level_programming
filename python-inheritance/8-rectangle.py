#!/usr/bin/python3
"""Area class add
"""

class BaseGeometry:
    """A base Geometry
    """
    def __init__(self, width, height):
        """Constructo init
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        raise Exception("area() is not implemented")
