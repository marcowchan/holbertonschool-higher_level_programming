#!/usr/bin/python3
def multiple_returns(sentence):
    c = sentence[0] if len(sentence) else None
    return (len(sentence),  c)
