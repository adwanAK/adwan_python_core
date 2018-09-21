'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


# Takes list returns tuple of index, item

def my_enumrate(_list):
    list_of_tuples = []

    for item in _list:
        list_of_two = [_list.index(item), item]
        my_tuple = tuple(list_of_two)
        list_of_tuples.append(my_tuple)

    # Returns tuple of index, item pair
    return tuple(list_of_tuples)


if __name__ == '__main__':

    words = ["Kadri", "Adwan", "Tony"]
    print_enu = my_enumrate(words)
    print(print_enu)
