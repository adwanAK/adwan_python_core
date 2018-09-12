'''
Write a script that finds the first vowel in a a user inputted string.

'''

user_input = input("Type a word with vowels: ")
vowels = list("aioue")
for c in user_input:  # look at each letter (incl. whitespace) of the string
    if c in vowels:  # check whether it's a vowel
        print(c)
        break
