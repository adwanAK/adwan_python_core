'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''

def tuplify(input_list):
    """Slices a list into tuples of two.

    If the list has an odd number of ints, it adds 0 to the last pair

    Args:
        input_list (list): a list of integers

    Returns:
        tuple_list (list): a list of tuples of two
    """
    tuple_list = []
    input_list.sort()
    for i in range(0, len(input_list), 2):
        list_slice = input_list[i:i+2]
        if len(list_slice) % 2 != 0:
            list_slice.append(0)
        tup = tuple(list_slice)
        tuple_list.append(tup)
        print(tup)
    return tuple_list

# testing the function
num_list = [1, 7, 3, 5, 4, 6, 2]
print(tuplify(num_list))
