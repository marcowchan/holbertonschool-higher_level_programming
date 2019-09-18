#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    arr = [0, 0]
    for i in range(2):
        if len(tuple_a) > i:
            arr[i] += tuple_a[i]
        if len(tuple_b) > i:
            arr[i] += tuple_b[i]
    return (arr[0], arr[1])
