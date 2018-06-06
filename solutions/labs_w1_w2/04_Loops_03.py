'''
Using a "for-loop", print out all even numbers from 1-100.


'''

for num in range(1, 101):  # upper bound is exclusive, but we want 100
    if num % 2 == 0:
        print(num)
