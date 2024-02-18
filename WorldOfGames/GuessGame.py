# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the

import random

with open('Difficulty.txt', 'r') as file:
    difficulty = int(file.read())


def generate_number():
    number = random.randint(1, difficulty)
    secret_number = number
    # to remove, only for testing
    # print("Random number between 1 and 5:", secret_number)
    return secret_number


def get_guess_from_user():
    while True:
        try:
            guess = int(input("Add your guess, choose a number between 1 to " + str(difficulty) + ": "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print("choose a number between 1 to " + str(difficulty))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_results(guess, secret_number):
    # print(guess, secret_number)
    if guess == secret_number:
        print("Correct! nice guess")
        return True
    else:
        print("Wrong guess")
        return False


def play():
    secret_number = generate_number()
    guess = get_guess_from_user()
    result = compare_results(guess, secret_number)
    if result is True:
        print(result)
        return True
    else:
        print(result)
        return False


play()
