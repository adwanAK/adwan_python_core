'''
--------------------------------------------------------
                99 BOTTLES OF BEER LYRICS
--------------------------------------------------------

https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

-- GOAL --
Create a program that prints out every line to the song
"99 bottles of beer on the wall." This should be a pretty simple program,
so to make it a bit harder, here are some rules to follow.

-- RULES --
1) If you are going to use a list for all of the numbers,
    do not manually type them all in. Instead, use a built in function.
2) Besides the phrase "take one down," you may not type in any
    numbers/names of numbers directly into your song lyrics.
3) Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
4) Put a blank line between each verse of the song.

'''

# possible solution
for n in range(99, 0, -1):
	glassware = ('bottles', 'bottles')
	if n == 2:
		glassware = ('bottles', 'bottle')
	elif n < 2:
		glassware = ('bottle', 'bottles')
	print(f"""{n} {glassware[0]} of beer on the wall, {n} {glassware[0]} of beer.
Take one down and pass it around, {n-1} {glassware[1]} of beer on the wall.\n""")
