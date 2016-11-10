import os
import time
import sys
import tty
import termios
import random

# to do: boss zone triggering the hot cold game, item del after pick up, bug fixing, story between level 1&2 & 2&3.


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
    while True:
        ready = input("Are you ready for the greatest adventure of your life? ").lower()
        if ready in ("yes", "y"):
            return False
        else:
            time.sleep(1)
            continue


def make_board(hero_x, hero_y, status):
    # arguments = dict(locals().items())  # !!!!!!!!!!!
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
    meat = "& "
    good_mushroom = dark_purple + "qp" + end_color
    bad_mushroom = bright_purple + "qp" + end_color

    board = [[tree] * board_size for num in range(board_size + 1)]
    walls = [tree, water, mountain]
    for x in range(1, board_size):
        for y in range(1, board_size - 1):
            board[x][y] = ground

    if status['level'] == 1:
        # tree placement
        for loc in range(1, 6):
            board[loc][3] = tree
        for loc in range(1, 6):
            board[loc][4] = tree
        for loc in range(1, 6):
            board[loc][5] = tree
        for loc in (2, 3, 4):
            board[loc][11] = tree
        for loc in (2, 3, 4):
            board[loc][10] = tree
        for loc in (2, 3, 4, 5, 6):
            board[loc][9] = tree
        for loc in (2, 3, 4, 5):
            board[loc][8] = tree
        for loc in range(6, 20):
            board[loc][12] = tree
        for loc in range(7, 19):
            board[loc][11] = tree
        for loc in range(10, 17):
            board[loc][10] = tree
        for loc in range(1, 6):
            board[15][loc] = tree
        for loc in range(1, 6):
            board[14][loc] = tree
        for loc in range(1, 6):
            board[13][loc] = tree
        for loc in range(19, 24):
            board[24][loc] = tree
        for loc in range(19, 23):
            board[loc][1] = tree
        for loc in range(7, 12):
            board[loc][1] = tree
        for loc in range(7, 12):
            board[loc][6] = tree
        for loc in range(10, 17):
            board[loc][16] = tree
        for loc in range(12, 15):
            board[loc][17] = tree
        for loc in range(11, 14):
            board[loc][15] = tree
        board[6][1] = tree
        board[7][2] = tree
        board[12][23] = tree
        # water placement
        for loc in (9, 16, 18):
            board[loc][22] = water
        for loc in (9, 16, 18):
            board[loc][21] = water
        for loc in range(11, 15):
            board[loc][20] = water
        for loc in range(11, 15):
            board[loc][19] = water
        board[15][21] = bridge
        board[15][20] = bridge
        board[17][21] = water
        board[17][22] = water
        board[10][20] = water
        board[20][23] = water
        board[19][23] = water
        board[19][22] = water
        board[10][21] = water
        board[8][23] = water
        # mountain placement
        for loc in range(2, 6):
            board[loc][20] = mountain
        for loc in range(3, 8):
            board[loc][19] = mountain
        for loc in range(1, 8):
            board[loc][21] = mountain
        for loc in (4, 5, 7):
            board[17][loc] = mountain
        for loc in (4, 5, 7):
            board[18][loc] = mountain
        board[11][14] = mountain
        board[11][23] = mountain
        board[12][22] = mountain
        board[13][23] = mountain
        board[18][5] = mountain
        for loc in range(16, 23):
            board[loc][14] = mountain
        for loc in range(18, 21):
            board[loc][15] = mountain
        for loc in range(5, 8):
            board[loc][15] = mountain
        board[18][6] = mountain
        board[22][17] = mountain
        board[23][5] = mountain
        board[23][6] = mountain
        # item placement
        if status['basket'] == 0:
            board[20][11] = basket

    if status['level'] == 2:
        board[5][5] = tree
        board[3][7] = tree
        board[3][7] = tree
        board[2][8] = tree
        for loc in range(2, 5):
            board[loc][9] = tree
        for loc in range(2, 5):
            board[loc][20] = tree
        for loc in range(20, 24):
            board[loc][20] = tree
        for loc in range(19, 24):
            board[loc][19] = tree
        for loc in range(19, 23):
            board[loc][15] = tree
        for loc in range(19, 25):
            board[loc][17] = tree
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
        for loc in range(5, 15):
            board[17][loc] = water
        for loc in range(1, 16):
            board[16][loc] = water
        for loc in range(1, 16):
            board[15][loc] = water
        for loc in range(6, 13):
            board[18][loc] = water
        for loc in range(8, 10):
            board[19][loc] = water
        for loc in range(16, 24):
            board[14][loc] = water
        for loc in range(16, 18):
            board[15][loc] = water
        for loc in range(19, 24):
            board[18][loc] = water
        for loc in range(20, 24):
            board[12][loc] = water
        for loc in range(19, 22):
            board[13][loc] = water
        for loc in range(16, 18):
            board[loc][18] = water
        for loc in range(20, 24):
            board[15][loc] = mountain
        for loc in range(17, 24):
            board[8][loc] = mountain
        for loc in range(17, 24):
            board[loc][14] = mountain
        for loc in range(18, 24):
            board[loc][13] = mountain
        for loc in range(19, 23):
            board[loc][12] = mountain
        for loc in range(9, 14):
            board[loc][8] = mountain
        for loc in range(9, 12):
            board[loc][7] = mountain
        for loc in range(3, 12):
            board[loc][1] = mountain
        for loc in range(5, 11):
            board[loc][2] = mountain
        for loc in range(9, 14):
            board[loc][6] = mountain
        for loc in range(18, 22):
            board[loc][3] = mountain
        for loc in range(18, 22):
            board[loc][2] = mountain
        for loc in range(20, 24):
            board[loc][7] = mountain
        board[15][15] = bridge
        board[15][14] = bridge
        board[16][15] = bridge
        board[18][22] = bridge
        if status['basket'] == 1:
            board[2][22] = basket

    elif status['level'] == 3:
        board[20][11] = "<^"
        board[20][12] = "~^"
        board[20][13] = "> "
        board[21][11] = "e3"
        board[21][12] = "33"
        board[21][13] = "e "
        board[22][11] = ".|"
        board[22][12] = "w|"

    if status['level'] == 1:
        number_of_good_shrooms = 8
        number_of_bad_shrooms = 4
    elif status['level'] == 2:
        number_of_good_shrooms = 15
        number_of_bad_shrooms = 8

    if status['level'] != 3:
        if status['state'] == 0:
            a = 0
            while a < number_of_good_shrooms:
                c = random.randint(1, 23)
                d = random.randint(1, 23)
                if board[c][d] == ground:
                    board[c][d] = good_mushroom
                    a += 1
                    status['g_shrooms'].append([c, d])
        elif status['state'] == 1:
            a = 0
            while a < number_of_good_shrooms:
                board[status['g_shrooms'][a][0]][status['g_shrooms'][a][1]] = good_mushroom
                a += 1

        if status['state'] == 0:
            a = 0
            while a < number_of_bad_shrooms:
                c = random.randint(1, 23)
                d = random.randint(1, 23)
                if board[c][d] == ground:
                    board[c][d] = bad_mushroom
                    a += 1
                    status['b_shrooms'].append([c, d])

        elif status['state'] == 1:
            a = 0
            while a < number_of_bad_shrooms:
                board[status['b_shrooms'][a][0]][status['b_shrooms'][a][1]] = bad_mushroom
                a += 1

        if status['state'] == 0:
            a = 0
            while a < 8:
                c = random.randint(1, 23)
                d = random.randint(1, 23)
                if board[c][d] == ground:
                    board[c][d] = meat
                    a += 1
                    status['meat'].append([c, d])
        elif status['state'] == 1:
            a = 0
            while a < len(status['meat']):
                board[status['meat'][a][0]][status['meat'][a][1]] = meat
                a += 1

    if good_mushroom in board[hero_x][hero_y]:
        if status['mushrooms'] < status['limit']:
            status['mushrooms'] += 1
            # del status['g_shrooms'][hero_x][hero_y]

    if meat in board[hero_x][hero_y]:
        status['steps'] += 10
        # del status['meat'][hero_x][hero_y]

    if basket in board[hero_x][hero_y]:
        status['basket'] += 1

    status['state'] = 1

    board[hero_x][hero_y] = "@ "

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


