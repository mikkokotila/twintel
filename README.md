# twint | signals intelligence taxonomy from Twitter API 

**Twint** is a Python package that provides a very high level abstraction layer to Twitter API and provides the preprocessed results in a pandas dataframe. The system have been built with several key concerns in mind. 

### Key Features

- availability of key scores (influence, reach, etc)
- applicability of the data for neural networks
- identification of spam and other bots
- singleline commands for all four important methods:
   - streaming API for both keywords and users
   - REST API for for keywords
   - REST API for user timelines
   - Flatfile ingestion from JSON (from Twitter API)
 - all methods return identical dataframe

### Installation 

    pip install git+https://github.com/mikkokotila/twint.git

### Use Examples

#### Gets 500 'deep learning' tweets 

    search('deep learning',500)
    
#### Get the timeline of Donald Trump
    
    timeline('realdonaldtrump')
    
#### Opens a stream for keyword cars (very high volume)

    stream('cars')
    
#### Ingest a JSON file resulting from stream()
    
    flatfile('some_tweets.json')

### Signal Taxonomy 

SIGNAL | SOURCE  
-------|---------
influence_score | Twint
reach_score | Twint
quality_score | Twint
compound | NLTK 
neu | NLTK 
neg | NLTK 
pos | NLTK 
days_since_creation | Twitter
user_tweets | Twitter 
user_favourites | Twitter | 
user_followers | Twitter
user_following | Twitter
user_listed | Twitter
handle | Twitter
created_at | Twitter
default_profile | Twitter
egg_account | Twitter
description | Twitter
location | Twitter
timezone | Twitter
expanded_url | Twitter
url | Twitter
site_url | Twitter 
retweet_count | Twitter
text | Twitter
