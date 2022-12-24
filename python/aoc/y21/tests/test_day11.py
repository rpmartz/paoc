import copy
import unittest

from day_11 import *


def get_board():
    board = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]
    ]

    return copy.deepcopy(board)


class DayEleven(unittest.TestCase):

    def test_example(self):
        expected_after_10 = 204
        actual_after_10 = count_num_flashes(get_board(), 10)
        self.assertEqual(expected_after_10, actual_after_10)

        expected = 1656
        actual = count_num_flashes(get_board(), 100)

        self.assertEqual(expected, actual)

    def test_sub_example(self):
        subsample_board = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1]
        ]

        flashes = count_num_flashes(subsample_board, 2)
        self.assertEqual(9, flashes)

    def test_get_neighbors(self):
        i = 4
        j = 5

        expected = {
            (3, 5), (5, 5), (4, 4), (4, 6), (3, 4), (3, 6),
            (5, 4), (5, 6)
        }
        actual = get_neighbors(i, j)
        self.assertEqual(expected, actual)
