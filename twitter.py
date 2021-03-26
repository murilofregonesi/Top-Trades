import tweepy
import os
import json


consumer_key = os.environ['API_KEY']
consumer_secret = os.environ['API_KEY_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

BRAZIL_WOE_ID = 23424768

class Twitter():
    api = tweepy.API(auth)

    @staticmethod
    def update_status(status: str):
        Twitter.api.update_status(status)

    @staticmethod
    def search_tweets(query: str) -> list:
        results = Twitter.api.search(q=query, lang='pt')
        return results

    @staticmethod
    def trending_topics():
        topics = Twitter.api.trends_place(BRAZIL_WOE_ID)
        topics = json.loads(json.dumps(topics[0]['trends'], indent=1))
        return topics

    @staticmethod
    def get_user(user):
        user = Twitter.api.get_user(user)
        return user

    @staticmethod
    def user_timeline(screen_name: str):
        timeline = Twitter.api.user_timeline(screen_name=screen_name)
        return timeline
