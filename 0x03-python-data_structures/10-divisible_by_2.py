#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for n in my_list:
        if n % 2:
            result += [False]
        else:
            result += [True]
    return result
