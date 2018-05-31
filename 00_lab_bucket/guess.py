import random

# randomly generate a number between 1 and 100
secret_num = random.randint(1, 100)
print(secret_num)

guess = 0  # initialize with 0
while guess != secret_num:
    guess = int(input("Guess which number between 1 and 100 I picked this time: "))

print("Good job! *clap, clap*")
