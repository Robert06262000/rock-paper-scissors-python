from Mechanics import opponent

print("Let's play rock paper scissors.")
while True:
    throw = input("\nEnter your first throw (rock, paper, scissors, lizard, spock; or enter r, p, s, l, k).")
    if throw == "rock" or throw == "r":
        result = "r"
        opponent(result)
    elif throw == "paper" or throw == "p":
        result = "p"
        opponent(result)
    elif throw == "scissors" or throw == "s":
        result = "s"
        opponent(result)
    elif throw == "lizard" or throw == "l":
        result = "l"
        opponent(result)
    elif throw == "spock" or throw == "k":
        result = "k"
        opponent(result)
    else:
        print("Invalid throw.")
        continue
    choice = input("Would you like to play again? (y/n)")
    if choice.lower() == "n":
        break

print("Thank you for playing!")