from time import sleep
import tweepy 
from config import create_api
from nepse_data import *
import datetime

f = "last.txt"
def read_last_seen(f):
    file = open(f, 'r') 
    last_seen_id = int(file.read().strip())
    file.close()
    return last_seen_id 

def store_last_seen(f, last_seen_id):
    file= open(f, 'w') 
    file.write(str(last_seen_id)) 
    file.close()
    return

def reply():
    api = create_api()
    mentions = api.mentions_timeline(read_last_seen(f), tweet_mode='extended')
    for mention in reversed(mentions):
        scraped = scrapping()
        for i in range(len(scraped)):
            try:
                if mention.full_text.lower() == scraped[i]['Symbol'].lower() or mention.full_text.lower() in scraped[i]['Symbol'].lower() :
                    message = "As on : " + str(datetime.datetime.now()) + "\n" + i['Symbol'] + "@" + "LTP: " + i['LTP'] + "\n" + "%Change: " + i['% Change'] + "\n" + "Volume: " + i['Qty.']
                    api.update_status(message, mention.user.screen_name, in_reply_to_status_id=mention.id)
                    store_last_seen(f, mention.id)
                    api.create_favorite(mention.id)
                else:
                    api.update_status("Something went wrong!", in_reply_to_status_id=mention.id)
                    store_last_seen(f, mention.id)
                    api.create_favorite(mention.id)

            except tweepy.TweepError as error:
                if error.api_code == 187:
                    print('duplicate message')
                    break
                else:
                    raise error

while True:
    scrapping()
    reply()
    sleep(5)