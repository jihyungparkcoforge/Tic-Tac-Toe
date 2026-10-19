from copy import deepcopy

from ai import AI
from board import Board


def test_easy_returns_empty_cell():
    board = Board()
    board.place_mark(0, 0, "X")
    available = board.empty_cells()

    move = AI("easy").next_ai_move("O", board)

    assert move in available


def test_hard_takes_winning():
    board = Board()

    placements = [
        (0, 0, "X"), (0, 1, "X"), (0, 2, "O"),
        (1, 0, "X"), (1, 1, "O"),
                     (2, 1, "O"), (2, 2, "X"),
    ]
    for row, col, mark in placements:
        board.place_mark(row, col, mark)

    move = AI("hard").next_ai_move("O", board)

    assert move == (2, 0)


def test_hard_blocks():
    board = Board()


    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(1, 1, "O")

    move = AI("hard").next_ai_move("O", board)

    assert move == (0, 2)


def test_ai_does_not_change_board():
    board = Board()
    board.place_mark(0, 0, "X")
    original = deepcopy(board.board)

    AI(difficulty="hard").next_ai_move("O", board)

    assert board.board == original
