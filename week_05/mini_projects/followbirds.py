'''
Using the tweepy package, build a script that classifies a twitter handle
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''
import requests
import tweepy

auth = tweepy.OAuthHandler('GE8oeAmqFrMRL4OhvPtTKHfcg', '5OzRsCepFYrAtu37UrVlkGeX2PUrDBHGGFwIXcRaGw4OINdlIk')
auth.set_access_token('1030462573555019776-mU2lHEsZhPBzwkFnsxxGqNLxy12C8P', 'OQBxKFirkD8Ecc7Y7yhbNR4QaHGHgI6tEyiTI8t6Eii5m')
api = tweepy.API(auth)


users_dict = {'Google': [], 'Yahoo': [], 'SamsungMobile': [] }



def categorize(user):
    for friend in user.friends():
        users_dict[user.screen_name].append(friend.screen_name)


def find_match(_dict):
    for key, value in _dict.items():
        for item in value:
            print(f"{key}, {item}")
            #if item is in value Find matched in friends


########### Starts here
for user in users_dict:
    user = api.get_user(user)
    categorize(user)
find_match(users_dict)

#print(users_dict)

