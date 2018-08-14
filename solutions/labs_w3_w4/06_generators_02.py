'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)

# creating the generator expression
div_gen = (n for n in nums if (n % 1111 == 0))
# checking on its output by using a listcomp
print([n // 1111 for n in div_gen])

# keep in mind that you can run any function on the elements that the
# generator expression yields. this is cool stuff!
