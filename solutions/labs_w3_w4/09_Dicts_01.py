'''
Complete Exercise 11.3 from the textbook (p. 104).

Modify print_hist to print the keys and their values in alphabetical order.

def print_hist(h):
    for c in h:
        print c, h[c]

'''

def print_hist(input_dict):
    """Prints a dictionary's key-value pairs alphabetically by keys.

    Args:
        input_dict (dict): a dict with strings as keys
    """
    for key in sorted(input_dict.keys()):
        print(key, input_dict[key])


# testing
print_hist({'p': 1, 'a': 1, 'r': 2, 'o': 1, 't': 1})
