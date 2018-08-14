'''
Using the tweepy package, build a script that classifies a twitter handle
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import os
import json
from pprint import pprint
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
user = api.get_user(handle)

num_followers = user.followers_count


print(f"{user.screen_name} has {num_followers} followers")
# here comes the classification. big thanks to www.chris.com and the
# folks who made these beautiful birds.
# http://www.chris.com/ascii/index.php?art=animals/birds%20(land)
if num_followers > 1000:
    print(r"""
                                                             | |
                                                             : |
                                                             ' :
                                                               ' .-'
                                                            _.
                             /^\                        _.-'_]\
             \              |   \__                 _.-'_.=\\|\]
              \             |_/\ \/\            _.-'_.='\\  \\ |
         `.    \            | \ \ \^\       _.-'_.=' \\  \\  \\|
   .       `.   \            \ \ \   \  _.-'_.=\  \\  \\  \\ |\    /
   :         `.  \            \ \     | | i\\  \\  \\  \\  \\| |  '
   |           `. \            \_\   /  | | \\  \\  \\  \\  \\ | / '
                                )_)  |  | |  \\  \\  \\  \\  \\|' /
   |                    _     .'.'   |  | |\  \\  \\  \\  \\ |\  /
   |                _.-'|\  .'.' _.;|\.-' |\\  \\  \\  \\  \\| |'
   :            _.-'_.1 | ||~;_-:;:;| |_.-' \\  \\  \\  \\  \ \]
   '        _.-'_.-'//| |_:| ; |:;:;| |  \\  \\  \\  \\  \\./\
        _.-'_.-'/  // | |::| ; |:;:;| |\  \\  \\  \\  \\  \ \/ .
    _.-'_.-'  //  //  | |::| ; |:;:;| |\\  \\  \\  \\  \\./\ . |
 . [_.-' //  //  //  /|_|::| ; |:;:;| | \\  \\  \\  \\  \ \/ | | .-'
   | // //  //  //  //' |::| ; |:;''Y |  \\  \\  \\  \\./\   | :
   |// //  //  //  //  /|::|_; Y    Y |\  \\  \\  \\  \ \/   : .
    / //  //  //  //  //|:''\~\Y    Y;|\\  \\  \\  \\-'\     . :
   | //  //  //  //  // Y    Y\Y;   :;| \\  \\  \\-'\`-'     : |
   |//  //  //  //  //  Y    :;:;    Y|  \\ _\\-'\`-' .      | |
    /  //  //  //  //  /Y;    Y.Y.  _L|\_.\\ _\`-' / /       | |
   |  //  //  //  //  //:;    _L`L-'_ Y'\.-'`     / /        |
   | //  //  //  //  //  Y._.-'Y Y-'  |          ' '
   |//  //  //  //  //  /;L    | |    :         / /
    /  //  //  //  //  // Y    | |    :          /
   :`-'/  //  //  //_.Y"  |    | |    |         '
   '   `='/_ // _/ '      |    | |
   .        ` "'          :    | |    :
   :    _.-'              :    \ |
   | .-'                  |     Y     |
   '                      |     :     |
                          .     :     |
                          :     :
                          |     6     :
                          |    5 5
                              4 : 4   |
                          :  3  :  3  |
                            2   :   2 :
                          :1    :    1:
                          :     :
                          |     6     :
                          |    5 5
                              4   4   |
                          :  3     3  |
                            2       2 :
                          :1         1:
                          |           |
""")
elif num_followers > 500:
    print(r"""
       /.\
       Y  \
      /   "L
     //  "/
     |/ /\_==================
     / /
    / /
    \/
""")
elif num_followers > 100:
    print(r"""
  '. (v)  .'
    '( \.'
      ``\
""")
elif num_followers > 10:
    print(r"""
   __(.)<
   \___)
""")
else:
    print(r"""
         .-"-.
       .'     '.
      /         \
     :           ;
     |           |
     :           :
      \         /
       `.     .'
         `~~~`
""")
