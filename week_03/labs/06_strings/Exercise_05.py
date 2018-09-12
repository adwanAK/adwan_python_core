'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''
user_iput = input("type a word")

print(user_iput.upper())
print(user_iput.lower())

vowels = "aioue"
input_list = list(user_iput.lower())
for c in range(0, len(input_list)-1):
    if input_list[c] in vowels:
        input_list[c] = input_list[c].upper()

input_final = "".join(input_list)
print(input_final)
