# Project: Snake, Water, Gun Game
# Built by: Aryan

import random

# Step 1: Define your game logic function here
# def check_winner(user, computer):

# Step 2: Main game loop & user input below

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
yourdict = {"s" : 1, "w" : -1, "g" : 0}
revesedict = {1: "Snake", 0 : "gun", -1 : "water" }

you = yourdict[youstr]

print(f"You choosed {revesedict[you]}\nComputer Choosed {revesedict[computer]}")


if computer == you:
    print("Draw")
elif computer == -1 and you == 1:
    print("You win!")
elif computer == 1 and you == -1:
    print("You lose!")
elif computer == 1 and you == 0:
    print("You Win!")
elif computer == 0 and you == 1:
    print("You Lose!")
elif computer == 0 and you == -1:
    print("You Win!")
elif computer == -1 and you == 0:
    print("You Lose!")
else:
    print("Something went wrong!")