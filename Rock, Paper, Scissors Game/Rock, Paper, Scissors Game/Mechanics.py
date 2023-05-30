import random

def opponent(throw):
    move = random.randint(1, 5)
    if move == 1:
        print("Your opponent threw rock.")
    elif move == 2:
        print("Your opponent threw paper.")
    elif move == 3:
        print("Your opponent threw scissors.")
    elif move == 4:
        print("Your opponent threw lizard.")
    elif move == 5:
        print("Your opponent threw spock.")

    if throw == "r" and move == 1:
        print("It's a tie.\n")
    if throw == "p" and move == 2:
        print("It's a tie.\n")
    if throw == "s" and move == 3:
        print("It's a tie.\n")
    if throw == "l" and move == 4:
        print("It's a tie.\n")
    if throw == "k" and move == 5:
        print("It's a tie.\n")
    if (throw == "r" and move == 2) or (throw == "r" and move == 5):
        print("You lose!\n")
    if (throw == "p" and move == 3) or (throw == "p" and move == 4):
        print("You lose!\n")
    if (throw == "s" and move == 1) or (throw == "s" and move == 5):
        print("You lose!\n")
    if (throw == "l" and move == 1) or (throw == "l" and move == 3):
        print("You lose!\n")
    if (throw == "k" and move == 2) or (throw == "k" and move == 4):
        print("You lose!")
    if (throw == "r" and move == 3) or (throw == "r" and move == 4):
        print("You win!\n")
    if (throw == "p" and move == 1) or (throw == "p" and move == 5):
        print("You win!\n")
    if (throw == "s" and move == 2) or (throw == "s" and move == 4):
        print("You win!\n")
    if (throw == "l" and move == 2) or (throw == "l" and move == 5):
        print("You win!\n")
    if (throw == "k" and move == 1) or (throw == "k" and move == 3):
        print("You win!\n")