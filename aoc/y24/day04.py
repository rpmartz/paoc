

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

def generate_offsets(i, j):
    directions = [
        # horizontal right
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        # horizontal left
        [(0, 0), (0, -1), (0, -2), (0, -3)],
        # vertical down
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        # vertical up
        [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
        # diagonal upward right
        [(0, 0), (1, -1), (2, -2), (3, -3)],
        # diagonal downward right
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        # diagonal upward left
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
        # diagonal downward left
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
    ]

    offset_coords = []
    for direction in directions:
        offset_coords.append([(i + di, j + dj) for di, dj in direction])
    return offset_coords



def search_grid(i, j, grid) -> int:
    offset_coords = generate_offsets(i, j)
    num_ways_to_spell = 0

    for group in offset_coords:
        chars = []
        for coord in group:
            chars.append(grid.get(coord, '#')) # let '#' denote off board

        if ''.join(chars) == 'XMAS':
            num_ways_to_spell += 1


    return num_ways_to_spell

def search_grid_x_mas(i, j, grid) -> int:

    if grid[(i,j)] != 'A':
        return 0

    left_diag_offsets = [(-1, -1), (0, 0), (1, 1)]
    right_diag_offsets = [(1, -1), (0, 0), (-1, 1)]

    left_diag_chars = []
    for di, dj in left_diag_offsets:
        left_diag_chars.append(grid.get((i + di, j + dj), '#'))

    right_diag_chars = []
    for di, dj in right_diag_offsets:
        right_diag_chars.append(grid.get((i + di, j + dj), '#'))

    if ''.join(left_diag_chars) in {'MAS', 'SAM'} and ''.join(right_diag_chars) in {'MAS', 'SAM'}:
        return 1


    return 0



grid, depth, width = read_puzzle()

total_appearances = 0
xmas_appearances = 0
for i in range(depth + 1):
    for j in range(width + 1):
        total_appearances += search_grid(i, j, grid)
        xmas_appearances += search_grid_x_mas(i, j, grid)

print(total_appearances)
print(xmas_appearances)