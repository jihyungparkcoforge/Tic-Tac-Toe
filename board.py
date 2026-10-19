class Board:
    def __init__(self, board, turn):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        self.turn = "player 1"


    def place_mark(self, row, col, mark):
        if self.board[row][col] != " ":
            return False

        if mark in ["X", "O"]:
            self.board[row][col] = mark
            return True

        return False

    def remove_mark(self, row, col):
        if self.board[row][col] in ["O", "X"]:
            self.board[row][col] = " "

    def empty_cells(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print((i, j))

    def has_won(self, mark):
        # algorithm to detect won
        return

    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == " ":
                    return False
