'''
Using the tweepy package, fetch and save the *JSON of all tweets* of
a user to a tweets.json file

Hint: utilize tweepy's Cursor object and the ._json attribute.

'''

import os
import json
import tweepy


# fetch the secrets from our virtual environment variables
CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']
# authenticate to the service we're accessing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# create the connection
api = tweepy.API(auth)

# define a handle to inspect for quicker reference
handle = 'twitter'  # for example purposes; prop any handle you want!

tweet_list = []
# using the Cursor object
for status in tweepy.Cursor(api.user_timeline, id=handle).items():
    tweet_list.append(status._json)

# write to JSON file
with open('tweets.json', 'w') as f:
    json.dump(tweet_list, f)
