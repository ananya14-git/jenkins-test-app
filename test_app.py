#!/usr/bin/env python3
"""
Unit tests for the Jenkins test application
"""
import unittest
from app import add, multiply

class TestAppFunctions(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
