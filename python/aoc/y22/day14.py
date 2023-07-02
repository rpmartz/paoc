

def read_input():
    with open('data/day14.txt', 'r') as ifile:
        lines = [line.strip() for line in ifile.readlines()]

    return lines

def parse_line(line):
    points = [p.strip() for p in line.split('->')]
    return points


lines = read_input()
for line in lines:
    points = list(map(text_to_numeric, parse_line(line)))
    add_rocks_to_board(points)

print(BOARD)

