# googlesuggest.py v0.1
#
# November 13th, 2018
# <heinrich.scholz@protonmail.ch>
# https://github.com/HeinrichScholz/rePysithory
#
# This Python3 script complete a sequence of words
# with the suggestions returned by  the "suggestqueries.google.com" api.
#
# It was written for educational purpose and does not implement any
# optimisation.

from urllib.parse import urlparse
from urllib.parse import urlunsplit
from urllib.parse import urlsplit
from urllib.parse import urlencode
import requests
import json
import argparse

# Parsing CLI arguments
parser		= argparse.ArgumentParser(description = "GoogleSuggest complete a ser of words with suggestions provided by suggestqueries.google.com")
parser.add_argument("words", help = "set of words to be completed")
args		= parser.parse_args()

# Keyword submitted to suggestqueries.google.com
keyword         = args.words

# URL components to be encoded as the target for GET request
scheme          = "https"
netloc          = "suggestqueries.google.com"
path            = "/complete/search"
query           = {'output':'firefox', 'hl':'fr', 'q':keyword}
fragment        = ""

# Crafting the URL
query           = urlencode(query)
url             = urlunsplit((scheme, netloc, path, query, fragment))

# Processing the GET request (using "requests" package JSON decoder)
json_data       = requests.get(url).json()
for suggestion in json_data[1]:
	print(suggestion)

