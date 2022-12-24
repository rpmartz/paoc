import unittest

from python.aoc.y22.day12 import parse_to_grid, get_elevation, Point, solve


class Day12Test(unittest.TestCase):

    def parse_test_input(self):
        input_lines = ['Sabqponm', 'abcryxxl', 'accszExk', 'acctuvwj', 'abdefghi']
        puzzle = parse_to_grid(input_lines)

        return puzzle

    def test_parsing_test_grid(self):
        puzzle = self.parse_test_input()
        self.assertEqual(Point(0, 0), puzzle.start)
        self.assertEqual(Point(2, 5), puzzle.end)
        self.assertEqual('m', puzzle.grid[Point(0, 7)])
        self.assertEqual('i', puzzle.grid[Point(4, 7)])
        self.assertEqual('a', puzzle.grid[Point(4, 0)])

    def test_getting_elevation(self):
        self.assertEqual(1, get_elevation('a'))
        self.assertEqual(1, get_elevation('S'))
        self.assertEqual(26, get_elevation('z'))
        self.assertEqual(26, get_elevation('E'))

    def test_solving_example(self):
        puzzle = self.parse_test_input()
        self.assertEqual(31, solve(puzzle))
