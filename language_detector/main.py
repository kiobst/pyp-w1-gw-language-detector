# -*- coding: utf-8 -*-

"""This is the entry point of the program."""
from languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    
    # create dictionary to store counters of words in a language
    # example --> counters = {"spanish": 29, "german": 3, "english": 0}
    counters = {}
    for language in LANGUAGES:
        counters[language["name"]] = 0
    
    # iterate through each word in text, 
    # compare to common words in each dictionary
    # if it matches, then add +1 to the counter for the language
    for word in text.split():
        for language in LANGUAGES:
            name = language['name']
            commonwords = language['common_words']
            if word in commonwords:
                counters[name] += 1
    # return the highest value of all keys in the counter dictionary
    return max(counters, key=counters.get)