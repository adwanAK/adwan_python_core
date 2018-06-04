'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''

# C = (F - 32) / 1.8
fahrenheit = float(input("Enter degree in Fahrenheit: "))
celsius = (fahrenheit - 32) / 1.8
print(celsius)
