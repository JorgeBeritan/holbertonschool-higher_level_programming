#!/usr/bin/python3
"""by me
"""


class Student:
    """In this we return a method descrition for JSON serialization
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """In this function we learn how return description
        dictionary for JSON serialization
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: self.__dict__[attr] for attr in self.__dict__.keys() & attrs}

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__setattr__(key, value)