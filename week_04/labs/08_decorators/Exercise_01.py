'''
Write a decorator function that wraps text passed to it in <p> tags.

'''

def p_decorate(func):

    def wrapper(the_baby):
        return f"<p> {func(the_baby)} <p>"

    return wrapper


@p_decorate
def prettify(baby):
    return baby


if __name__ == '__main__':
    print(prettify("Nimer"))

#It will print :
# <p> Nimer <p>




