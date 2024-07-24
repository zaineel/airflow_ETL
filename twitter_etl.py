import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    
    access_key = 'gaxHtrwjNXVMESTcouVMu08pO'
    access_secret = 'yAY23s5IN0nO7pzzJjyPHuBgxrDLbQYPeE4UB4hFIdjQAeCJF4'
    consumer_key = '1454953129993293829-r6WwxdI4TYnEHgOFyJfXwlz9UD5ydw'
    consumer_secret = 'okjMwzWjjwUAtDH7B5jx0FwrcSXxSuwjvmSxxzBrUGhqA'

    #twitter authentication
    auth = tweepy.OAuth1UserHandler(consumer_key=access_key, consumer_secret=access_secret)
    auth.set_access_token(key=consumer_key, secret=consumer_secret)

    #creating an API object
    api = tweepy.API(auth=auth)

    #getting tweets from a particular user
    tweets = api.user_timeline(screen_name='@elonmusk', count=200, include_rts=False, tweet_mode='extended')
    print(tweets)