'''
Complete Exercise 10.7 (p.121) - the birthday paradox - from the textbook.

'''

def has_dublicate(param):
    #param = list(param)

    for x in param:
        if x in param[param.index(x)+1:]:
            return True

    return False


t= "dublicates_string_here"
print(has_dublicate(t))
