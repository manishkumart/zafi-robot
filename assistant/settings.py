"""
SeTtINgs
"""

# built-in
import logging

# keyword for waking up
KEYWORD = "zafi"

# sst/tts language used for recognizing
# (at the moment only en-US is avilable)
# language you want to speak and get answered in
LANGUAGE = "en-US"
# first two letters of language
LANGUAGE_SHORT = LANGUAGE[:2]

# location used for weather requests and more
LOCATION = "india"
# openweatherapi key from their site
# (neccesary for weather requests)
WEATHER_API_KEY = "d22edf5137dd00bc87463abbef20e6c6"


# the stt speech engine used to recognize audio
# (at the moment only google available)
STT_ENGINE = "google"

# the tts engine used to reply
# (NOT used at the moment: auto-detect)
TTS_ENGINE = ""
# subtitles
# set to 'false' if you don't want to print every tts output to console
TTS_SUBTITLE = True
# set to false to deactivate auto OS detection for tts engine
# (you will need to use the python library gTTS)
TTS_AUTODETECT = True

# os used for specific raspberry pi software
# (NOT used at the moment: auto-detect)
OPERATING_SYSTEM = ""

# activation sound path on keyword
ACTIVATION_SOUND_PATH = "assistant/data/files/sound/activation.mp3"

# phrases file path for matching
PHRASES_FILE_PATH = "assistant/data/files/json/phrases.json"
# replies file path for replying
REPLIES_FILE_PATH = "assistant/data/files/json/replies.json"

# news ticks
# (how man titles from the news page)
MAX_NEWS_TICKS = 4

# energy threshold for manual ambient
# noise adaption
SR_ENERGY_THRESHOLD = 200

# logger definitions
LOGGER_NAME = "zafi"
LOGGER_LEVEL = logging.DEBUG
