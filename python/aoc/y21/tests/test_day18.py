from unittest import TestCase

from python.aoc.y21.day_18 import add, magnitude, split


class TestDay18(TestCase):

    def test_addition(self):
        left = eval('[1, 2]')
        right = eval('[[3,4],5]')
        expected = eval('[[1,2],[[3,4],5]]')
        self.assertEqual(expected, add(left, right))

        left = eval('[[[[4,3],4],4],[7,[[8,4],9]]]')
        right = eval('[1,1]')
        expected = eval('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
        self.assertEqual(expected, add(left, right))

    def test_magnitude(self):
        cases = [
            ('[[1, 2], [[3, 4], 5]]', 143),
            ('[[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]', 1384),
            ('[[[[1, 1], [2, 2]], [3, 3]], [4, 4]]', 445),
            ('[[[[3, 0], [5, 3]], [4, 4]], [5, 5]]', 791),
            ('[[[[5, 0], [7, 4]], [5, 5]], [6, 6]]', 1137),
            ('[[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]', 3488),
        ]

        for case in cases:
            sfish_num = eval(case[0])
            calculated_magnitude = magnitude(sfish_num)
            self.assertEqual(case[1], calculated_magnitude)

    def test_split(self):
        self.assertEqual([5, 5], split(10))
        self.assertEqual([5, 6], split(11))
        self.assertEqual([6, 6], split(12))
        self.assertEqual([6, 7], split(13))

