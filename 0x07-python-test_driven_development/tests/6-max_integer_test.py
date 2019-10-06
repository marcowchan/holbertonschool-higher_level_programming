#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer()"""
    def test_sorted_integers(self):
        """tests with list of sorted integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_rev_sorted_integers(self):
        """tests with list of reverse sorted integer"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_middle_max(self):
        """tests with list with max in the middle"""
        self.assertEqual(max_integer([3, 2, 5, 4, 1]), 5)

    def test_positive_integers(self):
        """tests with list of positive integers"""
        self.assertEqual(max_integer([1, 15]), 15)

    def test_one_integer(self):
        """tests with list of one integers"""
        self.assertEqual(max_integer([-1]), -1)

    def test_duplicate_integer(self):
        """tests with list of duplicate integers"""
        self.assertEqual(max_integer([55, 55]), 55)

    def test_empty_list(self):
        """tests with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_unmodified_list(self):
        """tests if the original list is unmodified"""
        test_list = [653, 2625, 34, -531, 0]
        test_copy = list(test_list)
        self.assertTrue(len(test_copy) == len(test_list))
        for i in range(len(test_copy)):
            self.assertTrue(test_copy[i] == test_list[i])
