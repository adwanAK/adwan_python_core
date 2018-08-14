'''
Complete Exercise 8.1 from the textbook (p.79).

Read the documentation of the string methods:
- https://docs.python.org/3/library/stdtypes.html#string-methods

Demonstrate below:
- strip
- replace
- find

'''

text = "Return the lowest index in the string where substring sub \
is found within the slice s[start:end]. Optional arguments start and end \
are interpreted as in slice notation. Return -1 if sub is not found."

print(text.find("the"))  # see text above ;)
print(text.replace("slice", "CHILL POOL"))  # 🏝
print(text.strip("R"))  # removing whitespace chars usually makes more sense :)
