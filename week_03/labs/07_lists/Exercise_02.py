'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]
common_list = []
diff_list = []

# make the lists of set objects for easier computations
set_one = set(list_one)
set_two = set(list_two)

set_common = set_one.intersection(set_two)
set_difference = set_one.symmetric_difference(set_two)

# print as a list
print("Common elements:", list(set_common))
print("Different elements:", list(set_difference))

