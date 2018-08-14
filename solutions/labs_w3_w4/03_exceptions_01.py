'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

while True:
    try:
        n = input("Enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("That's not an integer! Please try again.")
print("Good job! You've entered an indeedteger!")
