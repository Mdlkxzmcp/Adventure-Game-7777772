import os
import time
import sys
import tty
import termios
import random
import hotcold

# to do: boss zone triggering the hot cold game, item del after pick up, bug fixing, story between level 1&2 & 2&3.


def intro():
    """intro screen, self explanatory"""
    os.system('clear')
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
    print("Mdlkxzmcp, Rafał Sebestjanski and Pawel Potaczek present:::\n\n")
    time.sleep(1)
    print (""" ▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ █      ▄▀▀▀█▄    ▄▀▀▀▀▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄
█ ▄▀   █ ▐ ▄▀ ▀▄ █   █   █ █  █ ▄▀     █  ▄▀  ▀▄ █      █ █   █   █ ▐  ▄▀   ▐ █ █   ▐ █    █  ▐
▐ █    █   █▄▄▄█ ▐  █▀▀█▀  ▐  █▀▄      ▐ █▄▄▄▄   █      █ ▐  █▀▀█▀    █▄▄▄▄▄     ▀▄   ▐   █
  █    █  ▄▀   █  ▄▀    █    █   █      █    ▐   ▀▄    ▄▀  ▄▀    █    █    ▌  ▀▄   █     █
 ▄▀▄▄▄▄▀ █   ▄▀  █     █   ▄▀   █       █          ▀▀▀▀   █     █    ▄▀▄▄▄▄    █▀▀▀    ▄▀
█     ▐  ▐   ▐   ▐     ▐   █    ▐      █                  ▐     ▐    █    ▐    ▐      █
▐                          ▐           ▐                             ▐                ▐         """)
    time.sleep(3)
    print("\nCONTROL:\nA - move left\nS - move down\nD - move right\nW - move up\n")
    print("OBJECTS:\n@ - player\n# - tree\nA - mountain\n~ - water\n= - bridge\nqp- mushroom\n% - shoes\n& - meat\nu - basket\nS - life")
    while True:
        ready = input("\nAre you ready for the greatest adventure of your life? ").lower()
        if ready in ("yes", "y", "ye"):
            return False
        elif ready in ("quit", "q"):
            quit()
        else:
            time.sleep(1)
            continue


