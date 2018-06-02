'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''

#collect input from the user
user_input = int(input("Enter a number between 1 and 1,000,000,000 \
to see whether is it odd or even: "))

#print the number the user inputed to the console
print(f"The user input is {user_input}")

#complete the rest of the code to determine whether it is odd or even
if user_input % 2 == 0:
    print(f"{user_input} is EVEN")
else:
    print(f"{user_input} is ODD")
