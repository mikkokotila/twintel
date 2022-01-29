#! /usr/bin/env python
#
# Copyright (C) 2017 Mikko Kotila

import os

DESCRIPTION = "Twitter data for signals intelligence"
LONG_DESCRIPTION = """\

twintel is a Python package that provides a
very high level abstraction layer to Twitter
API and provides the preprocessed results in a
pandas dataframe. The system have been built with
several concerns in mind:

"""

DISTNAME = 'twintel'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'http://github.com/mikkokotila'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/mikkokotila/twintel'
VERSION = '1.5.2'

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
          install_requires=install_requires,
          packages=['twintel',
                    'twintel._methods',
                    'twintel._resources',
                    'twintel._processing'],
                    
          classifiers=['Intended Audience :: Science/Research',
                       'Programming Language :: Python :: 3.7',
                       'Programming Language :: Python :: 3.8',
                       'Operating System :: POSIX',
                       'Operating System :: Unix',
                       'Operating System :: MacOS'])
      
    os.system('pip install nltk')
    os.system('python -m nltk.downloader vader_lexicon')
