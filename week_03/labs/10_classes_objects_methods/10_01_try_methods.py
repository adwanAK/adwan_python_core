'''
Read the documentation of the string methods at:
http://docs.python.org/3/library/stdtypes.html#string-methods.
You might want to experiment with some of them to make sure you
understand how they work. strip and replace are particularly useful.

The documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate
optional arguments. So sub is required, but start is optional, and if
you include start, then end is optional.

Demonstrate below:
- strip
- replace
- find

Source: Exercise in chapter "Strings" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2009.html

'''

str_1 = "Hello# Worl#d#"
print("")
print(str_1.strip("#"))

print(str_1.replace("#",""))

print(f"'W' Found at position:{str_1.find('W')}")

print(f"'l' is found at {str_1.find('l', 5)} where we started search at index 5")




