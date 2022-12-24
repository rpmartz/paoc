import unittest

from python.aoc.y21.day_07 import find_best_alignment


class DaySeven(unittest.TestCase):

    def test_example_case(self):
        input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

        expected = 2, 37
        actual = find_best_alignment(input)
        self.assertEqual(expected, actual)
