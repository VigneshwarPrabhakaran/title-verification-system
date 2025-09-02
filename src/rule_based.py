# rule_based.py - Basic rule-based title checks

def check_disallowed_words(title):
    disallowed = ["fake", "illegal", "banned"]
    return any(word.lower() in title.lower() for word in disallowed)
