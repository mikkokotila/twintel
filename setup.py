#! /usr/bin/env python

import os

DESCRIPTION = "Twitter data for signals intelligence"
LONG_DESCRIPTION = """\

twintel - Twitter data for signals intelligence
==============================================
**twintel** is a Python package that provides a
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

DISTNAME = 'twintel'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://github.com/mikkokotila'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/mikkokotila/twintel'
VERSION = '1.4.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup


install_requires = ['pandas',
                    'nltk',
                    'tweepy',
                    'twython',
                    'aiohttp_socks']

if __name__ == "__main__":

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          setup_requires=['nltk'],
          install_requires=install_requires,
          packages=['twintel',
                    'twintel._methods',
                    'twintel._resources',
                    'twintel._processing'],
                    
          classifiers=[
                     'Intended Audience :: Science/Research',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Operating System :: MacOS'],
          )
    os.system('pip install nltk')
    os.system('python -m nltk.downloader vader_lexicon')
