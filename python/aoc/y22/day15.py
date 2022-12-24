from python.aoc.common.geometry import Point, manhattan_distance
from python.aoc.common.parsing import ints


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
    min_x = 0
    max_x = -10000000

    radii = {}

    for pair in pairs:
        sensor = pair[0]
        beacon = pair[1]

        distance_to_closest_beacon = manhattan_distance(sensor, beacon)
        radii[sensor] = distance_to_closest_beacon

        min_x = min([min_x, sensor.x - distance_to_closest_beacon])
        max_x = max([max_x, sensor.x + distance_to_closest_beacon])

    num_checked = 0
    for x in range(min_x, max_x + 1):

        pt = Point(x, 2000000)
        num_checked += 1

        for pair in pairs:
            sensor = pair[0]
            dist_to_sensor = manhattan_distance(sensor, pt)

            if dist_to_sensor <= radii[sensor]:
                covered_locations.add(pt)
                break

    print(f'x range: {min_x} to {max_x}')
    # need min x and max x to determine length of row
    print(f'num covered locations: {len(covered_locations)}')
    print(f'num checked: {num_checked}')
    print(f'answer: {num_checked - len(covered_locations)}')
    # 334399 too low
    # 334400 too low
    # 334402 too low
    # 1642660 not correct
    # 1642657 not correct


if __name__ == '__main__':
    part_one()
