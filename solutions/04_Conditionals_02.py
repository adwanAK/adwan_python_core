'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''

choice = int(input("Enter a number: "))

# because there are endless numbers that are NOT 1..7
# we catch that case first and avoid the code from running the other checks
if choice not in [1, 2, 3, 4, 5, 6, 7]:
    print("Other")
elif choice == 1:
    print("Monday")
elif choice == 2:
    print("Tuesday")
elif choice == 3:
    print("Wednesday")
elif choice == 4:
    print("Thursday")
elif choice == 5:
    print("Friday")
elif choice == 6:
    print("Saturday")
else:  # note that the code only ever comes here if choice == 7
    print("Sunday")
