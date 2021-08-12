#%% 1
# set parent folder access for import keys
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import tweepy
import logging
# import keys from parent folder to avoid upload to github
from twitter_auth import consumer_key, consumer_secret, access_token, access_token_secret

logger = logging.getLogger()
#%% 2

def create_api():
        
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)
    
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api



