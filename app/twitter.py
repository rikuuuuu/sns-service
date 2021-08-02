#tweetを投稿
import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

# 取得した各種キーを格納-----------------------------------------------------
consumer_key = os.getenv('TW_CONSUMER_KEY')
consumer_secret = os.getenv('TW_CONSUMER_SEC_KEY')
access_token = os.getenv('TW_ACCESS_TOKEN')
access_token_secret = os.getenv('TW_ACCESS_SC_TOKEN')
me_accout_id = os.getenv('ME_ACCOUT_ID')

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#-------------------------------------------------------------------------

def get_tweet():
    tweets = api.user_timeline(me_accout_id, count=200, page=1)
    for tweet in tweets:
        print('user : ', tweet.user.screen_name)
        print(tweet.text)
    return

def post_tweet(text):
    api.update_status(text)
    return

def post_tweet_with_media(text: str, images: list):
    # api.update_with_media(filename=filename, status=text)
    media_ids: list = []
    for image in images:
        img = api.media_upload(image)
        media_ids.append(img.media_id)
    api.update_status(status=text, media_ids=media_ids)
    return