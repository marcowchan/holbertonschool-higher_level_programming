#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
import json
from models.base import Base


class BaseTest(unittest.TestCase):
    """Tests for the Base class."""
    def setUp(self):
        """Initializes the __nb_objects attribute before each test."""
        self.assertIs(hasattr(Base, "_Base__nb_objects"), True)
        Base._Base__nb_objects = 0

    def test_id_type(self):
        """Checks if the id is an integer type."""
        my_class = Base()
        self.assertIs(type(my_class.id), int)

    def test_id_increments(self):
        """Checks if the ids increment."""
        for i in range(1, 6):
            with self.subTest(i=i):
                my_class = Base()
                self.assertEqual(my_class.id, i)

    def test_sets_id(self):
        """Checks if the id can be set."""
        my_class = Base(13)
        self.assertEqual(my_class.id, 13)

    def test_sets_id_increments(self):
        """Checks if the ids increment after setting an id."""
        for i in range(1, 10):
            with self.subTest(i=i):
                if i == 5:
                    my_class = Base(13)
                    self.assertEqual(my_class.id, 13)
                else:
                    my_class = Base()
                    if i < 5:
                        self.assertEqual(my_class.id, i)
                    else:
                        self.assertEqual(my_class.id, i - 1)

    def test_sets_negative_id(self):
        """Checks if the id can be set with a negative integer."""
        my_class = Base(-7)
        self.assertEqual(my_class.id, -7)

    def test_to_json(self):
        """Checks the json represntation."""
        input = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        expected = json.dumps(input)
        self.assertEqual(Base.to_json_string(input), expected)

    def test_to_json_empty(self):
        """Checks the json represntation with an empty list."""
        input = []
        expected = "[]"
        self.assertEqual(Base.to_json_string(input), expected)

    def test_to_json_none(self):
        """Checks the json represntation with None."""
        input = None
        expected = "[]"
        self.assertEqual(Base.to_json_string(input), expected)
