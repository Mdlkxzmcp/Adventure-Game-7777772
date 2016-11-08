import os
import time
import sys
import tty
import termios

inv = {'rope': 0, 'torch': 0, 'gold coin': 0, 'dagger': 0, 'arrow': 0}

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
    ground = ". "
    tree = "# "
    water = "~ "  # to be changed into the ~ = symbol
    mountain = "A "
    secret = "!^"
    bridge = "▓▓"
    basket = "u "
    big_basket = "U "
    good_mushroom = "qp"
    bad_mushroom = "qp"
    board = [[tree] * board_size for num in range(board_size + 1)]
    walls = [tree, water, mountain]
    for x in range(1, board_size):
        for y in range(1, board_size - 1):
            board[x][y] = ground

    if level == 1:
        # tree placement
        for loc in range(1, 5):
            board[loc][4] = tree
        for loc in range(3, 5):
            board[loc][11] = tree
        for loc in range(3, 5):
            board[loc][12] = tree
        board[6][1] = tree
        board[7][2] = tree
        # water placement
        board[8][23] = water
        board[9][22] = water
        board[10][21] = water
        for loc in range(11, 15):
            board[loc][20] = water
        board[15][21] = bridge
        board[16][22] = water
        board[17][21] = water
        board[18][22] = water
        board[19][23] = water
        # mountain placement
        for loc in range(2, 4):
            board[loc][20] = mountain
        board[11][14] = mountain
        board[11][23] = mountain
        board[12][22] = mountain
        board[13][23] = mountain
        board[17][4] = mountain
        board[17][5] = mountain
        board[17][7] = mountain
        board[18][5] = mountain
        board[22][17] = mountain
        board[23][5] = mountain
        board[23][6] = mountain
        # item placement
        # if items["basket"] == 1:
        #     board[20][11] = basket

    if level == 2:
        board[5][5] = tree
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

def display_inventory(inventory):
    print ("Inventory:")

    print_table(inv)
    print("Total number of items:", sum(inv.values()))

def print_table(inventory):
    n = max(len(key) for key in inv)
    m = max(len(str(v)) for v in inv.values())
    if m < 7:
        m = 7
    print ('count'.rjust(m),'item name'.rjust(n+3))
    print ("-"*(n+m+4))

    for key, value in sorted(inv.items(), key = lambda i: i[1], reverse = True):
        print (str(inv[key]).rjust(m), key.rjust(n+3))

    print ("-"*(n+m+4))


def main():
    position_x = 1
    position_y = 1
    level = 1
    # intro()
    board = make_board(position_x, position_y, level)
    while True:
        display_inventory(inv)
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
