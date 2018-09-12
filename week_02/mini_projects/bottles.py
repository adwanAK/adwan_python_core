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


for x in range(99, 1, -1):
    print(x, "bottles of beer on the wall,", x, "bottles of beer.")
    print("Take one down and pass it around,", x-1, "bottles of beer on the wall")
    print("\n")

    if(x - 1 == 2):
        x = 2
        print(x, "bottles of beer on the wall,", x, "bottles of beer.")
        print("Take one down and pass it around,", x-1, "bottle of beer on the wall\n")
        break


print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall")

