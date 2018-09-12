# '''
# Take in a number from the user and print "Monday", "Tuesday", ...
# "Sunday", or "Other" if the number from the user is 1, 2,... 7,
# or other respectively. Use a "nested-if" statement.

# '''
print("Type in a number between 1 and 7")

user_input = int(input())
while((user_input < 1) or (user_input > 7)):
    print("Wrong input, choose a number between 1 and 7")
    user_input = int(input())

if(user_input == 1):
    print("Monday")
if(user_input == 2):
    print("Tuesday")
if(user_input == 3):
    print("Wednesday")
if(user_input == 4):
    print("Thursday")
if(user_input == 5):
    print("Friday")
if(user_input == 6):
    print("Saturday")
if(user_input == 7):
    print("Sunday")
