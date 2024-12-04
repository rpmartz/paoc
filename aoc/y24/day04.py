
def read_puzzle():
    with open('data/day04.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    puzzle_grid = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            puzzle_grid[(i,j)] = char

    return puzzle_grid

print(read_puzzle())