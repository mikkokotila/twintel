import entropy
import pandas as pd

def keywords(data):
    
    ## retweet_count

    d6 = pd.DataFrame()

    ## tweet entropy
    l = []
    for i in range(len(data.text)):
        l.append(entropy.shannon_entropy(data.text[i]))

    d6['tweet_entropy'] = pd.Series(l)

    ## number of words in tweet
    l = []
    for i in range(len(data.text)):
        l.append(len(pd.Series(data.text[i].split())))

    d6['no_of_words'] = pd.Series(l)

    ## % of unique words in the tweet                
    l = []
    for i in range(len(data.text)):

        l.append(len(data.text[i]))

    d6['tweet_length'] = pd.Series(l)

    d6x = pd.DataFrame({
                        'sum' : d6.sum().astype('int'),
                        'median' : d6.median(),
                        'mean' : d6.mean(),
                        'std' : d6.std()})

    d6x = d6x.round(decimals=3)
    
    del d6
    
    return d6x