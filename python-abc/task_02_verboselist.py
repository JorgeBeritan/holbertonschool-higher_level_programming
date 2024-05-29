#!/usr/bin/python3

class VerboseList(list):

    def __init__(self, lista):
        self.lista = lista
        self.element

    def append(self, element):
        return self.lista + self.element
    

vl = VerboseList([1, 2, 3, 4])
vl.append(4)