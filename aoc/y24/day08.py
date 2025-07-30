
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
                grid[(i, j)] = char

    return grid

def run_search_from_point(start, dx, dy, char):
    i = start[0]
    j = start[1]
    found = set()
    while 0 < i < 49 and 0 < j < 49:
        i = i + dx
        j = j + dy
        if (i, j) in grid and grid[(i, j)] == char:
            found.add((i, j))

    return found

def extend_diagonal(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    # Ensure it's a 45-degree diagonal
    if abs(dx) != abs(dy):
        raise ValueError("Points are not on a 45-degree diagonal.")

    # Unit direction vector
    step_x = int(dx / abs(dx))
    step_y = int(dy / abs(dy))

    # Manhattan distance
    manhattan_dist = abs(dx) + abs(dy)

    # Extend
    before_p1 = (x1 - step_x * manhattan_dist, y1 - step_y * manhattan_dist)
    after_p2  = (x2 + step_x * manhattan_dist, y2 + step_y * manhattan_dist)

    return before_p1, after_p2

def is_on_board(p):
    i = p[0]
    j = p[1]

    return 0 <= i < 49 and 0 <= j < 49

grid = parse_grid()
antinodes = set()

for antenna, value in grid.items():
    # horizontal
    matches = run_search_from_point(antenna, 1, 0, value)
    matches = matches | run_search_from_point(antenna, -1, 0, value)

    # vertical
    matches = matches | run_search_from_point(antenna, 0, 1, value)
    matches = matches | run_search_from_point(antenna, 0, -1, value)

    # upwards right
    matches = matches | run_search_from_point(antenna, 1, -1, value)
    # downwards left
    matches = matches | run_search_from_point(antenna, -1, 1, value)
    # upwards left
    matches = matches | run_search_from_point(antenna, -1, -1, value)
    # downwards right
    matches = matches | run_search_from_point(antenna, 1, 1, value)

    for match in matches:
        anode_1, anode_2 = extend_diagonal(match, antenna)
        if is_on_board(anode_1):
            antinodes.add(anode_1)
        if is_on_board(anode_2):
            antinodes.add(anode_2)


print(len(antinodes))

