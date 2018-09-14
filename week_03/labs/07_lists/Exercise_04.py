'''
Complete Exercise 10.2 (p.120) from the textbook.

'''

def cumsum(t):
    _sum = 0
    cumulative = [0]*len(t)
    t = list(t)

    for x in t:
        for y in range(0, t.index(x)+1):
            _sum = _sum + t[y]

        cumulative[t.index(x)] = _sum
        _sum = 0


    return cumulative




t = [1, 2, 3]

print("original list:", t)
print("After cumsum :", cumsum(t))
