'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''

# a nice way to gather multiple use inputs at once
lower, upper = input("Enter lower and upper bound (both inclusive), \
separated by a space: ").split()

for n in range(int(lower), int(upper)+1):
    # input() collects str type, so we'll have to convert it to int
    # +1 because range() upper bound is exclusive
    print(n**2)
