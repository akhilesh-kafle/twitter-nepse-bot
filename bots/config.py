import tweepy
from dotenv import load_dotenv

load_dotenv()

def create_api():
    consumer_key = os.getenv("consumer_key")
    consumer_secret = os.getenv("consumer_key")
    access_token = os.getenv("consumer_key")
    access_token_secret = os.getenv("consumer_key")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
    except Exception as e:
        print("Error creating API", exc_info=True)
        raise e
    return api

create_api()