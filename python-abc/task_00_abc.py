#!/usr/bin/python3
"""Implement abstract class
"""


from abc import ABC, abstractmethod
"""Import module abs
"""


class Animal(ABC):
    """Abstract class
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        return "Bark"
    
class Cat(Animal):

    def sound(self):
        return "Meow"
