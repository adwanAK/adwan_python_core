'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.
'''

user_input = input("Enter some text: ")

print(user_input.upper())
print(user_input.lower())

weird_case = ""
for c in user_input:
    if c in list("aeiou"):
        weird_case += c.lower()
    else:
        weird_case += c.upper()
print(weird_case)
