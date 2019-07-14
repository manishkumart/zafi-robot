# core / core modules packages
from assistant.core.modules import tts
from assistant.core.packages import googlesearch

"""
Google
try to find a result
from Google Search
"""
def ex(input):
    search_this = input.replace("otto ", "")

    # try to get a result from google search
    result = googlesearch.Search.get(search_this)

    tts.say(result)