'''
Write a script that finds the first vowel in a a user inputted string.

'''

vowels = list("aeiou")
user_string = input("Enter text for sophisticated analysis: ")

for c in user_string:  # look at each letter (incl. whitespace) of the string
    if c in vowels:  # check whether it's a vowel
        print(c)
        break
