def stream(items, kind="keywords", filename=''):

    """
    REQUIRED INPUTS:

    items = single keyword, single user, list of keywords, list of users
    kind = either 'user' or 'keyword' (default is 'keyword')

    You also need to set access_token, access_secret, consumer_secret
    and consumer_key (get it from http://apps.twitter.com)

    EXAMPLE SEARCH QUERIES:

    users = ['3329715436','4064981488','1345822466','21587082']
    keywords = ['hillary','trump']

    """

    from tweepy import OAuthHandler
    from tweepy import Stream
    from tweepy.streaming import StreamListener

    from twintel._resources.keys import key

    keys = key()

    if len(filename) == 0:
        filename = 'streamed_tweets.json'

    access_token = keys['token']
    access_secret = keys['token_secret']
    consumer_secret = keys['consumer_secret']
    consumer_key = keys['consumer_key']

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    class MyListener(StreamListener):

        def on_error(self, status):
            print(status)
            return True

        def on_data(self, data):
            try:
                with open(filename, 'a') as f:
                    f.write(data)
                    return True
            except BaseException as e:
                print("&quot;Error on_data: %s&quot; % str(e)")
            return True

    twitter_stream = Stream(auth, MyListener())

    if kind == 'keywords':
        twitter_stream.filter(track=items)

    if kind == 'users':
        for userid in items:
            if str(userid).isdigit() != True:
                print("These are not all user_id...the user id does not contain alphabets.")
                break
            if (len(items)) > 100:
                print("It's better to not try with more than 100 users per single stream.")
                break
            else:
                twitter_stream.filter(follow=items)
