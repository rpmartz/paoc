from itertools import combinations
from typing import Tuple


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

def mul_pt(pt, k) -> Tuple[int, int]:
    """Performs scalar multiplication of a point"""
    return pt[0] * k, pt[1] * k

def sub_pt(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    """subtraction of two points"""
    return a[0] - b[0], a[1] - b[1]


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
        # antinodes only if one is 2x distance, so at 2a - b and 2b - a
        anode_1 = sub_pt(mul_pt(a, 2), b)
        anode_2 = sub_pt(mul_pt(b, 2), a)

        if anode_1 in grid:
            antinodes.add(anode_1)
        if anode_2 in grid:
            antinodes.add(anode_2)


print(len(antinodes))

