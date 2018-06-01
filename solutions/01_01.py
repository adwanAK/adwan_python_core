'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
    - Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        * How helpful are the error messages?
    - Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
    - Use the interpretor to perform simple math.
    - Calculate how many seconds are in a year.
'''

# 1
print('hello world')

# 2
# open terminal app and type: python3
# this opens the interpreter
# then in your interpreter type
print('hello world!')

'''
# 3
- syntax errors:
    * print('hello world)  # missing closing quotation mark
    * very ;)
-
'''

help('print')
'''
OUTPUT:

Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
'''

# how many seconds in a year
seconds_per_minute = 60
seconds_per_hour = seconds_per_minute * 60
seconds_per_day = seconds_per_hour * 24
seconds_per_year = seconds_per_day * 365.2422  # accounting for leap years
print(seconds_per_year)
