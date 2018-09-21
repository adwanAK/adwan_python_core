'''
Improve the decorator from the previous exercise by allowing it to take
a tag as an input - making it more general.

'''

def p_decorate(func):

    def wrapper(the_baby, tag):
        _tuple = tuple(func(the_baby, tag))
        return f"{_tuple[1]} {_tuple[0]} {_tuple[1]}"

    return wrapper


@p_decorate
def prettify(baby, tag):
    return baby, tag


'''
Script will print   <❤> Nimer <❤>
'''
if __name__ == '__main__':

    print(prettify("Nimer", "<❤>"))
