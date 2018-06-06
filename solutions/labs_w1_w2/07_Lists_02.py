'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.


'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]

# initialize result lists
same_same, different = [], []

# find which items appear in both lists
for x in list_one:
    if x in list_two:
        same_same.append(x)
    else:  # gets all items of list_one that only appear there
        different.append(x)

# to complete the 'different' list, we need to also add all items of
# list_two that are not present in list_one
different += [x for x in list_two if x not in list_one]

# NOTE: ^ here I am using a python list comprehension - essentially just
#       a quick way to write a for loop. If you did it using a normal
#       loop that is perfectly fine. If you want to know more about
#       list comprehensions, check the relevant section in the docs.

print(same_same, " but ", different)  # ;)
