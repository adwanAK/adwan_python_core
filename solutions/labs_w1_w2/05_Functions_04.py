'''
Write a script that takes in a list and finds the max, min, average and sum.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_of_nums):
    max_num = max(list_of_nums)
    min_num = min(list_of_nums)
    average = sum(list_of_nums) / len(list_of_nums)
    print(f"max: {max_num}\nmin: {min_num}\navg: {average}")

stats(example_list)
