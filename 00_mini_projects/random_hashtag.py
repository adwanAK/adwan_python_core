'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''

import random


# getting a list of words from the system dictionary
# NOTE: works for UNIX users only
word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()

# add the hashtag symbol and ensure the word is lowercase
print('#' + str(random.choice(words)).lower())
