from random import randint

def key():

    di = {}

    x = randint(1, 3)

    if x == 1:
        token = "730761128951734273-F6QTnBibFat750m48yu1B6thTqWGtqj"
        token_secret = "b4u10GQurb9bqu7hteukMLdN1IMgbWdaQeHRFmyCEkdAu"
        consumer_secret = "YOFK1er2ErmL1bPLCGPdMvdQ8GNdZT3EVp1zlWWmb550fswajS"
        consumer_key = "PW0loTMtmxIJORhgpVKbAi3O7"

    elif x == 2:
        token = "730749638228115456-zVgNlOzMhhneUJhwPDLNK8LhQIH7dwJ"
        token_secret = "eb5Ul4Afk6tX4ZHqeLyKEBazc9LdijrrZzkjzCrFie3nO"
        consumer_secret = "72OPxzPfxlod3qZ5gYUFHSetOQT7PzmthCllOGHZbrXWYGzzes"
        consumer_key = "yGD26irzuYOnT3RBB5W8tHqxm"

    elif x == 3:

        token = "731718844264251392-n4NiVuKrDyCRNSVttgl9KM7QgUy9Gcx"
        token_secret = "NxGnlIa08eVgbuyh5sznphCGHuMQ3A8ES1jO2YqFIJ1zA"
        consumer_secret = "nlUQLufKwWyEHJRyVWVi3gOJ0IPIv7WtaQewQf02LFzxE7lZYn"
        consumer_key = "hhOHS09gS3blQhXK0atmdTGtw"

    di.update({'token': token,
               'token_secret': token_secret,
               'consumer_secret': consumer_secret,
               'consumer_key': consumer_key})

    return di
