from typing import List


def read_board():
    with open('data/day09.txt', 'r') as f:
        board = []
        for line in f.readlines():
            board.append([int(num) for num in line.strip()])

    return board


def find_low_points(board):
    board_depth = len(board) - 1
    board_width = len(board[0]) - 1

    low_points = []
    for i, row in enumerate(board):
        for j, _ in enumerate(row):

            lt_left = (j - 1 < 0) or row[j] < row[j - 1]
            lt_right = (j + 1 > board_width) or row[j] < row[j + 1]
            lt_bottom = (i + 1 > board_depth) or row[j] < board[i + 1][j]
            lt_top = (i - 1 < 0) or row[j] < board[i - 1][j]

            if all([lt_left, lt_right, lt_top, lt_bottom]):
                low_points.append((i, j, row[j]))

    return low_points


def calculate_risk_level(low_points):
    return sum(1 + p[2] for p in low_points)


def get_coordinates_of_neighbors(x, y, board):
    neighbors = []

    # left neighbor
    if y > 0:
        neighbors.append((x, y - 1))

    # right
    if y + 1 < len(board[0]):
        neighbors.append((x, y + 1))

    # top
    if x > 0:
        neighbors.append((x - 1, y))
    # bottom
    if x + 1 < len(board):
        neighbors.append((x + 1, y))

    return neighbors


def basin_size(x, y, board, seen_points=None):
    if seen_points is None:
        seen_points = set()

    if (x, y) not in seen_points and board[x][y] != 9:
        seen_points.add((x, y))
        neighbors = get_coordinates_of_neighbors(x, y, board)
        for neighbor in neighbors:
            basin_size(neighbor[0], neighbor[1], board, seen_points)

    return len(seen_points)


def find_basin_sizes(low_points, board) -> List[int]:
    basin_sizes = []

    for point in low_points:
        x, y = point[0], point[1]

        current_basin_size = basin_size(x, y, board)
        basin_sizes.append(current_basin_size)

    return basin_sizes


def do_part_one():
    board = read_board()
    low_points = find_low_points(board)
    risk_level = calculate_risk_level(low_points)

    print('Pt 1: %s' % risk_level)


def do_part_two():
    board = read_board()
    low_points = find_low_points(board)
    basins = find_basin_sizes(low_points, board)

    sorted_basins = sorted(basins)
    product = sorted_basins[-3] * sorted_basins[-2] * sorted_basins[-1]
    print('Pt 2: %s' % product)


if __name__ == '__main__':
    do_part_one()
    do_part_two()
