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

def count_case(sentence):
    """Counts uppercase and lowercase letters, as well as punctuation of a str.

    Args:
        sentence (str): Any type of string that should be analyzed

    Returns:
        dict: Contains counts for uppercase, lowercase and punctuation
    """
    analyze_dict = {}
    for char in sentence:
        if char.isspace():
            pass  # avoid counting whitespace characters
        elif char.isupper():
            analyze_dict["uppercase"] = analyze_dict.get("uppercase", 0) + 1
        elif char.islower():
            analyze_dict["lowercase"] = analyze_dict.get("lowercase", 0) + 1
        # NOTE: this is insecure. try improving it using the 'string' module!
        else:
            analyze_dict["punctuation"] = analyze_dict.get("punctuation", 0) + 1
    return analyze_dict

# gather user input
sent = input("Say something: ")

# easy testing
# sent = "I love to work with dictionaries!"
print(count_case(sent))
