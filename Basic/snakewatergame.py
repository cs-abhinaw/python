import random

"""
1 for snake
-1 for water
0 for gun
"""

# Computer randomly chooses
computer = random.choice([1, -1, 0])

# Dictionary for user input and reverse mapping
youDict = {"snake": 1, "water": -1, "gun": 0}
reversedDict = {1: "snake", -1: "water", 0: "gun"}

# User input
youstr = input("Enter your choice (snake / water / gun): ").lower()

# Validate input
if youstr not in youDict:
    print("Invalid input.")
else:
    you = youDict[youstr]

    print(f"You chose {reversedDict[you]} | Computer chose {reversedDict[computer]}")

    if computer == you:
        print("It's a draw!")

    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("You win!")

    else:
        print("You lose!")
