'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
print([x.startswith('D') for x in names])

############## using lambda ...plus map and list to print nicely
result = list(map(lambda x: x.startswith('D'), names))

print(result)

