from itertools import combinations

from aoc.common.geometry import manhattan_distance


def parse_grid() -> dict:
    with open('data/day08.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    _grid = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            # filtering `.` out saves memory, but complicates downstream
            # logic because it requires a bounds check for antinode locations,
            # whereas including it makes bounds checking a simple `in` check
            _grid[(i, j)] = char

    return _grid

def is_on_board(p):
    i = p[0]
    j = p[1]

    return 0 <= i < 49 and 0 <= j < 49

grid = parse_grid()
antinodes = set()

frequency_locations = dict()
for coords, frequency in grid.items():
    if frequency != '.':
        locations = frequency_locations.get(frequency, set())
        locations.add(coords)
        frequency_locations[frequency] = locations


# now we have a data structure that groups the location of each antenna by frequency
for frequency, antenna_coordinates in frequency_locations.items():
    # we need all of the combinations of antennas for this frequency
    _combinations = combinations(antenna_coordinates, 2)
    for a, b in _combinations:
        man_dist = abs(a[0] - b[0]) + abs(a[1] - b[1])


# print(len(antinodes))

