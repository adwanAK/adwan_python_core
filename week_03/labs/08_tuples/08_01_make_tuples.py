'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''

def sort_list(param):
    param = list(param)
    param.sort()

    list_of_tuples = []
    for x in range(0, len(param), 2):
        list_of_two = param[x:x+2]

        if(len(list_of_two) % 2 != 0):
            list_of_two.append(0)

        tuple_of_two = tuple(list_of_two)
        list_of_tuples.append(tuple_of_two)

    for x in list_of_tuples:
        print(x)


t = [12, 4, 6, 88, 5, 3]
sort_list(t)

