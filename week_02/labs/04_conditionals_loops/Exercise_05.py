# '''
# Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
# 	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
# 	Print the results to the console.

# 	For example, if a user enters 1 and 100, the output should be:
# 		The sum is: 5050
# 		The average is: 50.5
# '''

print("Type in lower bound :")
lower = int(input())

print("Type in upper bound :")
upper = int(input())

sum = 0
n = 0
while lower <= upper:
    sum = sum + lower
    lower += 1
    n += 1

print("sum is: ", sum)
print("average is: ", sum/n)
