'''
Complete Exercise 8.4 (p.96) from the textbook by writing out the docstrings for the functions.

'''


def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# any_lowercase1() will return on first character which doesn't produce what we want


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# any_lowercase2() will only evaluate the letter 'c' not the parameter we are passing


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# any_lowercase3() will run through the whole string and return on last character value only.


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# This one works and I do not know why. I have to ask instructor


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# any_lowercase5() Not doing what we want.
# Checks every letter if it is not lowercased and returns boolean if all the
    # letters in string are lowercased or not;
