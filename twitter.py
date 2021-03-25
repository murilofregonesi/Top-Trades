import tweepy
import os


consumer_key = os.environ['API_KEY']
consumer_secret = os.environ['API_KEY_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class Twitter():
    api = tweepy.API(auth)

    @staticmethod
    def update_status(status: str):
        Twitter.api.update_status(status)
