from aoc.common.geometry import Point, manhattan_distance
from aoc.common.parsing import ints


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


def get_test_input():
    return ['Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
            'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
            'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
            'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
            'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
            'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
            'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
            'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
            'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
            'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
            'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
            'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
            'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
            'Sensor at x=20, y=1: closest beacon is at x=15, y=3']


def parse_lines(lines):
    pairs = []
    for line in lines:
        coordinates = ints(line)
        assert len(coordinates) == 4
        sensor = Point(coordinates[0], coordinates[1])
        beacon = Point(coordinates[2], coordinates[3])

        coverage_range = sensor.manhattan_distance_to(beacon)

        pairs.append(Pair(sensor, beacon))

    return pairs


def part_one():
    lines = get_test_input()
    pairs = parse_lines(lines)

    pairs_in_range = set()
    Y = 2_000_000

    ranges = set()
    for pair in pairs:
        d = pair.distance()
        dy = abs(pair.sensor.y - Y)
        if dy > d:  # sensor cannot reach line we care about
            ranges.add(range(-1, -1))
        else:
            dx = d - dy  # "remaining range" of horizontal coverage on line
            ranges.add(range(pair.sensor.x - dx, pair.sensor.x + dx + 1))
            pairs_in_range.add(pair)

    range_union = set().union(*ranges)
    # x coordinates of any beacons on the y line
    y_beacon_locations = {pair.sensor.x for pair in pairs_in_range if pair.beacon.y == Y}

    answer = len(range_union) - len(y_beacon_locations)
    print(answer)

    # 4717629 - wrong
    # 4717628 - wrong


if __name__ == '__main__':
    part_one()

# 334399 too low
# 334400 too low
# 334402 too low
# 1642660 not correct
# 1642657 not correct
