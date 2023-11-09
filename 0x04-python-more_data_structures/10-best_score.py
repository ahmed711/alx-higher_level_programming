#!/usr/bin/python3

def best_score(a_dictionary={}):
    if a_dictionary == None:
        return None
    max_entry = (None, None)
    for key, value in a_dictionary.items():
        if max_entry[0] == None or value > max_entry[0] > 0:
            max_entry = (value, key)
    return max_entry[1]
