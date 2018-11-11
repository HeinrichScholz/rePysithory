# googlesuggest.py v0.1
#
# November 11th, 2018
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

# Keyword submitted to suggestqueries.google.com
keyword         = input()

# URL components to be encoded as the target for GET request
scheme          = "https"
netloc          = "suggestqueries.google.com"
path            = "/complete/search"
query           = {'output':'firefox', 'hl':'fr', 'q':keyword}
fragment        = ""

# Crafting the URL
query           = urlencode(query)
url             = urlunsplit((scheme, netloc, path, query, fragment))

# Making the GET request
json_data       = requests.get(url).json()
print(json_data)
