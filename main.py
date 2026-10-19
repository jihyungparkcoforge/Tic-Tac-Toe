from board import Board
from game import play

while True:
    game_board = Board()

    play(game_board = game_board)


    while True:
        game_end = input("Do you want to play again?\n 1. Yes   2. No\n").strip()
        if game_end == "1":
            break
        elif game_end == "2":
            exit(0)
        else:
            print("Invalid input. \n")
