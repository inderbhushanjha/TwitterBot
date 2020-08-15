import tweepy
import time

from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) #to stay in the twitter access limit and notify when twitter will stop sending data for how much seconds.

FileName = 'last_id.txt'

'''def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id'''

'''def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return'''

def like_hashtags(hashtag,username):
    #last_seen_id = retrieve_last_seen_id(FILE_NAME)
    NumberTweets = 400
    for tweet in tweepy.Cursor(api.search, hashtah).items(NumberTweets) or tweepy.Cursor(api.search_users ,username).items(NumberTweets):
        try:
           tweet.favorite()
           time.sleep(15)

        except tweepy.TweepError as error:
            print(error.reason)
        except StopIteration:
            break


while True:
    hashtag = []  #put all hashtags here
    username = [] #put usernames here
    like_hashtags(hashtag)

