from ai import AI


def play(game_board, ai=None):
    mark = "X"

    while not game_board.is_full():
        game_board.display()
        if ai and mark == "O":

            ai_move = ai.next_ai_move(
                player=mark,
                game_board=game_board,
            )

            if ai_move is None:
                break

            row, col = ai_move
        else:
            point = input("Where do you want to place? [0-2], [0-2]: \n")
            row, col = map(int, point.split(","))

        if not game_board.place_mark(row, col, mark):
            continue


        if game_board.has_won(mark):
            game_board.display()
            print(f"{mark} won!")
            break

        if mark == "X":
            mark = "O"
        else:
            mark = "X"

    print("Draw!")
