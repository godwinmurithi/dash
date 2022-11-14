# author = rhnvrm <hello@rohanverma.net>

import os
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):
    '''
    Generic Twitter Class for the App
    '''
    def __init__(self, query, retweets_only=False, with_sentiment=False):
        # keys and tokens from the Twitter Dev Console
        bearer_token = "AAAAAAAAAAAAAAAAAAAAALuNhAEAAAAAKAa5kwUJ%2B39JNRqHlwJh7MYxNcY%3DmwsyLWQQvB8zIwkS6nNvjxTwDObmHOg8rD6U33YmHWJE6ZaEHC"

        client = tweepy.Client(bearer_token, wait_on_rate_limit=True)
        # Attempt authentication
        try:
            #self.auth = OAuthHandler(consumer_key, consumer_secret)
            #self.auth.set_access_token(access_token, access_token_secret)
            self.query = query
            self.retweets_only = retweets_only
            self.with_sentiment = with_sentiment
            self.api = tweepy.API(self.auth)
            self.tweet_count_max = 100  # To prevent Rate Limiting
        except:
            print("Error: Authentication Failed")

    def set_query(self, query=''):
        self.query = query

    def set_retweet_checking(self, retweets_only='false'):
        self.retweets_only = retweets_only

    def set_with_sentiment(self, with_sentiment='false'):
        self.with_sentiment = with_sentiment

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self):
        tweets = []

        try:
            for response in tweepy.Paginator(client.search_all_tweets, 
                                 query = self.query,
                                 user_fields = ['username', 'public_metrics', 'description', 'location'],
                                 tweet_fields = ['created_at', 'geo', 'public_metrics', 'text'],
                                 expansions = 'author_id',
                                 start_time = '2022-08-01T00:00:00Z',
                                 end_time = '2022-08-15T00:00:00Z',
                              max_results=500):
            time.sleep(1)
            tweets.append(response)
           

            return tweets




        

        except tweepy.TweepError as e:
            print("Error : " + str(e))
