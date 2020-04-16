"""
@author: kateschneider
"""

import tweepy as tw
from tweepy import OAuthHandler
    
'''
User credentials to access twitter API
'''

access_token = [ACCESS TOKEN HERE]
access_token_secret = [SECRET ACCESS TOKEN HERE]
consumer_key = [CONSUMER KEY HERE]
consumer_secret = [SECRET CONSUMER KEY HERE]

'''
OAuth process, using the keys and token
'''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

'''
Creation of the actual interface, using authentication
'''
    
api = tw.API(auth)

'''
Functions
'''

def timeline(username):
   
    '''
    Function that returns a designated user's timeline.
    '''
    
    tweets_list = []
    
    for status in tw.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended", include_rts = True).items():
        tweets_list.append([status.full_text,status.created_at])
        
    return(tweets_list)

'''
Defined variables
'''
    
username = '[USERNAME HERE]'

'''
Printing tweets to a file
'''

f = open("timeline_[USERNAME HERE].txt",'w')
for tweet in timeline(username):
    print(tweet, file=f)


