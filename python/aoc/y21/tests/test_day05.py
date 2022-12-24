from unittest import TestCase

from day_05 import build_board, part_one, part_two


class Day05Tests(TestCase):

    def test_horizontal_line_with_two_segments(self):
        board = build_board(10, 10)
        lines = ['0,9 -> 5,9', '0,9 -> 2,9']

        part_one(lines, board)
        for row in board:
            print(row)

        self.assertEqual(board[9][0], 2)
        self.assertEqual(board[9][1], 2)
        self.assertEqual(board[9][2], 2)
        self.assertEqual(board[9][3], 1)
        self.assertEqual(board[9][4], 1)
        self.assertEqual(board[9][5], 1)

    def test_part_two_whole_input(self):
        board = build_board(10, 10)
        lines = [
            '0, 9 -> 5, 9',
            '8, 0 -> 0, 8',
            '9, 4 -> 3, 4',
            '2, 2 -> 2, 1',
            '7, 0 -> 7, 4',
            '6, 4 -> 2, 0',
            '0, 9 -> 2, 9',
            '3, 4 -> 1, 4',
            '0, 0 -> 8, 8',
            '5, 5 -> 8, 2'
        ]

        part_two(lines, board)
        for row in board:
            print(row)

        # bottom left corner line
        self.assertEqual(board[9][0], 2)
        self.assertEqual(board[9][1], 2)
        self.assertEqual(board[9][2], 2)
        self.assertEqual(board[9][3], 1)
        self.assertEqual(board[9][4], 1)
        self.assertEqual(board[9][5], 1)

        # l to r diagonal line starting in top left corner
        self.assertEqual(board[0][0], 1)
        self.assertEqual(board[1][1], 1)
        self.assertEqual(board[2][2], 2)
        self.assertEqual(board[3][3], 1)
        self.assertEqual(board[4][4], 3)
        self.assertEqual(board[5][5], 2)
        self.assertEqual(board[6][6], 1)
        self.assertEqual(board[7][7], 1)
        self.assertEqual(board[8][8], 1)

        # l to r diagonal upward line starting at bottom left corner
        self.assertEqual(board[8][0], 1)
        self.assertEqual(board[7][1], 1)
        self.assertEqual(board[6][2], 1)
        self.assertEqual(board[5][3], 1)
        self.assertEqual(board[4][4], 3)
        self.assertEqual(board[3][5], 2)
        self.assertEqual(board[2][6], 1)
        self.assertEqual(board[1][7], 2)
        self.assertEqual(board[0][8], 1)
