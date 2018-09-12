# '''
# Demonstrate the use of the "break" statement to exit a loop.

# '''
# """ to break from loop and stop its execution"""
#Below is a "while" loop to print out every third number counting backwards from 1000 to 1
# Here I am breaking out of the loop before it goes to negative range
x = 100
while x >= 1:
    x -= 3
    if(x < 0):
        break
    else:
        print(x)
