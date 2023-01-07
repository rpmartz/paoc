from python.aoc.common.geometry import Point, manhattan_distance
from python.aoc.common.parsing import ints
from dataclasses import dataclass

@dataclass
class Pair:
    sensor: Point
    beacon: Point
    range: int


def get_input():
    with open('data/day15.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    return lines


def parse_lines(lines):
    pairs = []
    for line in lines:
        coordinates = ints(line)
        assert len(coordinates) == 4
        sensor = Point(coordinates[0], coordinates[1])
        beacon = Point(coordinates[2], coordinates[3])

        coverage_range = sensor.manhattan_distance_to(beacon)

        pairs.append(Pair(sensor, beacon, coverage_range))

    return pairs


def part_one():
    lines = get_input()
    pairs = parse_lines(lines)




if __name__ == '__main__':
    part_one()

 # 334399 too low
# 334400 too low
# 334402 too low
# 1642660 not correct
# 1642657 not correct
