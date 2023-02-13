#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from models.base import Base


class TestMaxInteger(unittest.TestCase):
    def test_id_generation(self):
        # Test id generation for instances without an id
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_id_assignment(self):
        # Test id assignment for instances with an id
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base(42)
        self.assertEqual(b5.id, 42)


if __name__ == '__main__':
    unittest.main()
