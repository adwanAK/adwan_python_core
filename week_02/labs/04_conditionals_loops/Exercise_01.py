# '''
# Write a program that gets a number between 1 and 1,000,000,000
# from the user and determines whether it is odd or even using an if statement.
# Print the result.

# NOTE: We will be using the input() function. This is demonstrated below.

# '''

print("Please type in any number between 1 and 1,000,000,000")
user_input = int(input())
while((user_input < 1) or (user_input > 1000000000)):
    print("Wrong input, choose a number between 1 and 1,000,000,000")
    user_input = int(input())

if((user_input % 2) == 0):
    print("it is even")
else:
    print("it is odd")
