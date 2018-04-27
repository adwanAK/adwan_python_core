# ----- reproduce the functionality of python's enumerate() ----- #

# define a function my_enumerate() that takes an iterable as input
# and yields the element and its index

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

twelve_monkeys = ['James', 'Jeffrey', 'Jose', 'Scarface', 'Tiny',
					'Kathryn', 'L.J.', 'Marilou', 'Louie', 'Teddy',
					'Fale', 'Wayne']

print([x for x in my_enumerate(twelve_monkeys)])
print([x for x in enumerate(twelve_monkeys)])
print(my_enumerate(twelve_monkeys))
print(enumerate(twelve_monkeys))