def print_table(inventory):
    width = 11
    print("Status:")
    print("-" * width, "~", sep='')
    for key, value in inventory.items():
        if key == 'steps':
            steps = ("{} - {}".format(value, key))
        elif key == 'life':
            life = ("{} - {}".format(value, key))
        elif key == 'mushrooms':
            mushrooms = ("{} - {}".format(value, key))
    print(steps, '\n', life, '\n', mushrooms)


def status_update(hero_x, hero_y, status):
    if status['mushrooms'] == 8 and status['level'] == 1:
        status['level'] = 2
        status['state'] = 0
        hero_x = 1
        hero_y = 1
    if status['basket'] == 1:
        status['limit'] = 12
    if status['basket'] == 2:
        status['limit'] = 15
    if status['steps'] == 0:
        status['life'] -= 1
        hero_x = 1
        hero_y = 1
        status['steps'] = 100
    return hero_x, hero_y, status


def main():
    status = {'steps': 100, 'life': 3, 'level': 1, 'boots': 0, 'basket': 0, 'limit': 5,
              'mushrooms': 0, 'state': 0, 'g_shrooms': [], 'b_shrooms': [], 'meat': []}
    hero_x = 1
    hero_y = 1
    # intro()
    board = make_board(hero_x, hero_y, status)
    status['state'] = 1
    while True:
        print_table(status)
        movement = getch()
        if movement == "w" and (". " in board[hero_x - 1][hero_y] or "= " in board[hero_x - 1][hero_y] or "qp" in board[hero_x - 1][hero_y] or "S "in board[hero_x - 1][hero_y] or "& " in board[hero_x - 1][hero_y] or "u " in board[hero_x - 1][hero_y]):
            hero_x -= 1
            status['steps'] -= 1
        elif movement == "s" and (". " in board[hero_x + 1][hero_y] or "= " in board[hero_x + 1][hero_y] or "qp" in board[hero_x + 1][hero_y] or "S " in board[hero_x + 1][hero_y] or "& " in board[hero_x + 1][hero_y] or "u " in board[hero_x + 1][hero_y]):
            hero_x += 1
            status['steps'] -= 1
        elif movement == "a" and (". " in board[hero_x][hero_y - 1] or "= " in board[hero_x][hero_y - 1] or "qp" in board[hero_x][hero_y - 1] or "S " in board[hero_x][hero_y - 1] or "& " in board[hero_x][hero_y - 1] or "u " in board[hero_x][hero_y - 1]):
            hero_y -= 1
            status['steps'] -= 1
        elif movement == "d" and (". " in board[hero_x][hero_y + 1] or "= " in board[hero_x][hero_y + 1] or "qp" in board[hero_x][hero_y + 1] or "S " in board[hero_x][hero_y + 1] or "& " in board[hero_x][hero_y + 1] or "u " in board[hero_x][hero_y + 1]):
            hero_y += 1
            status['steps'] -= 1
        elif movement == "q":
            return False
        if status['life'] == 0:
            print("Your grandma grew impatient and turned you into a mushroom. Game Over.")
            # return False
        hero_x, hero_y, status = status_update(hero_x, hero_y, status)
        board = make_board(hero_x, hero_y, status)
        print(hero_x, hero_y, status['state'], status['level'])

if __name__ == '__main__':
    main()
