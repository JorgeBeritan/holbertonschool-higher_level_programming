#!/usr/bin/python3


import pickle

class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        with open(filename, "wb") as archive:
            pickle.dump(self.name, archive)
            pickle.dump(self.age, archive)
            pickle.dump(self.is_student, archive)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as archive:
            name = pickle.load(archive)
            age = pickle.load(archive)
            is_student = pickle.load(archive)
        return cls(name, age, is_student)
