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


def get_neighbors(point: Point) -> set[Point]:
    return {
        Point(point.x + 1, point.y),
        Point(point.x - 1, point.y),
        Point(point.x, point.y + 1),
        Point(point.x, point.y - 1)
    }


def get_elevation(letter):
    if letter == 'S':
        return 1
    elif letter == 'E':
        return 26

    return '#abcdefghijklmnopqrstuvwxyz'.index(letter)


def solve(puzzle: Puzzle):
    # do bfs, where each "level" is a move
    visited = set()
    queue = []

    visited.add(puzzle.start)
    start_depth = 0
    queue.append((puzzle.start, start_depth))

    while queue:
        current_position, depth = queue.pop(0)
        current_elevation = get_elevation(puzzle.grid[current_position])

        cardinal_neighbors = [n for n in get_neighbors(current_position) if n in puzzle.grid.keys()]
        eligible_neighbors = set()
        for n in cardinal_neighbors:
            n_elevation = get_elevation(puzzle.grid[n])
            if n_elevation < current_elevation or abs(current_elevation - n_elevation) <= 1:
                eligible_neighbors.add(n)

        for neighbor in eligible_neighbors:
            if neighbor not in visited:
                if neighbor == puzzle.end:
                    return depth + 1

                visited.add(neighbor)
                queue.append((neighbor, depth + 1))

    return None


def parse_to_grid(lines):
    grid = {}
    start = None
    end = None
    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            point = Point(i, j)
            grid[point] = letter
            if letter == 'S':
                start = point
                grid[point] = 'a'
            elif letter == 'E':
                end = point
                grid[point] = 'z'
            else:
                grid[point] = letter

    assert start != None
    assert end != None

    return Puzzle(start=start, end=end, grid=grid)


def part_1():
    lines = read_input()
    puzzle = parse_to_grid(lines)
    moves = solve(puzzle)

    return moves


def part_2():
    lines = read_input()
    puzzle = parse_to_grid(lines)
    trail_lengths = []

    for location, elevation in puzzle.grid.items():
        if elevation == 'a':
            trail_length = solve(Puzzle(start=location, end=puzzle.end, grid=puzzle.grid))
            if trail_length:
                trail_lengths.append(trail_length)

    return min(trail_lengths)


if __name__ == '__main__':
    print(f'Part 1: {part_1()}')
    print(f'Part 2: {part_2()}')
