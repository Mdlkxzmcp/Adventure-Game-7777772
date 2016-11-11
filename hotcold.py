import random


def intro():
    print("""I, the mushroom, am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
    Cold           No digit is correct.
    Warm           One digit is correct but in the wrong position.
    Hot            One digit is correct and in the right position.
    I have thought up a number. You have 10 guesses to get it.""")


def number_generator():
    available = []
    for number in range(0, 10):
        available.append(number)
    first_number = random.choice(available)
    available.remove(first_number)
    second_number = random.choice(available)
    available.remove(second_number)
    third_number = random.choice(available)
    available.remove(third_number)
    the_number = (first_number, second_number, third_number)
    return the_number


def number_pick(the_number):
    try_number = 1
    while True:
        if try_number > 10:
            print("\nYou tried but you failed.\n\n")
            success = False
            return False
        guessed_number = []
        guess = input("\nGuess #{}: ".format(try_number))
        try:
            for number in guess:
                guessed_number.append(int(number))
        except ValueError:
            print("only numbers please~")
        tuple_number = tuple(guessed_number)
        if the_number == tuple_number:
            success = True
            return False
        else:
            for index, value in enumerate(tuple_number):
                if tuple_number[index - 1] == the_number[index - 1]:
                    print("Hot ", end="")
                elif tuple_number[index - 1] in the_number:
                    print("Warm ", end="")
                elif tuple_number[index - 1] not in the_number:
                    print("Cold ", end="")
            try_number += 1
    return success


def main():
    intro()
    success = number_pick(number_generator())
    return success
