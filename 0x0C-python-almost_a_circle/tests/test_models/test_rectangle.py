#!/usr/bin/python3
"""Unittest for the Rectangle class."""
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Tests for the Rectangle class."""
    def setUp(self):
        """Initializes __nb_objects."""
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
        """Checks getter for width."""
        my_class = Rectangle(71, 98)
        self.assertEqual(my_class.width, 71)

    def test_gets_height(self):
        """Checks getter for height."""
        my_class = Rectangle(71, 98)
        self.assertEqual(my_class.height, 98)

    def test_gets_x(self):
        """Checks getter for x."""
        my_class = Rectangle(71, 98, 12)
        self.assertEqual(my_class.x, 12)

    def test_gets_y(self):
        """Checks getter for y."""
        my_class = Rectangle(71, 98, 12, 21)
        self.assertEqual(my_class.y, 21)

    def test_no_args(self):
        """Checks for missing arguments exception."""
        self.assertRaisesRegex(
            TypeError,
            "missing 2 required positional arguments: 'width' and 'height'",
            Rectangle
        )

    def test_one_args(self):
        """Checks for missing argument exception."""
        self.assertRaisesRegex(
            TypeError,
            "missing 1 required positional argument: 'height'",
            Rectangle,
            17
        )

    def test_default_position_x(self):
        """Checks for default position attributes."""
        my_class = Rectangle(17, 12)
        self.assertEqual(my_class.x, 0)
        self.assertEqual(my_class.y, 0)

    def test_default_position_y(self):
        """Checks for default position attributes."""
        my_class = Rectangle(17, 12, 972)
        self.assertEqual(my_class.y, 0)

    def test_width_type(self):
        """Checks width type."""
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
        """Checks height type."""
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
        """Checks width value."""
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
        """Checks height value."""
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
        """Checks x type."""
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
        """Checks y type."""
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
        """Checks x value."""
        self.assertRaisesRegex(
            ValueError,
            "x must be >= 0",
            Rectangle,
            17, 13, -12
        )

    def test_y_value(self):
        """Checks y value."""
        self.assertRaisesRegex(
            ValueError,
            "y must be >= 0",
            Rectangle,
            17, 13, 12, -16
        )

    def test_area(self):
        """Checks area."""
        my_class = Rectangle(6, 5, 2, 16, 1)
        self.assertEqual(my_class.area(), 30)

    def test_display(self):
        """Checks display."""
        my_class = Rectangle(3, 4)
        expected = "###\n###\n###\n###\n"
        f = StringIO()
        with redirect_stdout(f):
            my_class.display()
        output = f.getvalue()
        self.assertEqual(output, expected)

    def test_str(self):
        """Checks string representation."""
        my_class = Rectangle(3, 4, 1, 2, 6)
        self.assertEqual(my_class.__str__(), "[Rectangle] (6) 1/2 - 3/4")

    def test_display_position(self):
        """Checks display with a non-zero coordinates."""
        my_class = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        f = StringIO()
        with redirect_stdout(f):
            my_class.display()
        output = f.getvalue()
        self.assertEqual(output, expected)

    def test_update_args(self):
        """Checks update with args."""
        my_class = Rectangle(2, 3, 1, 1, 6)
        my_class.update(12)
        self.assertEqual(my_class.id, 12)
        my_class.update(12, 12)
        self.assertEqual(my_class.width, 12)
        my_class.update(12, 12, 13)
        self.assertEqual(my_class.height, 13)
        my_class.update(12, 12, 13, 11)
        self.assertEqual(my_class.x, 11)
        my_class.update(12, 12, 13, 11, 11)
        self.assertEqual(my_class.y, 11)

    def test_update_kwargs(self):
        """Checks update with kwargs."""
        my_class = Rectangle(10, 10, 10, 10)
        my_class.update(height=1)
        self.assertEqual(my_class.height, 1)

        my_class.update(width=1, x=2)
        self.assertEqual(my_class.width, 1)
        self.assertEqual(my_class.x, 2)

        my_class.update(y=1, width=2, x=3, id=89)
        self.assertEqual(my_class.y, 1)
        self.assertEqual(my_class.width, 2)
        self.assertEqual(my_class.x, 3)
        self.assertEqual(my_class.id, 89)

        my_class.update(x=1, height=2, y=3, width=4)
        self.assertEqual(my_class.x, 1)
        self.assertEqual(my_class.height, 2)
        self.assertEqual(my_class.y, 3)
        self.assertEqual(my_class.width, 4)

    def test_dictionary(self):
        """Checks dictionary representation."""
        my_class = Rectangle(10, 2, 1, 9)
        expected = {'x': 1, 'height': 2, 'width': 10, 'y': 9, 'id': 1}
        self.assertEqual(my_class.to_dictionary(), expected)
