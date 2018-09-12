# '''
# Write a script that prints out all the squares of numbers
# from a user inputed lower to a user inputed upper bound.

# Use a for loop that demonstrates the use of the range function.

# '''

print("input lower: ")
lower = int(input())

print("input upper: ")
upper = int(input())

print("-----squares----")
for x in range(lower, upper+1):
    print(x**2)
