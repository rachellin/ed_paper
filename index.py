import tweepy
from pprint import pprint

# authorize
from settings import TWITTER_KEY, TWITTER_SECRET

consumer_key = TWITTER_KEY
consumer_secret = TWITTER_SECRET

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# 1. count # of tweets with hashtag 
# 2. 


# TODO: search query is not the same thing as hashtag - maybe i can just search fort thinspo instead because that's easier 
def tweets_from_search (query):
    '''get all tweets from search query'''
    tweet_list = []
    counter = 0
    for tweet in tweepy.Cursor(api.search_tweets, q=query, wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items():
        tweet_list.append(tweet)
        counter += 1
        print(counter)
        # counter += 1
        # if counter % 200 == 0:
        #     time.sleep(900) # rest 15 mins
        #     print("sleeping for 15 mins")
    print("mined tweets for {}".format(query))
    return tweet_list
    # just get the size of this tweet_list for the number of tweets

def getTweet (query):
    '''get a singular tweet object's json'''
    for tweet in tweepy.Cursor(api.search_tweets, q=query).items(1):
        twt_obj = tweet
    # attributes i need: place, 
    return twt_obj._json

#pprint(tweets_from_search("#thinspo"))
pprint(getTweet("#thinspo"))