import unittest

from day_09 import *

board = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
]


class DayNineTest(unittest.TestCase):

    def test_find_low_points_from_sample_board(self):
        low_points = find_low_points(board)
        expected = [(0, 1, 1), (0, 9, 0), (2, 2, 5), (4, 6, 5)]
        self.assertEqual(low_points, expected)

    def test_summing_risk_score(self):
        low_points = [(0, 1, 1), (0, 9, 0), (2, 2, 5), (4, 6, 5)]
        self.assertEqual(15, calculate_risk_level(low_points))

    def test_finding_neighbors(self):
        x, y = 0, 1

        expected = [(0, 0), (0, 2), (1, 1)]
        actual = get_coordinates_of_neighbors(x, y, board)
        self.assertEqual(set(expected), set(actual))

        x, y = 0, 9
        expected = [(0, 8), (1, 9)]
        actual = get_coordinates_of_neighbors(x, y, board)
        self.assertEqual(set(expected), set(actual))

        x, y = 2, 2
        expected = [(2, 1), (2, 3), (1, 2), (3, 2)]
        actual = get_coordinates_of_neighbors(x, y, board)
        self.assertEqual(set(expected), set(actual))

    def test_finding_basins(self):
        low_points = find_low_points(board)
        expected = [3, 9, 14, 9]
        actual = find_basin_sizes(low_points, board)

        self.assertEqual(expected, actual)
