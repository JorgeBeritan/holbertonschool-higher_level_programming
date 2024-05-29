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

    def to_json(self):
        """In this function we learn how return description
        dictionary for JSON serialization
        """
        json_dict = {}
        for key, value in self.__dict__.items():
            json_dict[key] = value
        return json_dict
