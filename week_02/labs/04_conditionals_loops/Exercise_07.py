# '''
# Use a "while" loop to print out every third number counting backwards from 1000 to 1.

# '''

x = 100
third_number = 0
while x >= 1:
    x -= 3
    if(x < 0):
        continue
    else:
        print(x)
