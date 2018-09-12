'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''
import random

print("Game: guess number between 1 and 100 and type here: ")
x = random.randint(1, 100)
user_input = int(input())
if(user_input != x):
    while(user_input != x):
        print("Wrong! try again: ")
        user_input = int(input())


print("Congratulations! You guessed it right", user_input)

