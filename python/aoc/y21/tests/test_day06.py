import unittest

from python.aoc.y21.day_06 import process_day


class Day06Test(unittest.TestCase):

    def test_process_day_one(self):
        input = [3, 4, 3, 1, 2]

        process_day(fish_list=input)
        self.assertEqual([2, 3, 2, 0, 1], input)

        process_day(fish_list=input)
        self.assertEqual([1, 2, 1, 6, 0, 8], input)

        process_day(input)
        self.assertEqual([0, 1, 0, 5, 6, 7, 8], input)

        process_day(input)
        self.assertEqual([6, 0, 6, 4, 5, 6, 7, 8, 8], input)

    def test_eighty_days(self):
        input = [3, 4, 3, 1, 2]

        for x in range(0, 80):
            process_day(input)

        self.assertEqual(5934, len(input))
