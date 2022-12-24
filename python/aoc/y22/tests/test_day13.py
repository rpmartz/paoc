from unittest import TestCase

from python.aoc.y22.day13 import compare_packet


class TestDay13(TestCase):
    def test_comparing_two_unequal_numbers(self):
        self.assertTrue(compare_packet(4, 5) < 0)
        self.assertTrue(compare_packet(5, 4) > 0)
        self.assertEqual(0, compare_packet(5, 5))

    def test_comparing_list_and_number(self):
        self.assertEqual(0, compare_packet([4], 4))
        self.assertTrue(compare_packet([4], 5) < 0)
        self.assertTrue(compare_packet(5, [4]) > 0)

    def test_comparing_lists(self):
        self.assertTrue(compare_packet([9], [[8, 7, 6]]) > 0)
        self.assertTrue(compare_packet([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) < 0)
        self.assertTrue(compare_packet([7, 7, 7, 7], [7, 7, 7]) > 0)
        self.assertTrue(compare_packet([], [3]) < 0)
        self.assertTrue(compare_packet([[[]]], [[]]) > 0)
        self.assertTrue(compare_packet([1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) > 0)
