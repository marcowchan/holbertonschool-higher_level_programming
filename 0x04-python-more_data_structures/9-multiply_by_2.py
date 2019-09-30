#!/usr/bin/python3
def times_2(num):
    return num * 2


def multiply_by_2(a_dictionary):
    return {k: times_2(v) for k, v in a_dictionary.items()}
