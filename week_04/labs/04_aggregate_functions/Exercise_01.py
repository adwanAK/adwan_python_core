'''
Build a simple aggregator function.

'''

def add_vars(x: int, y: int, z: int) -> int:
    return x + y + z

print(add_vars(1, 2, 3))

# NOTE: keep in mind that python remains dynamically typed
# what we do up there is called 'type hinting' and only
# has an effect when run with third-party type checkers like mypy
#print(add_vars(1, 2, 3.0))
