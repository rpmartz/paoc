from itertools import combinations

def parse_grid() -> dict:
    with open('data/day08.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    _grid = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.':
                antennas = _grid.get(char, set())
                antennas.add((i, j))
                _grid[char] = antennas

    return _grid

def is_on_board(p):
    i = p[0]
    j = p[1]

    return 0 <= i < 49 and 0 <= j < 49

grid = parse_grid()
antinodes = set()

# now we have a data structure that groups the location of each antenna by frequency
for frequency, antenna_coordinates in grid.items():
    # we need all of the combinations of antennas for this frequency
    _combinations = combinations(antenna_coordinates, 2)
    for a, b in _combinations:
        print(f'{frequency} -> {a} -> {b}')


# print(len(antinodes))

