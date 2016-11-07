import os


def make_board(position_x, position_y):
    os.system('clear')
    board_size = 25
    board = [["# "] * board_size for num in range(board_size + 1)]

    for x in range(1, board_size):
        for y in range(1, board_size - 1):
            board[x][y] = ". "

    board[position_x][position_y] = "@ "

    for line in board:
        print("".join(line))


def main():
    position_x = 12
    position_y = 10
    make_board(position_x, position_y)
    while True:
        movement = input()
        if movement == "w":
            position_x -= 1
        elif movement == "s":
            position_x += 1
        elif movement == "a":
            position_y -= 1
        elif movement == "d":
            position_y += 1
        elif movement == "quit":
            return False
        make_board(position_x, position_y)

main()