def make_board(hero_x, hero_y, status):
    """most complex function here but all it really does is creating the board itself. Look at comments inside to learn
    more about specific parts of the function"""
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
    bridge = dark_groundish + "= " + end_color
    basket = "u "
    lifes = blue + "S " + end_color
    shoes = bright_green + "% " + end_color
    meat = dark_groundish + "& " + end_color
    good_mushroom = dark_purple + "qp" + end_color
    bad_mushroom = bright_purple + "qp" + end_color

    # the creation of a (in this case) 25x25 board that is all trees at first
    board = [[tree] * board_size for num in range(board_size + 1)]
    walls = [tree, water, mountain]
    for x in range(1, board_size):
        for y in range(1, board_size - 1):
            board[x][y] = ground
            # now the insides are all turned into ground symbols so that they make a 24x24 board inside the 25x25 one

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
        # life placement
        if status['max_life'] == 3:
            board[1][23] = lifes

        # basket placement
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
        if status['max_life'] == 4:
            board[24][3] = lifes
        # shoes placement
        if status['boots'] == 0:
            board[15][18] = shoes
        elif status['boots'] > 0:
            board[15][18] = ground
        if status['basket'] == 1:
            board[2][22] = basket
        elif status['basket'] > 1:
            board[2][22] = ground

    elif status['level'] == 3:
        board[20][11] = "<^"
        board[20][12] = "~^"
        board[20][13] = "> "
        board[21][11] = "e3"
        board[21][12] = "33"
        board[21][13] = "e "
        board[22][11] = ".|"
        board[22][12] = "w|"

    # depending on the level a given number is set to the variables used in the random placement element generation
    if status['level'] == 1:
        number_of_good_shrooms = 8
        number_of_bad_shrooms = 4
        amount_of_meat = 4
    elif status['level'] == 2:
        number_of_good_shrooms = 15
        number_of_bad_shrooms = 8
        amount_of_meat = 5

    if status['level'] != 3:
        # the status dictionary has a state variable that tells this function if it should either create new elements...
        if status['state'] == 0:
            a = 0
            while a < number_of_good_shrooms:
                c = random.randint(1, 23)
                d = random.randint(1, 23)
                if board[c][d] == ground:
                    board[c][d] = good_mushroom
                    a += 1
                    status['g_shrooms'].append([c, d, 1])  # the "1" is changed to "0" when the element should be hidden
        # or load them from the already made list variable from within the status dictionary
        elif status['state'] == 1:
            a = 0
            while a < number_of_good_shrooms:
                if status['g_shrooms'][a][2] == 1:
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
            while a < amount_of_meat:
                c = random.randint(1, 23)
                d = random.randint(1, 23)
                if board[c][d] == ground:
                    board[c][d] = meat
                    a += 1
                    status['meat'].append([c, d, 1])
        elif status['state'] == 1:
            a = 0
            while a < amount_of_meat:
                if status['meat'][a][2] == 1:
                    board[status['meat'][a][0]][status['meat'][a][1]] = meat
                a += 1

    # if the player steps on an element that should dissapear the state of the element itself is changed
    if good_mushroom in board[hero_x][hero_y]:
        if status['mushrooms'] < status['limit']:
            status['mushrooms'] += 1
            for a in range(0, number_of_good_shrooms):
                if (status['g_shrooms'][a][0] == hero_x) and (status['g_shrooms'][a][1] == hero_y):
                    status['g_shrooms'][a][2] = 0

    if meat in board[hero_x][hero_y]:
        status['steps'] += 10
        for a in range(0, amount_of_meat):
            if (status['meat'][a][0] == hero_x) and (status['meat'][a][1] == hero_y):
                status['meat'][a][2] = 0

    if basket in board[hero_x][hero_y]:
        status['basket'] += 1

    if lifes in board[hero_x][hero_y]:
        status['max_life'] += 1
        status['life'] += 1
    status['state'] = 1

    if shoes in board[hero_x][hero_y]:
        status['steps'] += 50
        status['boots'] = 1

    board[hero_x][hero_y] = "@ "

    # after finally creating the whole board it's time to print it to the screen!
    for line in board:
        print("".join(line))

    return board


