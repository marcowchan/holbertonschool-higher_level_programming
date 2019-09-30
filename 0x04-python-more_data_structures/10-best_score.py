#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    return sorted(a_dictionary.items(), key=lambda p: p[1], reverse=True)[0][0]
