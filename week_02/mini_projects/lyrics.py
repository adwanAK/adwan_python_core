'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

Train using string methods and loops on an open-end mini-project!

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics

'''
lyrics = "My first verse:this is my 2nd verse:and my last verse"
chorus = "my chorus, my chorus"

verses = lyrics.split(":")
for verse in verses:
    print(verse)
    print(chorus, "\n")
