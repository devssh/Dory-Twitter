import tweepy
import time
import datetime
import os

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        print("streaming " + str(time.time()))
        open("data" + datetime.datetime.today().strftime('%Y-%m-%d') + ".json", "a+").write(data)

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    while(True):
      try:    
        consumer_token = os.getenv("CONSUMER_TOKEN")
        consumer_secret = os.getenv("CONSUMER_SECRET")
        access_token = os.getenv("ACCESS_TOKEN")
        access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        listener = StdOutListener()

        TweetStream = tweepy.Stream(auth=api.auth, listener=listener)

        TweetStream.filter(track=[u"python", u"java", u"clojure", u"scala", u"haskell", u"javascript", u"babel", u"apache",
                        u"nginx", u"redis", u"erlang", u"blockchain", u"golang", u"keras", u"tensorflow",
                        u"deep learning", u"elixir", u"ruby", u"lua", u"c++", u"rustacean", u"lisp"
                        ], async=True)
      except:
        pass
