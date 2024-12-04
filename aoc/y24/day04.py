
def read_puzzle():
    with open('data/day04.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    puzzle_grid = []
    for line in lines:
        line_chars = []
        for char in line:
            line_chars.append(char)

        puzzle_grid.append(line_chars)

    return puzzle_grid

print(read_puzzle())