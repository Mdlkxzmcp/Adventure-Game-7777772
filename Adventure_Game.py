import os
import sys

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

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
        movement = getch()
        if movement == "w" and position_x > 1:
            position_x -= 1
        elif movement == "s" and position_x < 24:
            position_x += 1
        elif movement == "a" and position_y > 1:
            position_y -= 1
        elif movement == "d" and position_y < 23:
            position_y += 1
        elif movement == "q":
            return False
        make_board(position_x, position_y)

main()
