'''
Complete Exercise 8.2 (p.95) from the textbook.

'''


def rotate_word(word, amount):
    ord_list = list(word)
    print(ord_list)
    char_list = list(word)
    for c in range(0, len(word)):
        ord_list[c] = ord(word[c]) + amount
        char_list[c] = chr(ord_list[c])

    print(char_list)


rotate_word("cheer", 7)
