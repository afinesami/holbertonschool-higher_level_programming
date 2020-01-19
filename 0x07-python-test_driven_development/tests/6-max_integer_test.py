#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Presence of docstrings"""

    def test_presence_of_module_docstring(self):
        test = __import__('6-max_integer').__doc__
        self.assertTrue(len(test) > 1)

    def test_presence_of_func_docstring(self):
        test = max_integer.__doc__
        self.assertTrue(len(test) > 1)

    """Working results"""
    def test_empty_list(self):
        test = []
        self.assertIsNone(max_integer(test))

    def test_no_arguments(self):
        self.assertIsNone(max_integer())

    def test_one_element(self):
        test = [1]
        self.assertEqual(max_integer(test), 1)

    def test_some_elements(self):
        test = [3425, 457458, 1, 3249056, -2346, 0]
        self.assertEqual(max_integer(test), 3249056)

    def test_floats(self):
        test = [23.2354, 635.34, 234658, 99, -102346.052]
        self.assertEqual(max_integer(test), 234658)

    def test_big_numbers(self):
        big = 1000000000000000000000000000000000000000000000000
        smal = -1000000000000000000000000000000000000000000000000
        test = [big, smal]
        self.assertEqual(max_integer(test), big)

    def test_pos_infinity(self):
        test = [1, 2, float('inf'), 9]
        self.assertEqual(max_integer(test), float('inf'))

    def test_neg_infinity(self):
        test = [1, 2, -float('inf'), 9]
        self.assertEqual(max_integer(test), 9)

    def test_custom_int_subclass(self):
        class ChildInt(int):
            pass
        big = ChildInt(456563723456365843)
        number = [1, 2, 3, big_child]
        self.assertEqual(max_integer(number), big)

    def test_boolean(self):
        '''test boolean
        '''
        self.assertEqual(max_integer([True, False]), True)

    """Catching exceptions"""
    def test_passing_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_passing_string(self):
        test = [2345, 2, "L0Lz", 9]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_passing_list(self):
        test = [2345, 2, [], 9]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_passing_list_one_int(self):
        test = [666, [1337], 99]
        with self.assertRaises(TypeError):
            max_integer(test)


if __name__ == "__main__":
    unittest.main()
