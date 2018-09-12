# '''
# Using a "while" loop, find the sum of numbers from 1-100.
# Print the sum to the console.

# '''
x = 1
total = 0
while x <= 100:
    total = total + x
    x += x

print("total is: ", total)
