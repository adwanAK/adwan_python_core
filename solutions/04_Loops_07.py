'''
Use a "while" loop to print out every third number counting backwards from 1000 to 1.

'''

count = 1000
iteration = 1

while count > 0:
    if iteration == 3:  # check whether it's a third number in the count
        # if so, print and reset the iteration to start over
        print(count)
        iteration = 1
    else:
        # if not, increment the iterator by 1
        iteration += 1
    count -= 1  # remember to decrease the count by 1
