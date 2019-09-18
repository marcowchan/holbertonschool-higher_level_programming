#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for n in my_list[1:]:
        if max < n:
            max = n
    return max
