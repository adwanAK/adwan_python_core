'''
Print out every prime number between 1 and 100.

'''

# check for tricks:
# - http://www.counton.org/explorer/primes/checking-if-a-number-is-prime/
# - http://planetmath.org/howtofindwhetheragivennumberisprimeornot
primes_below_100 = [2, 3, 5, 7]

for num in range(1, 101):
    if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0) or (num % 7 == 0):
        pass
    else:
        print(num)
