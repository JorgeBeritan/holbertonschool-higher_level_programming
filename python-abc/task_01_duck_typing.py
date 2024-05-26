#!/usr/bin/python3
"""Implementation Abstract class with geomtry
"""


from abc import ABC, abstractmethod
from math import pi as pi
"""import abc and abstractmethod and pi
"""


class Shape(ABC):
    """Abstract class of shape of geometry
    """
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    """Class circle inherit Shape Class
    """
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise AssertionError("Perimeter should handle negative radius")

    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius
    
class Rectangle(Shape):
    """Class Rectangle inherit Shape Class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
def shape_info(clase):
    """Function to print area and perimeter of Shape
    """
    print("Area:", clase.area())
    print("Perimeter:", clase.perimeter())
