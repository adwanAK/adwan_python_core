'''
Use the external python module 'markovify' to create short text snippets
of your favorite text resource.

https://github.com/jsvine/markovify

CHALLENGE: rewrite it using `markovbot` to let the bot tweet
some wisdom once in a while!
https://github.com/esdalmaijer/markovbot

'''

import os
import markovify

# gets current directory path
dirname = os.path.dirname(os.path.abspath(__file__))
book = os.path.join(dirname, 'freud.txt')

with open(book, 'rb') as f:  # import as a bytes like object
    text = str(f.read())

model = markovify.Text(text)

# generate a freudian quote
quote = model.make_sentence()
print(quote)


# EXAMPLE OUTPUT

# We may say that the Professor was going to a strict and crabbed father
# who lived\nunhappily with his whole family; at half-past eleven.

# Nothing can be\nbrought to an orgasm, and thus avoid all\nobscurities
# connected with the latent dream thought.
