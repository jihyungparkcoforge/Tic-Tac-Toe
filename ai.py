import random


class AI:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty

    def next_ai_move(self, player, game_board):
        if self.difficulty == "hard":
            _, ai_move = self.minimax(
                player=player,
                game_board=game_board,
            )
            return ai_move
        else:
            return self.random_move(
                player=player,
                game_board=game_board,
            )

    def random_move(self, player, game_board):
        moves = game_board.get_available_moves()

        return random.choice(moves)


    def minimax(self, player, game_board):
        if game_board.has_won("O"):
            return 10, None

        if game_board.has_won("X"):
            return -10, None

        moves = game_board.get_available_moves()

        if not moves:
            return 0, None

        best_score = float("-inf") if player == "O" else float("inf")
        best_move = None

        for move in moves:
            row, col = move

            original = game_board.board[row][col]
            game_board.place_mark(row, col, player)

            next_player = "X" if player == "O" else "O"
            score, _ = self.minimax(next_player, game_board)

            game_board.board[row][col] = original

            if player == "O":
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if score < best_score:
                    best_score = score
                    best_move = move

        return best_score, best_move
