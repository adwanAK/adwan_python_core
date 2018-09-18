'''
Download http://thinkpython2.com/code/anagram_sets.py.
You’ll see that it creates a dictionary that maps from a sorted string
of letters to the list of words that can be spelled with those letters.
For example, 'opst' maps to the list:
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”;
read_anagrams should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
from anagram_sets import all_anagrams, signature
import shelve

def store_anagrams(anag_map):
    # take dictionary anagram_map
    # open shelf
    # store dictionary key and values in shelf

    with shelve.open("shelf.txt",'c') as shelf:
        for anagram, anagram_list in anag_map.items():
            shelf[anagram] = anagram_list


def read_anagrams(filename, word):
    # take stirngs file name (shelf file) & word to look up
    # open shelf
    # try and except to handle KeyError when sig is not found

    with shelve.open("shelf.txt",'c') as shelf:
        sig = signature(word)
        try:
            return shelf[sig]
        except KeyError:
            return []



if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    store_anagrams(anagram_map)


    # should return list of anagram for aah
    print(read_anagrams("shelfff.txt", "aah"))

    # should return [] because it does not exist in shelf
    print(read_anagrams("shelfff.txt", "8888888888888888"))
