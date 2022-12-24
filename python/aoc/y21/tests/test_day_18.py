from unittest import TestCase

from python.aoc.y21.day_18 import calculate_magnitude


class Test(TestCase):

    def test_exaple_calculate_magnitude(self):
        snailfish_num = '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
        calculated_magnitude = calculate_magnitude(snailfish_num)

        expected = 4140
        self.assertEqual(expected, calculated_magnitude)
