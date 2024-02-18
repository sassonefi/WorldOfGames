# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.

import random
import time
import os

with open('Difficulty.txt', 'r') as file:
    difficulty = int(file.read())


def generate_sequence():
    random_list = [random.randint(1, 101) for _ in range(difficulty)]
    print(random_list)
    time.sleep(0.7)
    #os.environ['TERM'] = 'xterm-color'
    os.system('clear')
    return random_list


def get_list_from_user():
    # Initialize an empty list to store the user input
    user_list = []

    # Ask the user to enter the numbers
    for i in range(difficulty):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                user_list.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return user_list


def is_list_equal(user_list, random_list):
    # Check if the lengths of the lists are equal
    if len(user_list) != len(random_list):
        return False

    # Compare each element of the lists
    for i in range(len(user_list)):
        if user_list[i] != random_list[i]:
            print("Lists are NOT equal")
            return False

    # If all elements are equal, return True
    print("Lists are equal")
    return True


def play():
    sequence = generate_sequence()
    # just for testing
    #print("Random list:", sequence)
    user_input_list = get_list_from_user()
    print("User input list:", user_input_list)
    is_equal = is_list_equal(user_input_list, sequence)
    if is_equal is True:
        #print(is_equal)
        return True
    else:
        #print(is_equal)
        return False


play()
