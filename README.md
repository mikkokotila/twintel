# twint | signals intelligence taxonomy from Twitter API 

### Installation 

    pip install git+

### Use Examples

#### Gets 500 'deep learning' tweets 

    search('deep learning',500)
    
#### Get the timeline of Donald Trump
    
    timeline('realdonaldtrump')
    
#### Opens a stream for keyword cars (very high volume)

    stream('cars')
    
#### Ingest a JSON file resulting from stream()
    
    flatfile()
