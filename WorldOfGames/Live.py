def welcome(name):
    print("Hello " + name + " and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.\n")


def load_game():
    print("Please choose a game to play: \n"
        "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
        "2. Guess Game - guess a number and see if you chose like the computer\n" 
        "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    game_selected = None
    game_difficulty = None

    while game_selected not in [1, 2, 3]:
        try:
            game_selected = int(input("Please enter the game number (1, 2, or 3): "))
            if 1 <= game_selected <= 3:
                break
            else:
                print("You selected wrong number")
        except ValueError:
            print("You entered invalid input")

    with open('Difficulty.txt', 'r') as file:
        difficulty = int(file.read())
        while game_difficulty not in range(1, difficulty):
            try:
                game_difficulty = int(input("Please choose game difficulty from 1 to " + str(difficulty) + ": "))
                if 1 <= game_difficulty <= difficulty:
                    break
                else:
                    print("You selected wrong number")
            except ValueError:
                print("You entered invalid input")

    print("you selected to play game " + str(game_selected) + " with difficulty level " + str(game_difficulty))

    return game_selected, game_difficulty
