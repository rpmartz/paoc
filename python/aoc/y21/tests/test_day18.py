from unittest import TestCase

from python.aoc.y21.day_18 import add


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















