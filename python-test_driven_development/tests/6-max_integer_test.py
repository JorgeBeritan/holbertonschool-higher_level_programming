#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):


    def test_max_integer(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(lista), max(lista))


if __name__ == "__main__":
    unittest.main()
