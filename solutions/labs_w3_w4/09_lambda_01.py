'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

d_search = lambda x: x.startswith('D')
print([x.startswith('D') for x in names] == [d_search(x) for x in names])
