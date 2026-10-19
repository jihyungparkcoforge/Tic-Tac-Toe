from board import Board

while True:
    mark = "X"
    game_board = Board()


    while not game_board.is_full():
        game_board.display()
        point = input("Where do you want to place? [0-3], [0-3]: \n")
        x,y = point.split(",")
        x = int(x.strip())
        y = int(y.strip())
        if mark == "X":
            mark = "O"
        else:
            mark = "X"
        game_board.place_mark(x,y,mark)

        if game_board.has_won(mark):
            print(f"{mark} won!")
            break

    while True:
        game_end = input("Do you want to play again?\n 1. Yes   2. No\n").strip()
        if game_end == "1":
            continue
        elif game_end == "2":
            break
        else:
            print("Invalid input. \n")
