from python.aoc.common.geometry import Point, manhattan_distance
from python.aoc.common.parsing import ints
from dataclasses import dataclass

@dataclass
class Pair:
    sensor: Point
    beacon: Point
    range: int


class Pair:

    def __init__(self, sensor, beacon):
        self.sensor = sensor
        self.beacon = beacon

    def distance(self):
        return manhattan_distance(self.sensor, self.beacon)


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

    pairs_in_range = set()

    for pair in pairs:
        distance_to_line = pair.sensor.manhattan_distance_to(Point(pair.sensor.x, 200000))

        if distance_to_line <= pair.range:
            pairs_in_range.add(pair)
            print(f'Sensor at {pair.sensor} is able to reach line')
        else:
            print(f'Sensor at {pair.sensor} NOT in range of line')




if __name__ == '__main__':
    part_one()

 # 334399 too low
# 334400 too low
# 334402 too low
# 1642660 not correct
# 1642657 not correct
