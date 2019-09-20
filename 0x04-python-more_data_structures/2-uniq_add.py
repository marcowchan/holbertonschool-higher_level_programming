#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    int_set = set()
    for num in my_list:
        if num not in int_set:
            int_set.add(num)
            uniq_sum += num
    return uniq_sum
