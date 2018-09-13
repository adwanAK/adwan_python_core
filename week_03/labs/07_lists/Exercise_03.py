'''
Complete Exercise 10.1 (p.120) from the textbook.

Sum up all elements from a nested list of integers.

'''

# I decided to use recursion and it work


def nested_sum(param, _sum=0):
    for x in param:
        if isinstance(x, list):
            _sum = nested_sum(x,_sum)
        else:
            _sum = _sum + int(x)

    return(_sum)


_list = [1, [2, [3, 4], 5], 6, 7, 8]
print(_list)

print(nested_sum(_list))
