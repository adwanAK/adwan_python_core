'''
Complete Exercise 10.1 from the textbook.

Sum up all elements from a nested list of integers.

'''

example_list = [[1, [44, 2, 7], 3], [4, 5, [6, [7, 5]]], [7, 8, 9]]

# referencing to a list outside of the function is sub-optimal
flat_list = []

def flatten_list(item, flat_list):
    if isinstance(item, int):
        flat_list.append(item)
    elif isinstance(item, list):
        for l in item:
            # add integers right away
            if isinstance(l, int):
                flat_list.append(l)
            # add all the items if it's a list containing only integers
            elif all(isinstance(x, int) for x in l):
                flat_list += l
            # if there are more lists inside the list,
            # call the function recursively
            else:
                flatten_list(l, flat_list)

# get one flat list using a bit of recursion
flatten_list(example_list, flat_list)
# getting the sum of the flattened list
summed = sum(flat_list)
print(summed)



# # TODO: currently not working recursion example
# # http://www.pythontutor.com/visualize.html#mode=edit

# example_list = [[1, [44, 2, 7], 3], [4, 5, [6, [7, 5]]], [7, 8, 9]]

# def sum_nested(x):
#     if isinstance(x, int):
#         return x
#     elif isinstance(x, list):
#         if all(isinstance(y, int) for y in x):
#             return sum(x) # problem: exits after reaching this the first time
#         else:
#             bucket_list = []
#             for y in x:
#                 if isinstance(y, list):
#                     return sum_nested(y)
#                 else:
#                     bucket_list.append(y)
#             return sum(bucket_list)

# print(sum_nested(example_list))
