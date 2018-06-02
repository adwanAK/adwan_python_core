'''
Using a "while" loop, find the sum of numbers from 1-100.
Print the sum to the console.

'''

# initializing our variables
count, count_sum = 0, 0

while count <= 100:
    count_sum += count
    count += 1

print(count_sum)

# NOTE: this number is called the nth triangular number
#       e.g. 5050 is the 100th triangular number
#       Check out the following picture if you want to know more:
#       https://bit.ly/2HaYbKh
