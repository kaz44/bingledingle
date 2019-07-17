import tweepy
from  datetime import datetime
import schedule
import time
import random

CONSUMER_KEY = "zpBd16Gq8aYow5fVv0LwTDngm"
CONSUMER_SECRET = "bKVuhwWpYUiigjmy4wAWzKWLByqRhJ8RQDiKhXziahZLQvLjnv"
ACCESS_KEY = "1151304700366602246-CqSGJje9oXJVTzr8ZV0c0ne4Q5JQLP"
ACCESS_SECRET = "LY8Tk12cbHrZnzyTou0Q6TthFfCEqmaygwKHSygCwZG5W"

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

print('bong')

def job():
    print('bong  bong')
    now = datetime.now()
    hour = now.hour % 12
    if hour == 0:
        hour = 12
    msg = "BINGLE " * (hour-1) + "BONG"    

    #api.update_status(status=msg)
    try:
        result = api.update_status(msg)
        print( result)
    except Exception as e:
        print( e)
    finally:
        print ("Done.")

schedule.every().minute.at(":00").do(job)

FILE_NAME = "last_seen_id.txt"

def retrieve_last_seen_id(filename):
    f_read  = open(filename,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, filename):
    f_write = open(filename,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return 

# def convert_cryptic(message):
    

def reply_to_tweets():
    print('replying  to  tweets...')
    last_seen_id  = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(since_id = last_seen_id)
    for mention in reversed(mentions):
        #last_seen_id =  mention.id
        store_last_seen_id(mention.id,FILE_NAME)
        if '#bongbong' in mention.text.lower():
            print('found bongbong')
            print('responding back...')
            try:
                api.update_status('@' + mention.user.screen_name + 
                ' BINGLE DINGLE ' +  'BINGLE'*random.randint(0,10) + 'BONG BONG', mention.id)
            except:
                print('cant do it')

while True:
    schedule.run_pending()
    reply_to_tweets()
    time.sleep(1)
