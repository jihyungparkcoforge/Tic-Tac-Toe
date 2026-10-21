from board import Board


def make_board(rows):
    board = Board()
    for row, cells in enumerate(rows):
        for col, mark in enumerate(cells):
            if mark != " ":
                assert board.place_mark(row, col, mark)
    return board


def test_has_won_horizontal():
    board = Board()
    board = make_board([
        ["X", "X", "X"],
        ["O", "O", " "],
        [" ", " ", " "],
    ])

    assert board.has_won("X") is True
    assert board.has_won("O") is False

def test_has_won_diagonal():
    board = Board()
    board = make_board([
        ["X", "X", "O"],
        ["O", "O", " "],
        ["O", " ", " "],
    ])

    assert board.has_won("X") is False
    assert board.has_won("O") is True

    board = make_board([
        ["X", "X", "O"],
        ["O", "X", " "],
        ["O", " ", "X"],
    ])

    assert board.has_won("X") is True
    assert board.has_won("O") is False

def test_has_won_vertical():
    board = Board()
    board = make_board([
        ["X", "X", "O"],
        ["X", "O", " "],
        ["X", " ", " "],
    ])

    assert board.has_won("X") is True
    assert board.has_won("O") is False

def test_place_mark():
    board = Board()

    board.place_mark(0, 0, "X")

    assert board.snapshot()[0][0] == "X"


def test_remove_mark():
    board = Board()

    board = make_board([
        ["X", "X", "O"],
        ["X", "O", " "],
        ["X", " ", " "],
    ])
    board.remove_mark(0,0)
    assert board.snapshot()[0][0] == " "

def test_is_full():
    board = Board()

    board = make_board([
        ["X", "X", "O"],
        ["O", "O", "X"],
        ["X", "O", "X"],
    ])
    assert board.is_full() is True

    board = make_board([
        ["X", "X", "O"],
        ["O", "O", " "],
        ["X", "O", "X"],
    ])
    assert board.is_full() is False

def test_empty_cells():
    board = Board()

    board = make_board([
        ["X", "X", "O"],
        ["X", "O", " "],
        ["X", " ", "O"],
    ])
    assert board.empty_cells() == [(1,2),(2,1)]

def test_board_size():
    board = Board()
    assert len(board.empty_cells()) == 9


def test_empty_at_beginning():
    board = Board()

    board = make_board([
        ["X", "X", "O"],
        ["X", "O", " "],
        ["X", " ", "O"],
    ])

    board = Board()
    assert board.empty_cells() == [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]


def test_taken_cell_preserves_first_mark():
    board = Board()
    assert board.place_mark(0, 0, "X") is True
    assert board.place_mark(0, 0, "O") is False
    assert board.snapshot()[0][0] == "X"


def test_full_board_without_winner_is_draw():
    board = make_board([
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ])
    assert board.is_full()
    assert not board.has_won("X")
    assert not board.has_won("O")

def test_place_mark_invalid():
    board = Board()

    assert board.place_mark(-1, 0, "X") == False
    assert board.place_mark(2, 3, "X") == False
