import random

import pytest

from ai import AI, EasyAI, HardAI
from board import Board


def test_easy_returns_empty_cell():
    board = Board()
    board.place_mark(0, 0, "X")
    available = board.empty_cells()

    move = EasyAI(random.Random(0)).choose_move(board, "O")

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

    move = HardAI(random.Random(0)).choose_move(board, "O")

    assert move == (2, 0)


def test_hard_blocks():
    board = Board()


    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(1, 1, "O")

    move = HardAI(random.Random(0)).choose_move(board, "O")

    assert move == (0, 2)


@pytest.mark.parametrize("ai_class", [EasyAI, HardAI])
def test_ai_does_not_change_board(ai_class):
    board = Board()
    board.place_mark(0, 0, "X")
    original = board.snapshot()

    ai_class(random.Random(0)).choose_move(board, "O")

    assert board.snapshot() == original


def test_abstract_ai_cannot_be_created():
    with pytest.raises(TypeError):
        AI(random.Random(0))


def test_hard_never_loses_as_second_player():
    board = Board()
    ai = HardAI(random.Random(0))

    def explore(mark):
        assert not board.has_won("X")
        if board.has_won("O") or board.is_full():
            return

        moves = board.empty_cells() if mark == "X" else [ai.choose_move(board, mark)]
        for row, col in moves:
            assert board.place_mark(row, col, mark)
            explore("O" if mark == "X" else "X")
            board.remove_mark(row, col)

    explore("X")
