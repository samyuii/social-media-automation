


import tweepy


# Set up Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_secret = "your_access_secret"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


# Post a tweet
tweet = "Automating tweets with Python! #TwitterAutomation"
api.update_status(tweet)