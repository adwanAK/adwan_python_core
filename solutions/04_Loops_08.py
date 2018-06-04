'''
Demonstrate the use of the "break" statement to exit a loop.

'''

import random


while True:  # this makes the while loop run forever
    num = random.randint(1, 1000)
    print(num)
    # to get out of here, we add a conditional with a break statement
    if num % 10 == 0:
        break

# Run the script a few times and see the different output
# as well as where it finally breaks out of the loop.
