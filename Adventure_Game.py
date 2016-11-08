import os
import time
import sys
import tty
import termios


def intro():
    print("\n\n      Welcome to the grand game of 'Mushroom Picking'!\n\n")
    time.sleep(1)
    print("""'Tales border on the thin line between reality and myth' - Mc' Dingus\n\n
    You wake up in your wooden shed, the first thing your senses pick up is a message:\n
    "Johny my boy, I'd like some mushrooms for my soup, could you get me some from
     The Dark Forest? Thanks. Oh actually bring me... 23 of the small ones and that funny one~"\n
    In that instant you know what date it is, it's your grandmas death aniversary~!
     You take your basket, put on your special camo outfit and go mushroom picking.\n\nHint: Don't starve.
    """)
    time.sleep(2)


def make_board(position_x, position_y, level):
    os.system('clear')
    board_size = 25
    # colors v
    dark_green = '\33[32m'
    bright_green = '\33[92m'
    dark_purple = '\33[35m'
    bright_purple = '\33[95m'
    dark_groundish = '\33[36m'
    bright_groundish = '\33[96m'
    white = '\33[97m'
    blue = '\33[94m'
    gold = '\33[33m'
    end_color = '\33[0m'
    # making symbols often with colors for each element of the map
    ground = bright_green + ". " + end_color
    tree = dark_green + "# " + end_color
    water = blue + "~ " + end_color
    mountain = gold + "A " + end_color
    secret = bright_green + "# " + end_color  # a tree with a different color
    bridge = dark_groundish + "= " + end_color
    basket = "u "
    big_basket = "U "
    good_mushroom = dark_purple + "qp" + end_color
    bad_mushroom = bright_purple + "qp" + end_color
    board = [[tree] * board_size for num in range(board_size + 1)]
    walls = [tree, water, mountain]
    for x in range(1, board_size):
        for y in range(1, board_size - 1):
            board[x][y] = ground

    if level == 1:
        # tree placement
        for loc in range(1, 5):
            board[loc][4] = tree
        for loc in (2, 3, 4):
            board[loc][11] = tree
        for loc in (3, 6, 7, 8):
            board[loc][12] = tree
        for loc in range(1, 6):
            board[15][loc] = tree
        board[6][1] = tree
        board[7][2] = tree
        board[12][23] = tree
        # water placement
        for loc in (9, 16, 18):
            board[loc][22] = water
        for loc in range(11, 15):
            board[loc][20] = water
        board[15][21] = bridge
        board[17][21] = water
        board[19][23] = water
        board[10][21] = water
        board[8][23] = water
        # mountain placement
        for loc in (2, 3):
            board[loc][20] = mountain
        for loc in (4, 5, 7):
            board[17][loc] = mountain
        board[11][14] = mountain
        board[11][23] = mountain
        board[12][22] = mountain
        board[13][23] = mountain
        board[18][5] = mountain
        board[22][17] = mountain
        board[23][5] = mountain
        board[23][6] = mountain
        # item placement
        # if items["basket"] == 1:
        #     board[20][11] = basket

    if level == 2:
        board[5][5] = tree
        board[3][7] = tree
        board[3][7] = tree
        board[2][8] = tree
        for loc in range(2, 5):
            board[loc][9] = tree
        board[5][12] = tree
        board[4][13] = tree
        board[8][13] = tree
        board[9][13] = tree
        for loc in (6, 8, 9, 13):
            board[loc][14] = tree
        board[7][15] = tree
        board[13][15] = tree
        board[14][15] = tree
        board[13][17] = tree
        board[1][21] = tree
        board[1][22] = tree
        board[4][22] = tree
        board[13][22] = tree
        for loc in range(1, 5):
            board[loc][23] = tree
        board[13][23] = tree
        board[23][3] = tree
        board[24][4] = tree

        # item placement
        board[2][22] = big_basket

    if level == 3:
        board[20][11] = "<^"
        board[20][12] = "~^"
        board[20][13] = "> "
        board[21][11] = "e3"
        board[21][12] = "33"
        board[21][13] = "e "
        board[22][11] = ".|"
        board[22][12] = "w|"

    board[position_x][position_y] = "@ "

    for line in board:
        print("".join(line))

    return board


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    position_x = 1
    position_y = 1
    level = 1
    # intro()
    board = make_board(position_x, position_y, level)
    while True:
        movement = getch()
        if movement == "w" and ". " in board[position_x - 1][position_y]:
            position_x -= 1
        elif movement == "s" and ". " in board[position_x + 1][position_y]:
            position_x += 1
        elif movement == "a" and ". " in board[position_x][position_y - 1]:
            position_y -= 1
        elif movement == "d" and ". " in board[position_x][position_y + 1]:
            position_y += 1
        elif movement == "q":
            return False
        board = make_board(position_x, position_y, level)

if __name__ == '__main__':
    main()
