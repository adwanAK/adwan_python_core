'''
Write a function that takes in a list and finds the max, min, average and sum.

'''


def computeList(num_list, maximum, minimum, total):
    minimum = num_list[1]
    for num in num_list:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
        total += num
    return (total, maximum, minimum)


num_list = [880, 23, 245, 52, 3, 2, 45242, 200000, 5, 2, 67, 7]
maximum = 0
minimum = 0
total = 0
mytuple = computeList(num_list, maximum, minimum, total)
print("List: ", num_list)
print("sum: ", mytuple[0])
print("average", mytuple[0]/len(num_list))
print("max: ", mytuple[1])
print("minimum: ", mytuple[2])
