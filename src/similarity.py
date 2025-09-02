# similarity.py - String similarity checks

from fuzzywuzzy import fuzz

def check_similarity(title1, title2):
    return fuzz.ratio(title1.lower(), title2.lower())
