from board import Board


def test_has_won_horizontal():
    board = Board()
    board.board = [
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "],
    ]

    assert board.has_won("X") is True
    assert board.has_won("O") is False

def test_has_won_diagonal():
    board = Board()
    board.board = [
        ["X", "X", "O"],
        ["O", "O", " "],
        ["O", " ", " "],
    ]

    assert board.has_won("X") is False
    assert board.has_won("O") is True

    board.board = [
        ["X", "X", "O"],
        ["O", "X", " "],
        ["O", " ", "X"],
    ]

    assert board.has_won("X") is True
    assert board.has_won("O") is False

def test_has_won_vertical():
    board = Board()
    board.board = [
        ["X", "X", "O"],
        ["X", "O", " "],
        ["X", " ", " "],
    ]

    assert board.has_won("X") is True
    assert board.has_won("O") is False

def test_place_mark():
    board = Board()

    board.place_mark(0, 0, "X")

    assert board.board[0][0] == "X"


def test_remove_mark():
    board = Board()

    board.board = [
        ["X", "X", "O"],
        ["X", "O", " "],
        ["X", " ", " "],
    ]
    board.remove_mark(0,0)
    assert board.board[0][0] == " "

def test_is_full():
    board = Board()

    board.board = [
        ["X", "X", "O"],
        ["O", "O", "X"],
        ["X", "O", "X"],
    ]
    assert board.is_full() is True

    board.board = [
        ["X", "X", "O"],
        ["O", "O", " "],
        ["X", "O", "X"],
    ]
    assert board.is_full() is False

def test_empty_cells():
    board = Board()

    board.board = [
        ["X", "X", "O"],
        ["X", "O", " "],
        ["X", " ", "O"],
    ]
    assert board.empty_cells() == [(1,2),(2,1)]
