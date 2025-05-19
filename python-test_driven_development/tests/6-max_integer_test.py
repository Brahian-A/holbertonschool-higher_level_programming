# tests/6-max_integer_test.py

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 5, 2]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.6, 3.1]), 3.1)

    def test_strings(self):
        self.assertEqual(max_integer("abcde"), "e")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

if __name__ == "__main__":
    unittest.main()
