import random
import sys

from ai import EasyAI, HardAI
from board import Board
from game import play


def main():
    while True:
        game_board = Board()

        while True:
            gamemode = input("Do you want to play single mode?\n 1. Yes   2. No\n").strip()
            if gamemode in ["1","2"]:
                break
            else:
                print("Invalid input. \n")

        if gamemode == "1":
            while True:
                level = input("What difficulty level do you want to play?\n 1. easy   2. hard\n").strip()
                if level == "1":
                    ai = EasyAI(random.Random())
                    play(game_board = game_board, ai = ai)
                    break
                elif level == "2":
                    ai = HardAI(random.Random())
                    play(game_board = game_board, ai = ai)
                    break
                else:
                    print("Invalid input. \n")
        else:
            play(game_board = game_board)


        while True:
            game_end = input("Do you want to play again?\n 1. Yes   2. No\n").strip()
            if game_end == "1":
                break
            elif game_end == "2":
                sys.exit()
            else:
                print("Invalid input. \n")



if __name__ == "__main__":
    main()
