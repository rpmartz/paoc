
# Each antenna is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter, or digit

# In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

# initial approach
# * iterate over each antenna in straight and diagonal lines
# * when we find a match, then we can add an antinode in each direction using the manhattan distance

def parse_grid() -> dict:
    with open('data/day08.txt') as f:
        lines = [l.strip() for l in f.readlines()]

    grid = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != '.':
                antennas = grid.get(char, set())
                antennas.add((i, j))
                grid[char] = antennas

    return grid

def is_on_board(p):
    i = p[0]
    j = p[1]

    return 0 <= i < 49 and 0 <= j < 49

grid = parse_grid()
antinodes = set()

for antenna, matching_nodes in grid.items():
    print(f'{antenna}: {matching_nodes}')


# print(len(antinodes))

