#!/usr/bin/python3
"""test_rectangle.py"""
import unittest
Base = __import__('base').Base



class TestBase(unittest.TestCase):

    def test_new_instance_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, b2.id)

    def test_specified_id(self):
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string_none(self):
        rjson = Base.to_json_string(None)
        self.assertEqual(rjson, '[]')

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, '[]')

        json_dictionary = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_dictionary, '[{"id": 12}]')


if __name__ == '__main__':
    unittest.main()
