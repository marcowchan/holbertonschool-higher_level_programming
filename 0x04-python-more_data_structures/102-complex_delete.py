#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in filter(lambda p: p[1] == value, list(a_dictionary.items())):
            del a_dictionary[k]
    return a_dictionary
