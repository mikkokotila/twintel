def timeline(screen_name):

    import tweepy

    from twintel._processing.data_frame import data_frame
    from twintel._resources.keys import key

    keys = key()

    access_token = keys['token']
    access_secret = keys['token_secret']
    consumer_secret = keys['consumer_secret']
    consumer_key = keys['consumer_key']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name=screen_name,
                                   count=200,
                                   include_rts=1)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:

        new_tweets = api.user_timeline(screen_name=screen_name,
                                       count=200,
                                       max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1

    df = data_frame(alltweets)
    df.meta_keyword = str(screen_name)

    return df
