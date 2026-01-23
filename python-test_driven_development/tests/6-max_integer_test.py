#!/usr/bin/python3
import unittest
max_int = __import__('6-max_integer').max_integer
class TestMax(unittest.TestCase):    
    def test_Max(self):
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int([13, 14, 56, 565]), 565)
        self.assertEqual(max_int([-1, 22, -45, 45]), 45)
        with self.assertRaises(TypeError):
            max_int(["er", 56, 556])
