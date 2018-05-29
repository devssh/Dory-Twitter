import tweepy
import time

consumer_token, consumer_secret, access_token, access_token_secret = open('tokens', 'r').read().split("\n")
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        # process stream data here
        print("streaming " + str(time.time()))
        open("data.json", "a+").write(data)

    def on_error(self, status):
        print(status)


listener = StdOutListener()
myStream = tweepy.Stream(auth=api.auth, listener=listener)

print(dir(myStream))
# myStream.sample()
myStream.filter(track=[u"python", u"java", u"clojure", u"scala", u"haskell", u"javascript", u"babel", u"apache",
                       u"nginx", u"redis", u"erlang", u"blockchain", u"golang", u"keras", u"tensorflow",
                       u"deep learning", u"elixir", u"ruby", u"lua", u"c++", u"rustacean", u"lisp"
                       ], async=True)
