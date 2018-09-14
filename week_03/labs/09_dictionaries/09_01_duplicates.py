'''(
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.

Solution: http://thinkpython2.com/code/has_duplicates.py.

Source: Chapter "Dictionaries" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2011.html

'''

def has_dublicate(param):
    # param = str(param)
    _dict = {}
    for value in param:
        if value in _dict:
            return True
        _dict[value] = True
    return False


print(has_dublicate("hello"))
