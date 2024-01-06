from python.aoc.common.parsing import ints

def get_instructions():
    with open('data/day06.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    instructions = []
    for line in lines:
         coords = ints(line)
         if 'off' in line:
             instructions.append(('off', (coords[0], coords[1]),(coords[2], coords[3])))
         elif 'on' in line:
             instructions.append(('on', (coords[0], coords[1]), (coords[2], coords[3])))
         else:
             instructions.append(('toggle', (coords[0], coords[1]), (coords[2], coords[3])))

    return instructions

def points_in_rectangle(p1, p2):
    start_x, end_x = min(p1[0], p2[0]), max(p1[0], p2[0])
    start_y, end_y = min(p1[1], p2[1]), max(p1[1], p2[1])

    return [(x, y) for x in range(start_x, end_x + 1) for y in range(start_y, end_y + 1)]

# todo could this be a defaaultdict?
def build_board():
    points = points_in_rectangle((0, 0), (999, 999))
    board = dict()
    for point in points:
        board[point] = 0

    return board


instructions = get_instructions()
board = build_board()

for instruction in instructions:
    rectangle = points_in_rectangle(instruction[1], instruction[2])

    action = instruction[0]
    if action == 'on':
        for point in rectangle:
            board[point] = board[point] + 1
    elif action == 'off':
        for point in rectangle:
            board[point] = max(0, board[point] - 1)
    else:
        for point in rectangle:
            board[point] = board[point] + 2

print(sum([v for v in board.values()]))