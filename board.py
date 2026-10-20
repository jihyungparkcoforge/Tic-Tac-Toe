class Board:
    def __init__(self):
        self._board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]


    def place_mark(self, row, col, mark):
        if self._board[row][col] != " ":
            return False

        if row not in [0,1,2] or col not in [0,1,2]:
            return False

        if mark in ["X", "O"]:
            self._board[row][col] = mark
            return True

        return False

    def remove_mark(self, row, col):
        if self._board[row][col] in ["O", "X"]:
            self._board[row][col] = " "

    def empty_cells(self):
        avail = []
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] == " ":
                    avail.append((i,j))
        return avail

    def has_won(self, mark):
        for row in self._board:
            if all(cell == mark for cell in row):
                return True

        for col in range(3):
            if all(self._board[row][col] == mark for row in range(3)):
                return True

        return all(self._board[i][2 - i] == mark for i in range(3)) | all(self._board[i][i] == mark for i in range(3))


    def is_full(self):
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
