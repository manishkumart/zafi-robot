# core / core modules
from assistant import settings
from assistant.core.modules import tts

"""
me info
some info
about the assistant
"""
def ex(cmd):
    tts.say("I am zhaafhe version 1.0. An AI poweered voice assistant Created by  Mr. Manish to serve people".format(settings.KEYWORD))
