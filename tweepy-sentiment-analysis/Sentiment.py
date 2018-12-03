#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 13:01:37 2018

@author: antoniosj
"""
import re 
import tweepy 
from textblob import TextBlob 
import TwitterClient as tc

def clean_tweet(self, tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(self, tweet):
    analysis = TextBlob(clean_tweet(self, tweet))
    
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'
    
def get_tweets(self, query, count = 10):
    
    tweets = []
    
    try: 
        fetched_tweets = self.api.search(q = query, count = count)
        
        for tweet in fetched_tweets: 
        
            parsed_tweet = {}
            #saving text from tweet
            parsed_tweet['text'] = tweet.text
            #saving sentiment
           
            parsed_tweet['sentiment'] = get_tweet_sentiment(self, tweet.text)
            
            if tweet.retweet_count > 0:
                
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else: 
                tweets.append(parsed_tweet)
                
        return tweets
    except tweepy.TweepError as e:
        print("Error: " + str(e))
        
def main():
    
    api = tc.TwitterClient()
    
    tweets = get_tweets(api, query = 'Donald Trump', count = 200)
    
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))) 
  
    # printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
  
    # printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 
  
if __name__ == "__main__": 
    # calling main function 
    main()