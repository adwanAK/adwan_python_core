'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''

import random


# randomly generate a number between 1 and 100
secret_num = random.randint(1, 100)
print(secret_num)

guess = 0  # initialize with 0
while guess != secret_num:
    guess = int(input("Which number between 1 and 100 did I pick this time? "))

print("Good job! *clap, clap*")
