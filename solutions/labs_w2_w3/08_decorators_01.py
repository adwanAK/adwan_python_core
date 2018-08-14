'''
Write a decorator function that wraps text passed to it in <p> tags.

'''

def p_decorate(func):
    def func_wrapper(text):
        return f"<p>{func(text)}</p>"
    return func_wrapper

@p_decorate
def add_location(location):
    return f"I really like hanging out in {location}"


print(add_location('Barcelona'))
