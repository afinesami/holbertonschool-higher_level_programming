#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Presence of docstrings"""

    def test_module_docstring(self):
        """Check: module docsting"""
        module = __import__('6-max_integer').__doc__
        self.assertTrue(len(module) > 1)

    def test_function_docstring(self):
        """Check: funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_no_args(self):
        """Check: no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Check: empty list []"""
        test = []
        self.assertIsNone(max_integer(test))

    def test_max_at_end(self):
        """Check: all positive max at end"""
        test = [12, 1, 18, 6, 14, 40]
        self.assertEqual(max_integer(test), 40)

    def test_two_of_max(self):
        """Check: max at end"""
        test = [12, 1, 40, 6, 14, 40]
        self.assertEqual(max_integer(test), 40)

    def test_none(self):
        """Check: passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Check: non integer type"""
        test = [1, "string", 3, 4, 5]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_one_element(self):
        """Check: only one number"""
        test_ele = [10]
        self.assertEqual(max_integer(test_ele), 10)

    def test_max_at_beginning(self):
        """Check: positive max at beginning"""
        test_pos = [130, 129, 23, 6, 0, 10]
        self.assertEqual(max_integer(test_pos), 130)

    def test_max_at_middle(self):
        """Check: max in middle"""
        test_max = [1, 10, 23, 30, 14, 12]
        self.assertEqual(max_integer(test_max), 30)

    def test_one_negative(self):
        """Check: negative number"""
        test = [10, -10, 1, 6, 4, 2]
        self.assertEqual(max_integer(test), 10)

    def test_all_10(self):
        """Check: all otems """
        test = [10, 10, 10, 10, 10, 10]
        self.assertEqual(max_integer(test), 10)

    def test_all_negative(self):
        """Check: all negative numbers"""
        test_neg = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(test_neg), -1)


if __name__ == "__main__":
    unittest.main()
