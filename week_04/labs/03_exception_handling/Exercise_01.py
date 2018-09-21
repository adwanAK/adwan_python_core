'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

while(True):
    try:
        user_input = int(input("Type in an integer please: "))
    except ValueError as exc: # Create object of the exception value type error
        exc.message ="Value type is not int [ValueError]."
        print(f"{exc.message}") # Customize exception message
        print()
    else:
        print(f"Correct! {user_input} is of type integer.")
        print()

