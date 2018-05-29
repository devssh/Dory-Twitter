import tweepy

consumer_token, consumer_secret, access_token, access_token_secret = open('tokens', 'r').read().split("\n")
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        # process stream data here
        print("streaming")
        open("data.txt", "a+").write(data)

    def on_error(self, status):
        print(status)


listener = StdOutListener()
myStream = tweepy.Stream(auth=api.auth, listener=listener)

print(dir(myStream))
# myStream.sample()
myStream.filter(track=[u"python"], async=True)
