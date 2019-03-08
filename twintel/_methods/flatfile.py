def flatfile(filename='somecode_tweets.json'):

    '''Flatfile Method

    WHAT: a method for converting Twitter API json
    format in to a pandas dataframe with the standard
    twint scores and other metrics.

    HOW: flatfile('some_tweets.json')

    INPUT: a json file with tweet data from Twitter API

    OUTPUT: a pandas dataframe with standard twint signals.

    '''

    import pandas as pd

    from twintel._processing.data_frame import data_frame
    from twintel._processing.data_prep import data_prep
    import gc

    with open(filename, 'r') as f:

        data = f.readlines()
        data = map(lambda x: x.rstrip(), data)
        data_json_str = "[" + ','.join(data) + "]"
        del data
        data_df = pd.read_json(data_json_str)
        del data_json_str
        t = data_df[data_df['user'].isnull() != True]
        del data_df
        t = pd.DataFrame.reset_index(t)

    f.close()

    for col in ['coordinates',
                'display_text_range',
                'display_text_range',
                'geo',
                'extended_entities',
                'timestamp_ms',
                'source',
                'quoted_status_id_str',
                'quoted_status',
                'place',
                'is_quote_status',
                'in_reply_to_user_id',
                'in_reply_to_status_id',
                'id_str',
                'favorited',
                'extended_tweet',
                'contributors',
                'truncated',
                'retweeted_status',
                'quoted_status_id',
                'in_reply_to_user_id_str',
                'in_reply_to_status_id_str',
                'in_reply_to_screen_name',
                'filter_level']:

        try:
            t.drop(col, axis=1, inplace=True)
        except KeyError:
            pass

    temp = data_prep(t)
    del t
    df = data_frame(temp)
    del temp

    gc.collect()

    return df
