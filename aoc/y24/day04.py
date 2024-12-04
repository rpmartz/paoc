

def read_puzzle():
    with open('data/day04.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    puzzle_grid = {}
    puzzle_depth = 0
    puzzle_width = 0
    for i, line in enumerate(lines):
        puzzle_depth = max(puzzle_depth, i)
        for j, char in enumerate(line):
            puzzle_width = max(puzzle_width, j)
            puzzle_grid[(i,j)] = char

    return puzzle_grid, puzzle_depth, puzzle_width


def search_grid(i, j, grid) -> int:
    offset_coords = []
    num_ways_to_spell = 0

    # forwards same line
    offset_coords.append([(i, j), (i, j + 1), (i, j + 2), (i, j + 3)])

    # backwards same line
    offset_coords.append([(i, j), (i, j - 1), (i, j - 2), (i, j - 3)])

    # vertical downwards
    offset_coords.append([(i, j), (i + 1, j), (i + 2, j), (i + 3, j)])

    # vertical upwards
    offset_coords.append([(i, j), (i - 1, j), (i - 2, j), (i - 3, j)])

    # diagonal upwards right
    offset_coords.append([(i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)])

    # diagonal downward right
    offset_coords.append([(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)])

    # diagonal upward left
    offset_coords.append([(i, j), (i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3)])

    # diagonal downward left
    offset_coords.append([(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)])

    for group in offset_coords:
        chars = []
        for coord in group:
            chars.append(grid.get(coord, '#')) # let '#' denote off board

        if ''.join(chars) == 'XMAS':
            num_ways_to_spell += 1


    return num_ways_to_spell



grid, depth, width = read_puzzle()

total_appearances = 0
for i in range(depth):
    for j in range(width):
        total_appearances += search_grid(i, j, grid)

print(total_appearances)