
def compute(_list):

    for i in range(0, len(_list)):
        for y in range(0, len(_list)):
            if y == i:
                continue
            elif _list[i] + _list[y] == 8:
                print(f"{_list[i]}, {_list[y]}")


_list = [1, 2, 6, 4, 5, 3]
compute(_list)
