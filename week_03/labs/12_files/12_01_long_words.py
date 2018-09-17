'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

with open('words.txt', 'r') as f:
    data = f.read()

    # create a list of word by splitting by EOL End Of Line
    data_list = data.split("\n")

    # Loop through the list and print words with characters > 20
    for word in data_list:
        if len(word) >= 20:
            print(word)

