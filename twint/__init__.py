from twint._methods.stream import stream
from twint._methods.flatfile import flatfile
from twint._methods.search import search
from twint._methods.timeline import timeline

__version__ = "1.2"

# module level doc-string

__doc__ = """

twint - Twitter data for signals intelligence
==============================================
**twint** is a Python package that provides a
very high level abstraction layer to Twitter
API and provides the preprocessed results in a
pandas dataframe. The system have been built with
several concerns in mind:

- availability of key scores (influence, reach, etc)
- applicability of the data for neural networks
- identification of spam and other bots
- singleline commands for all four important methods:
   - streaming API for both keywords and users
   - REST API for for keywords
   - REST API for user timelines
   - Flatfile ingestion from JSON (from Twitter API)
 - all methods return identical dataframe
"""
