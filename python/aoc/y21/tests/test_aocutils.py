import unittest

from aoc.y21.aocutils import Point, get_neighbors, read_numeric_grid


class AocUtilsTest(unittest.TestCase):

    def test_four_neighbors(self):
        point = Point(x=3, y=4)

        expected = {Point(3, 3), Point(3, 5), Point(2, 4), Point(4, 4)}
        actual = get_neighbors(point, 4)

        self.assertEqual(expected, actual)

    def test_eight_neighbors(self):
        point = Point(x=3, y=4)

        expected = {
            Point(3, 3), Point(3, 5), Point(2, 4), Point(4, 4),
            Point(2, 3), Point(2, 5), Point(4, 3), Point(4, 5)
        }

        actual = get_neighbors(point, num=8)
        self.assertEqual(expected, actual)

    def test_reading_grid(self):
        input = """\
        1163751742
        1381373672
        2136511328
        3694931569
        7463417111
        1319128137
        1359912421
        3125421639
        1293138521
        2311944581
        """

        grid = read_numeric_grid(input)

        self.assertEqual(1, grid[(0, 0)])
        self.assertEqual(2, grid[(0, 9)])
        self.assertEqual(2, grid[(9, 0)])
        self.assertEqual(8, grid[(9, 8)])
