# ---- random hashtag generator ---- #
import random

# getting a list of words from the system dictionary
# NOTE: works for UNIX users only
word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()

# add the hashtag symbol and ensure the word is lowercase
print('#' + str(random.choice(words)).lower())