def getch():
    """black magic, do not touch"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
    # I don't even know man.


def print_table(inventory):
    """prints steps and life left as well as total number of collected mushrooms"""
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
    """function that changes various variables according to set condition. Takes hero_x, hero_y and status as args"""
    if status['mushrooms'] == 8 and status['level'] == 1:
        status['level'] = 2
        status['g_shrooms'] = []
        status['b_shrooms'] = []
        status['meat'] = []
        status['state'] = 0
        os.system('clear')
        print("\n\nAfter collecting all the eatible mushrooms in the area you venture deeeper into the dark forest...")
        time.sleep(3)
        os.system('clear')
        hero_x = 1
        hero_y = 1
    if status['mushrooms'] == 15 and status['state'] == 1:
        status['g_shrooms'] = []
        status['b_shrooms'] = []
        status['meat'] = []
        status['level'] = 3
        os.system('clear')
        print("\n\nYou have all the normal shrooms you need. Now, for the final mushroom that dwells", end="")
        print(" in the sacred section of The Dark Forest...")
        time.sleep(3)
        os.system('clear')
        status['state'] = 0
    if status['basket'] == 1:
        status['limit'] = 12
    if status['basket'] == 2:
        status['limit'] = 15
    if status['steps'] == 0:
        status['life'] -= 1
        hero_x = 1
        hero_y = 1
        status['steps'] = 50
    if status['boots'] == 1:
        status['steps'] += 50
    return hero_x, hero_y, status


def boss_fight(status):
    """function that calls the hotcold imported module once the player gets close enough to the last mushroom.
    Triggers either game_over or win_screen"""
    while True:
        success = hotcold.main()
        if success is True:
            return False
        elif success is False:
            status['life'] -= 1
            if status['life'] == 0:
                return False
    if status['life'] > 0:
        win_screen()
    else:
        game_over()


def win_screen():
    """shows the game won screen and asks the player about playing again"""
    print("You have collected all the mushrooms and satisfied your deceased and beloved grandma. Good job!!!")
    time.sleep(3)
    play_again = input("Do you want to play again? :> ").lower()
    if play_again in ('y', 'yes', 'ye'):
        main()
    else:
        quit()


def game_over():
    """shows the game over message and asks the player about trying again"""
    print("You lost to the one and only true mushroom.\n")
    time.sleep(3)
    play_again = input("Do you want to try again? ").lower()
    if play_again in ('y', 'yes', 'ye'):
        main()
    else:
        quit()


def main():
    status = {'steps': 50, 'max_life': 3, 'life': 3, 'level': 1, 'boots': 0, 'basket': 0, 'limit': 5,
              'mushrooms': 0, 'state': 0, 'g_shrooms': [], 'b_shrooms': [], 'meat': []}
    hero_x = 1
    hero_y = 1
    intro()
    board = make_board(hero_x, hero_y, status)
    status['state'] = 1
    while True:
        hero_x, hero_y, status = status_update(hero_x, hero_y, status)
        if status['level'] == 3 and hero_x in range(19, 24) and hero_y in range(10, 14):
            boss_fight(status)
        if status['level'] != 3:
            board = make_board(hero_x, hero_y, status)
            print_table(status)
        movement = getch()
        if movement == "w" and (". " in board[hero_x - 1][hero_y] or "= " in board[hero_x - 1][hero_y] or "qp" in board[hero_x - 1][hero_y] or "S "in board[hero_x - 1][hero_y] or "& " in board[hero_x - 1][hero_y] or "u " in board[hero_x - 1][hero_y] or "% " in board[hero_x - 1][hero_y]):
            hero_x -= 1
            if status['level'] != 3:
                status['steps'] -= 1
        elif movement == "s" and (". " in board[hero_x + 1][hero_y] or "= " in board[hero_x + 1][hero_y] or "qp" in board[hero_x + 1][hero_y] or "S " in board[hero_x + 1][hero_y] or "& " in board[hero_x + 1][hero_y] or "u " in board[hero_x + 1][hero_y] or "% " in board[hero_x + 1][hero_y]):
            hero_x += 1
            if status['level'] != 3:
                status['steps'] -= 1
        elif movement == "a" and (". " in board[hero_x][hero_y - 1] or "= " in board[hero_x][hero_y - 1] or "qp" in board[hero_x][hero_y - 1] or "S " in board[hero_x][hero_y - 1] or "& " in board[hero_x][hero_y - 1] or "u " in board[hero_x][hero_y - 1] or "% " in board[hero_x][hero_y - 1]):
            hero_y -= 1
            if status['level'] != 3:
                status['steps'] -= 1
        elif movement == "d" and (". " in board[hero_x][hero_y + 1] or "= " in board[hero_x][hero_y + 1] or "qp" in board[hero_x][hero_y + 1] or "S " in board[hero_x][hero_y + 1] or "& " in board[hero_x][hero_y + 1] or "u " in board[hero_x][hero_y + 1] or "% " in board[hero_x][hero_y + 1]):
            hero_y += 1
            if status['level'] != 3:
                status['steps'] -= 1
        elif movement == "q":
            return False
        board = make_board(hero_x, hero_y, status)
        if status['life'] == 0:
            print("Your grandma grew impatient and turned you into a mushroom. Game Over.")
            return False

if __name__ == '__main__':
    main()
