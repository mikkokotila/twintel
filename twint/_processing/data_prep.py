import pandas as pd
import gc


def data_prep(data):

    """
    It will take about 15 seconds for 30,000 tweet objects
    when read from a .json file in the full format

    """

    c = int(len(data))

    test = [[data['user'][i]['statuses_count'],
            data['user'][i]['followers_count'],
            data['user'][i]['friends_count'],
            data['user'][i]['listed_count'],
            data['user'][i]['favourites_count'],
            data['user'][i]['screen_name'],
            data['user'][i]['created_at'],
            data['user'][i]['default_profile'],
            data['user'][i]['default_profile_image'],
            data['user'][i]['location'],
            data['user'][i]['time_zone'],
            data['user'][i]['name'],
            data['user'][i]['lang'],
            data['user'][i]['description'],
            data['entities'][i]] for i in range(c)]

    df1 = pd.DataFrame(test)
    del test
    data = data.drop('entities', axis=1)

    df1.columns = ['user.statuses_count',
                   'user.followers_count',
                   'user.friends_count',
                   'user.listed_count',
                   'user.favourites_count',
                   'user.screen_name',
                   'user.created_at',
                   'user.default_profile',
                   'user.default_profile_image',
                   'user.location',
                   'user.time_zone',
                   'user.name',
                   'user.lang',
                   'user.description',
                   'entities']

    out = pd.concat([df1, data], axis=1)
    del df1, data
    out.check = 1
    gc.collect()

    return out
