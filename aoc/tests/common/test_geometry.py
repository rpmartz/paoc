from aoc.common.geometry import points_between_inclusive

import unittest

class TestPointsBetween(unittest.TestCase):

    def test_vertical_line_increasing_y(self):
        p1 = (0, 0)
        p2 = (0, 5)

        expected = [(0, i) for i in range(6)]

        self.assertEqual(expected, points_between_inclusive(p1, p2))

    def test_horizontal_line_increasing_x(self):
        p1 = (0, 0)
        p2 = (0, 5)

        expected = [(0, i) for i in range(6)]

        self.assertEqual(expected, points_between_inclusive(p1, p2))

    def test_vertical_line_decreasing_y(self):
        p1 = (0, 0)
        p2 = (0, -5)

        expected = [(0, i) for i in range(0, -6, -1)]

        self.assertEqual(expected, points_between_inclusive(p1, p2))

    def test_horizontal_line_decreasing_x(self):
        p1 = (0, 0)
        p2 = (-5, 0)

        expected = [(i, 0) for i in range(0, -6, -1)]

        self.assertEqual(expected, points_between_inclusive(p1, p2))
