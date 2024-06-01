from collections import namedtuple

Point = namedtuple("Point", "x y")


def read_file():
    with open('data/day05.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def build_board(rows, columns):
    """
    build 1000 x 1000 board of zeros
    """
    board = list()
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(0)

        board.append(row)

    return board


def mark_horizontal_line(board, start: Point, end: Point):
    assert start.y == end.y
    row_index = start.y

    # may need to swap range start and end to handle pair such as
    # (9, 4) to (3, 4). Probably could just use range(min(start.x, end.x) + abs(start.x - end.x))
    # to simplify
    if start.x < end.x:
        range_start = start.x
        range_end = end.x + 1
    else:
        range_start = end.x
        range_end = start.x + 1

    for column in range(range_start, range_end):
        board[row_index][column] = board[row_index][column] + 1


def mark_vertical_line(board, start: Point, end: Point):
    assert start.x == end.x

    if start.y < end.y:
        range_start = start.y
        range_end = end.y + 1
    else:
        range_start = end.y
        range_end = start.y + 1

    for row in range(range_start, range_end):
        board[row][start.x] = board[row][start.x] + 1


def mark_diagonal_line(board, start: Point, end: Point):
    d_x = end.x - start.x
    d_y = end.y - start.y

    length = max(abs(d_x), abs(d_y))

    x_direction = int(d_x / length)
    y_direction = int(d_y / length)

    for i in range(length + 1):
        x = start.x + i * x_direction
        y = start.y + i * y_direction
        board[y][x] = board[y][x] + 1


def part_one(lines, board):
    for line in lines:
        both_coordinate_pairs = line.split('->')
        first_pair = both_coordinate_pairs[0].split(',')
        second_pair = both_coordinate_pairs[1].split(',')

        start = Point(int(first_pair[0]), int(first_pair[1]))
        end = Point(int(second_pair[0]), int(second_pair[1]))

        is_horizontal = start.y == end.y
        is_vertical = start.x == end.x
        if is_vertical:
            mark_vertical_line(board, start, end)
        elif is_horizontal:
            mark_horizontal_line(board, start, end)
        else:
            continue

    num_points_ge_2 = 0
    for row in board:
        for point in row:
            if point > 1:
                num_points_ge_2 += 1

    print('Part One: %s' % num_points_ge_2)


def part_two(lines, board):
    for line in lines:
        both_coordinate_pairs = line.split('->')
        first_pair = both_coordinate_pairs[0].split(',')
        second_pair = both_coordinate_pairs[1].split(',')

        start = Point(int(first_pair[0]), int(first_pair[1]))
        end = Point(int(second_pair[0]), int(second_pair[1]))

        is_horizontal = start.y == end.y
        is_vertical = start.x == end.x
        if is_vertical:
            mark_vertical_line(board, start, end)
        elif is_horizontal:
            mark_horizontal_line(board, start, end)
        else:
            mark_diagonal_line(board, start, end)

    num_points_ge_2 = 0
    for row in board:
        for point in row:
            if point > 1:
                num_points_ge_2 += 1

    print('Part Two: %s' % num_points_ge_2)


if __name__ == '__main__':
    lines = read_file()
    board = build_board(1000, 1000)

    part_one(lines, board)
    part_two(lines, board)
