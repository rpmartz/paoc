from collections import namedtuple
from collections.abc import Mapping
from dataclasses import dataclass

# todo namedtuple vs dataclass
Point = namedtuple('Point', 'x, y')


@dataclass
class Puzzle:
    start: Point
    end: Point
    grid: Mapping[Point, str]


def read_input():
    with open('data/day12.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


def get_elevation(letter):
    '#abcdefghijklmnopqrstuvwxyz'.index(letter)


def parse_to_grid(lines):
    grid = {}
    start = None
    end = None
    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            point = Point(i, j)
            if letter == 'S':
                start = point
            elif letter == 'E':
                end = point
            else:
                grid[point] = letter

    assert start != None
    assert end != None

    return Puzzle(start=start, end=end, grid=grid)

# print(read_input())
# print(parse_to_grid(read_input()))
