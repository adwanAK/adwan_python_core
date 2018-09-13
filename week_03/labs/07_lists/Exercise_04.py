'''
Complete Exercise 10.2 (p.120) from the textbook.

'''

def cumsum(param):
    _sum = 0
    cumulative = [0]*len(param)
    param = list(param)

    for x in param:
        for y in range(0, param.index(x)+1):
            _sum = _sum + param[y]

        cumulative[param.index(x)] = _sum
        _sum = 0


    return cumulative




t = [1, 2, 3]

print("original list:", t)
print("After cumsum :", cumsum(t))
