from typing import List

from python.aoc.common.geometry import Point

ROCK = '#'
SAND = 'o'
BOARD = {}

def read_input():
    with open('data/day14.txt', 'r') as ifile:
        lines = [line.strip() for line in ifile.readlines()]

    return lines

def parse_line(line):
    points = [p.strip() for p in line.split('->')]
    return points

def text_to_numeric(point):
    res = point.split(',')
    return Point(int(res[0]), int(res[1]))

def add_rocks_to_board(points: List[Point]):
    for p1, p2  in zip(points, points[1:]):
        points_between = p1.points_between(p2)
        for point in points_between:
            BOARD[point] = ROCK


lines = read_input()
for line in lines:
    points = list(map(text_to_numeric, parse_line(line)))
    add_rocks_to_board(points)

print(BOARD)

