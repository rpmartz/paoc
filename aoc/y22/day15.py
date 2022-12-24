from aoc.common.geometry import Point, manhattan_distance
from aoc.common.parsing import ints


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

        pairs.append((sensor, beacon))

    return pairs


def part_one():
    lines = get_input()
    pairs = parse_lines(lines)

    covered_locations = set()
    min_x = 10000000
    max_x = -10000000
    for pair in pairs:
        sensor = pair[0]
        beacon = pair[1]

        distance_to_closest_beacon = manhattan_distance(sensor, beacon)

        for x in range(sensor.x - distance_to_closest_beacon, sensor.x + distance_to_closest_beacon):

            max_x = max(max_x, x)
            min_x = min(min_x, x)

            for y in range(sensor.y - distance_to_closest_beacon, sensor.y + distance_to_closest_beacon):
                pt = Point(x, y)
                dist_to_beacon = manhattan_distance(sensor, pt)
                if dist_to_beacon <= distance_to_closest_beacon:
                    covered_locations.add(Point(x, y))

    # need min x and max x to determine length of row
    print(f'num covered locations: {len(covered_locations)}')


if __name__ == '__main__':
    part_one()
