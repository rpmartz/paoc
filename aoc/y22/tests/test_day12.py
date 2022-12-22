import unittest

from aoc.y22.day12 import parse_to_grid, Point


class Day12Test(unittest.TestCase):

    def test_parsing_test_grid(self):
        input_lines = ['Sabqponm', 'abcryxxl', 'accszExk', 'acctuvwj', 'abdefghi']

        puzzle = parse_to_grid(input_lines)
        self.assertEqual(Point(0, 0), puzzle.start)
        self.assertEqual(Point(2, 5), puzzle.end)
        self.assertEqual('m', puzzle.grid[Point(0, 7)])
        self.assertEqual('i', puzzle.grid[Point(4, 7)])
        self.assertEqual('a', puzzle.grid[Point(4, 0)])
