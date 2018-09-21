temp = ""
_list = [1, 2, 3, 6, 4, 5]
for i in range(0, len(_list)):
    for x in range (i, len(_list)):
        if _list[i] < _list[x]:
            temp = _list[i]
            _list[i] = _list[x]
            _list[x] = temp

print(_list)
		
		
