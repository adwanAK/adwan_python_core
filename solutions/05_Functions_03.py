'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

import random


def open_fridge():
    is_open = random.choice([True, True, False])
    return is_open

def get_ingredient():
    if open_fridge():
        ingr = random.choice(["butter", "cucumber", "gummibears", "milk"])
        print(f"Fetched some {ingr}")
        return ingr
    else:
        print("Whoops, the fridge door is closed!")
        return

def mix_ingredients():
    ingr_1 = get_ingredient()
    ingr_2 = get_ingredient()
    if (ingr_1 != None) and (ingr_2 != None):
        print(f"frrrrrrrrrrrmmmrrrrrrr... Finished!")
        print(f"Enjoy your {ingr_1 + ingr_2} shake!")
    else:
        print("Please try again. Remember physics. Focus!")


mix_ingredients()
