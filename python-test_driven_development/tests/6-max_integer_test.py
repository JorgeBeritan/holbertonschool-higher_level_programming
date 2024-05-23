#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):


    def test_max_integer(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(lista), max(lista))
    
    def test_max_integer_beginning(self):
        lista = [7, 1, 3, 4, 5, 6]
        self.assertEqual(max_integer(lista), max(lista))
    
    def test_max_integer_middle(self):
        lista = [1, 2, 3, 7, 5, 6]
        self.assertEqual(max_integer(lista), max(lista))
    def test_max_integer_negative(self):
        lista = [1, 2, 3, -50, 68, -2]
        self.assertEqual(max_integer(lista), max(lista))
    def test_max_integer_negative_only(self):
        lista = [-1, -2, -3, -100, -2]
        self.assertEqual(max_integer(lista), max(lista))
    def test_max_intger_one_argument(self):
        lista = [1]
        self.assertEqual(max_integer(lista), max(lista))
    def test_max_integer_empty(self):
        lista = []
        self.assertEqual(max_integer(lista), None)

if __name__ == "__main__":
    unittest.main()
