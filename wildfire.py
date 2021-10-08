# -*- coding: utf-8 -*-

import os
import tweepy as tw
import pandas as pd
from ..credentials import consumer_key, consumer_secret, \
                          access_token, access_token_secret

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")

# Define the search term and the date_since date as variables
search_words = "#wildfires"
date_since = "2018-11-16"

tweets = tw.Cursor(api.search, 
                   q=search_words, 
                   lang='en',
                   since=date_since).items(5)


#for tweet in tweets:
#    print(tweet.text)
    
#[tweet.text for tweet in tweets]

#new_search = search_words + " -filter:retweets"

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]

tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location"])

#new_search = "climate+change -filter:retweets"