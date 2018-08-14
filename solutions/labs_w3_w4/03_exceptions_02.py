'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file_name = 'integers.txt'
try:
    fh = open(file_name, 'r')
    first = int(fh.readline())
except IOError:
    print(f'cannot open {file_name}')
except ValueError:
    print("please make sure the first line contains an integer")
else:
    print(first + 1)  # perform a calculation
    fh.close()
