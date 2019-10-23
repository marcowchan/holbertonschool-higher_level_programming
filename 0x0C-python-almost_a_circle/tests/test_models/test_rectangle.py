#!/usr/bin/python3
"""Unittest for the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Tests for the Rectangle class."""
    def setUp(self):
        """Initializes the __nb_objects attribute before each test."""
        Base._Base__nb_objects = 0

    def test_id_type(self):
        """Checks if the id is an integer type."""
        my_class = Rectangle(2, 3)
        self.assertIs(type(my_class.id), int)

    def test_id_increments(self):
        """Checks if the ids increment."""
        for i in range(1, 6):
            with self.subTest(i=i):
                my_class = Rectangle(3, 4)
                self.assertEqual(my_class.id, i)

    def test_sets_id(self):
        """Checks if the id can be set."""
        my_class = Rectangle(5, 6, 0, 0, 13)
        self.assertEqual(my_class.id, 13)

    def test_sets_id_increments(self):
        """Checks if the ids increment after setting an id."""
        for i in range(1, 10):
            with self.subTest(i=i):
                if i == 5:
                    my_class = Rectangle(7, 8, 0, 0, 13)
                    self.assertEqual(my_class.id, 13)
                else:
                    my_class = Rectangle(9, 10)
                    if i < 5:
                        self.assertEqual(my_class.id, i)
                    else:
                        self.assertEqual(my_class.id, i - 1)

    def test_sets_negative_id(self):
        """Checks if the id can be set with a negative integer."""
        my_class = Rectangle(11, 12, 0, 0, -7)
        self.assertEqual(my_class.id, -7)

    def test_gets_width(self):
        my_class = Rectangle(71, 98)
        self.assertEqual(my_class.width, 71)

    def test_gets_height(self):
        my_class = Rectangle(71, 98)
        self.assertEqual(my_class.height, 98)

    def test_gets_x(self):
        my_class = Rectangle(71, 98, 12)
        self.assertEqual(my_class.x, 12)

    def test_gets_y(self):
        my_class = Rectangle(71, 98, 12, 21)
        self.assertEqual(my_class.y, 21)

    def test_no_args(self):
        self.assertRaisesRegex(
            TypeError,
            "missing 2 required positional arguments: 'width' and 'height'",
            Rectangle
        )

    def test_one_args(self):
        self.assertRaisesRegex(
            TypeError,
            "missing 1 required positional argument: 'height'",
            Rectangle,
            17
        )

    def test_default_position_x(self):
        my_class = Rectangle(17, 12)
        self.assertEqual(my_class.x, 0)
        self.assertEqual(my_class.y, 0)

    def test_default_position_y(self):
        my_class = Rectangle(17, 12, 972)
        self.assertEqual(my_class.y, 0)

    def test_width_type(self):
        self.assertRaisesRegex(
            TypeError,
            "width must be an integer",
            Rectangle,
            [17], 13
        )
        self.assertRaisesRegex(
            TypeError,
            "width must be an integer",
            Rectangle,
            "17", 13
        )
        self.assertRaisesRegex(
            TypeError,
            "width must be an integer",
            Rectangle,
            (17,), 13
        )
        self.assertRaisesRegex(
            TypeError,
            "width must be an integer",
            Rectangle,
            {"width": 17}, 13
        )

    def test_height_type(self):
        self.assertRaisesRegex(
            TypeError,
            "height must be an integer",
            Rectangle,
            17, [13]
        )
        self.assertRaisesRegex(
            TypeError,
            "height must be an integer",
            Rectangle,
            17, "13"
        )
        self.assertRaisesRegex(
            TypeError,
            "height must be an integer",
            Rectangle,
            17, (13,)
        )
        self.assertRaisesRegex(
            TypeError,
            "height must be an integer",
            Rectangle,
            17, {"height": 13}
        )

    def test_width_value(self):
        self.assertRaisesRegex(
            ValueError,
            "width must be > 0",
            Rectangle,
            0, 13
        )
        self.assertRaisesRegex(
            ValueError,
            "width must be > 0",
            Rectangle,
            -17, 13
        )

    def test_height_value(self):
        self.assertRaisesRegex(
            ValueError,
            "height must be > 0",
            Rectangle,
            17, 0
        )
        self.assertRaisesRegex(
            ValueError,
            "height must be > 0",
            Rectangle,
            17, -13
        )

    def test_x_type(self):
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Rectangle,
            17, 13, [12]
        )
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Rectangle,
            17, 13, "12"
        )
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Rectangle,
            17, 13, (12,)
        )
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Rectangle,
            17, 13, {"x": 12}
        )

    def test_y_type(self):
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Rectangle,
            17, 13, 12, [16]
        )
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Rectangle,
            17, 13, 12, "16"
        )
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Rectangle,
            17, 13, 12, (16,)
        )
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Rectangle,
            17, 13, 12, {"y": 16}
        )

        def test_x_value(self):
            self.assertRaisesRegex(
                ValueError,
                "x must be > 0",
                Rectangle,
                17, 13, -12
            )

        def test_y_value(self):
            self.assertRaisesRegex(
                ValueError,
                "y must be > 0",
                Rectangle,
                17, 13, 12, -16
            )
