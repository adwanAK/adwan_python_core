_list = [1, 6, 2, 3, 4, 5]
temp = ""
print(f"Original list {_list}")
for i in range(0, len(_list)//2):
    temp = _list[i]
    print(temp)
    print(f"Before swap: i:{i} _list[i]:{_list[i]}")
    _list[i]= _list[len(_list) - i -1]
    _list[len(_list)-i - 1] = temp
    print(f"After swap: _list:[i]={_list[i]}  _list[len(_list) -i -1]: {_list[len(_list)-i-1]}")
    print(_list)
