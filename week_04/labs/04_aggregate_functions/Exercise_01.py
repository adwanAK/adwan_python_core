'''
Build a simple aggregator function.

'''

def aggreg_func(_list):
    _str = ""
    for item in _list:
        _str += item

    return _str


_list = ["You", "ARE", "GOING", "SIDEWAYS"]
print(aggreg_func(_list))
