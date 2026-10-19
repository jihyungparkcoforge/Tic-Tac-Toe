
def play(game_board):
    mark = "X"
    while not game_board.is_full():
        game_board.display()
        point = input("Where do you want to place? [0-2], [0-2]: \n")
        x,y = point.split(",")
        x = int(x.strip())
        y = int(y.strip())
        if mark == "X":
            mark = "O"
        else:
            mark = "X"
        if not game_board.place_mark(x,y,mark):
            continue

        if game_board.has_won(mark):
            game_board.display()
            print(f"{mark} won!")
            break
