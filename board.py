"""
This file creates the board object.
The board itself is private to prevent external manipulation;
instead, it contains all the functions necessary for tic-tac-toe,
such as drawing or erasing marks on the board and printing the entire board.
"""


class Board:
    def __init__(self):
        self._board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]


    def place_mark(self, row, col, mark):
        """
        After checking whether each coordinate is valid, if it is valid,
        it marks that location and returns True.
        If the coordinate has already been marked or the input itself is invalid, it returns False.
        """
        if row not in [0,1,2] or col not in [0,1,2]:
            return False
        if self._board[row][col] != " ":
            return False

        if mark in ["X", "O"]:
            self._board[row][col] = mark
            return True

        return False

    def remove_mark(self, row, col):
        """
        If the program is asked for a coordinate marked with an "O" or an "X,"
        it clears that coordinate. If an empty coordinate is entered, it does nothing.
        """
        if self._board[row][col] in ["O", "X"]:
            self._board[row][col] = " "

    def empty_cells(self):
        """
        It iterates through the 3x3 cells, creates a list of all empty coordinates, and returns it.
        """
        avail = []
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] == " ":
                    avail.append((i,j))
        return avail

    def has_won(self, mark):
        """
        Checks the winning conditions for each row, column, and diagonal, and returns a boolean value.
        """
        for row in self._board:
            if all(cell == mark for cell in row):
                return True

        for col in range(3):
            if all(self._board[row][col] == mark for row in range(3)):
                return True

        return all(self._board[i][2 - i] == mark for i in range(3)) | all(self._board[i][i] == mark for i in range(3))


    def is_full(self):
        """
        I confirmed that there are no empty spaces in the 3x3 grid.
        """
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] == " ":
                    return False
        return True

    def snapshot(self):
        return tuple(tuple(row) for row in self._board)

    def display(self):
        print("   1   2   3 ")
        for i in range(len(self._board)):

            print(" -------------")
            print(f"{i+1}|",end="")
            for j in range(len(self._board[i])):
                print(f" {self._board[i][j]} ", end="|")

            print()
        print(" -------------")
