'''
Complete Exercise 12.1 from the textbook (p. 115).

Write a function called sumall that takes any number of arguments
and returns their sum.

'''

def sumall(*args):
    """Calculates the sum of a variable amount of inputs

    Args:
        *args: Numbers to be summed

    Returns:
        int: The sum of all inputs in *args
    """
    return sum(args)

# testing
print(sumall(1, 2, 3, 4, 5, 6))
