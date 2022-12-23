from unittest import TestCase

from aoc.y22.day13 import compare_packet


class TestDay13(TestCase):
    def test_comparing_two_unequal_numbers(self):
        self.assertTrue(compare_packet(4, 5) < 0)
        self.assertTrue(compare_packet(5, 4) > 0)
        self.assertEqual(0, compare_packet(5, 5))
