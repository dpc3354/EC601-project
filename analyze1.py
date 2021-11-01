import os
import sys
import tweepy
import json
from google.cloud import language_v1

client = language_v1.LanguageServiceClient()

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")


def get_all_tweets(username):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    alltweets = [] 

    new_tweets = api.user_timeline(screen_name = username,count=1)

    alltweets.extend(new_tweets)
    '''
    #oldest = alltweets[-1].id - 1
    # while len(new_tweets) > 0: 
    
    #     new_tweets = api.user_timeline(screen_name = username,count=10,max_id=oldest)
        
    #     alltweets.extend(new_tweets)
        
    #     oldest = alltweets[-1].id - 1
    #     if(len(alltweets) > 15):
    #         break
    #     print("...%s tweets downloaded so far" % (len(alltweets)))
    '''

    file = open('tweet.json', 'w') 
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    file.close()

def analyze_text_entities(text):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")

def main():
    username = sys.stdin.readline()
    try:
        get_all_tweets(username)
        file = open('tweet.json','r')
        dic = json.load(file)
        text = dic['text']
        analyze_text_entities(text)
    except:
        print("Username is not existed!!")
if __name__ == '__main__':
    print("Please enter the username:")
    main()



    
