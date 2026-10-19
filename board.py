class Board:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]


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
        for row in self.board:
            if all(cell == mark for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == mark for row in range(3)):
                return True

        if all(self.board[i][i] == mark for i in range(3)):
            return True

        return all(self.board[i][2 - i] == mark for i in range(3))


    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == " ":
                    return False
        return True

    def display(self):
        print("   0   1   2 ")
        for i in range(len(self.board)):

            print(" -------------")
            print(f"{i}|",end="")
            for j in range(len(self.board[i])):
                print(f" {self.board[i][j]} ", end="|")

            print()
        print(" -------------")
