temp = ""
_list = [1, 2, 3, 4, 5]
for theNumber in range(0, len(_list)):
    for other in range (theNumber, len(_list)):
        if _list[theNumber] < _list[other]:
            temp = _list[theNumber]
            _list[theNumber] = _list[other]
            _list[other] = temp

print(_list)
		
		
