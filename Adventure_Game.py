import os
os.system('clear')

board_size = 25
position_x = 12
position_y = 10
board = [["# "] * board_size for num in range(board_size + 1)]

for x in range(1, board_size):
    for y in range(1, board_size - 1):
        board[x][y] = ". "

board[position_x][position_y] = "@ "

for line in board:
    print("".join(line))
