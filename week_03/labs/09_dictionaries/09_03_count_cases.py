'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''

def process_sentence(sentence):
    my_dict = {"Upper case": 0, "Lower case": 0, "Punctuation": 0}
    # I need loop to travel he whole center
    for letter in sentence:
        if letter == " ":
            pass
        elif letter.isupper():
            my_dict["Upper case"] += 1
        elif letter.islower():
            my_dict["Lower case"] += 1
        else:
            my_dict["Punctuation"] += 1

    return my_dict


# Script starts here
sentence = "I love to work with dictionaries!"
final_dict = process_sentence(sentence)
for key in final_dict:
    print(key, ": ", final_dict[key])

