#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    arr = [0, 0]
    for i in range(len(tuple_a)):
        arr[i] += tuple_a[i]
    for i in range(len(tuple_b)):
        arr[i] += tuple_b[i]
    return (arr[0], arr[1])
