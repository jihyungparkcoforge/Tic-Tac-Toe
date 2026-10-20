import random
from abc import ABC, abstractmethod


class AI(ABC):
    def __init__(self, rng: random.Random):
        self._rng = rng

    @abstractmethod
    def choose_move(self, board, mark):
        """Return an empty (row, col) without changing the board."""
        pass


class EasyAI(AI):
    def choose_move(self, board, mark):
        return self._rng.choice(board.empty_cells())


class HardAI(AI):
    def choose_move(self, board, mark):
        _, move = self._minimax(mark, board)
        return move


    def _minimax(self, player, game_board):
        if game_board.has_won("O"):
            return 10, None

        if game_board.has_won("X"):
            return -10, None

        moves = game_board.empty_cells()

        if not moves:
            return 0, None

        best_score = float("-inf") if player == "O" else float("inf")
        best_move = None

        for move in moves:
            row, col = move

            game_board.place_mark(row, col, player)

            next_player = "X" if player == "O" else "O"
            try:
                score, _ = self._minimax(next_player, game_board)
            finally:
                game_board.remove_mark(row, col)

            if player == "O":
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if score < best_score:
                    best_score = score
                    best_move = move

        return best_score, best_move
