# '''
# Print out every prime number between 1 and 100.

# '''


# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result


print("Prime numbers between 1 and 100 are:")

for num in range(1,100 + 1):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
            else:
                print(num)
