import copy


def read_file():
    with open('data/day04.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def build_boards(lines):
    boards = []
    current_board = []
    for line in lines[2:]:
        if not line:
            boards.append(current_board)
            current_board = []

        row = [(int(num), False) for num in line.split(' ') if num != '']
        if row:
            current_board.append(row)

    return boards


def mark_number_seen(number, boards):
    for board in boards:
        for row in board:
            for index, box in enumerate(row):
                if box[0] == number:
                    row[index] = (number, True)


def has_row_bingo(board):
    for row in board:
        if all([row[0][1], row[1][1], row[2][1], row[3][1], row[4][1]]):
            return True

    return False


def has_column_bingo(board):
    for column in range(0, 5):
        if all(
                [board[0][column][1], board[1][column][1], board[2][column][1], board[3][column][1],
                 board[4][column][1]]):
            return True

    return False


def has_bingo(board):
    return has_row_bingo(board) or has_column_bingo(board)


def sum_seen_numbers(board):
    return sum([
        item[0] for row in board for item in row if item[1]
    ])


def part_one(boards, bingo_input):
    bingo_seen = False
    for number in bingo_input:
        mark_number_seen(number, boards)

        for board in boards:
            if has_bingo(board):
                print('Bingo for board on number %s' % number)
                unseen_num_sum = sum([
                    item[0] for row in board for item in row if item[1] == False
                ])

                print('Sum of unseen numbers on winning board: %s' % unseen_num_sum)
                print(unseen_num_sum * number)
                for row in board:
                    print(row)
                bingo_seen = True
                break

        if bingo_seen:
            break


def part_two(boards, bingo_input):
    # ordered list of tuples: (number_board_got_bingo_on, board)
    numbers_to_completed_boards = []

    # keep track of boards that already have bingo since a board that has a bingo
    # will have a bingo on subsequent draws of the number
    bingoed_boards_indices = set()

    for number in bingo_input:
        mark_number_seen(number, boards)

        for idx, board in enumerate(boards):
            if has_bingo(board) and idx not in bingoed_boards_indices:
                # make deep copy of board state at time it won; subsequent iterations will mark numbers seen
                # that were not seen at time of bingo
                numbers_to_completed_boards.append((number, copy.deepcopy(board)))
                bingoed_boards_indices.add(idx)

    last_pair = numbers_to_completed_boards[-1]
    print('Last board to win would win on  %s' % last_pair[0])
    board = last_pair[1]
    unseen_num_sum = sum([item[0] for row in board for item in row if item[1] == False])

    print('Sum of unseen numbers on winning board: %s' % unseen_num_sum)
    print('Product of unseen numbers times winning bingo draw: %s' % (unseen_num_sum * last_pair[0]))


if __name__ == '__main__':
    lines = read_file()
    bingo_input = [int(num.strip()) for num in lines[0].split(',')]
    boards = build_boards(lines)

    part_one(boards, bingo_input)
    print('\n=== Part Two ===\n')
    part_two(boards, bingo_input)
