"""
Created on Fri Nov 15 11:10:53 2019

@author: kateschneider
"""

import tweepy as tw
from tweepy import OAuthHandler
    
'''
User credentials to access twitter API
'''

access_token = '1149713584349470726-Jhg4lRPDr4KhQvTptLzln95EXJbvjp'
access_token_secret = 'kPbL8n2wqZJ467ci8F3UJfkPGSN56qqyFfu9xFq16UPnI'
consumer_key = 'fgLl7cExe3Wi3ufYPtqCsmtse'
consumer_secret = 'Q0wsv6CJ12gLjq9Gw3aq6eL259HWG9dOGuPe46xM4K60WIXPgR'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
    
api = tw.API(auth)

'''
Functions
'''

def tweet_search(search_words, date_since):
   
    '''
    Function that searches a defined hashtag and collects tweets from a defined date in a list format.
    '''
    
    tweets_list = []
    
    tweets = tw.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(5)
    
    for tweet in tweets:
        tweets_list.append(tweet.text)
        
    return(tweets_list)
    
def user_location(search_words, date_since):
    
    '''
    Function that accesses location information about the users tweeting with the defined hashtag.
    '''
    
    tweets = tw.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(5)
    
    users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
    
    return(users_locs)

'''
Defined variables
'''
    
search_words = "#cdnpoli"
date_since = "2019-11-01"

'''
Running the functions
'''

print(tweet_search(search_words, date_since))
print(user_location(search_words, date_since))

'''
Printing the tweets to a text file tweets.txt
'''

f = open("tweets.txt",'w')

print("List of tweets", file=f)
for tweet in tweet_search(search_words, date_since):
    print("Tweet no.", tweet_search(search_words, date_since).index(tweet)+1, file=f)
    print(tweet, file=f)

print("List of users and locations", file=f)
for user in user_location(search_words, date_since):
    print(user, file=f)
