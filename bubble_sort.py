temp = ""
_list = [1, 2, 3, 4, 5]
for index in range(0, len(_list)-1):
	if _list[index+1] > _list[index]:
		temp = _list[index]
		_list[index] = _list[index+1]
		_list[index+1] = temp

print(_list)
		
		
