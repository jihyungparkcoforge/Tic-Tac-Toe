"""
Main file. It reads the user's preferences and sets the parameters for the loop in `game.py` before running it.
"""

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

        # If the user selects single-player mode, the program prompts the user to enter an AI difficulty level, creates an AI object, and passes it as a parameter to game.play().
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

        # Depending on the user's choice, the game either continues or ends.
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
