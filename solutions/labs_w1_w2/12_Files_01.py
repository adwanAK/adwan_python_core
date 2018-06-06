'''
Complete Exercise 9.1 (p.84) from the textbook.

Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).

'''

with open('words.txt', 'r') as f:
    for line in f.readlines():
        line = line.rstrip()  # remove newline char
        if len(line) > 20:
            print(line)
