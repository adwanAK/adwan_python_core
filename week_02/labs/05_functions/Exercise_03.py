# '''
# Write a program with 3 functions. Each function must call
# at least one other function and use the return value to do something.

# '''


def makeCapital(param):
    print("Capital case : ", str(param).upper())


def makeSmall(param):
    print("Small case: ", str(param).lower())


def takeInput(param):
    return (makeCapital(param), makeSmall(param))


user_input = input("Type a word and program will display lower and in upper case")
takeInput(user_input)
