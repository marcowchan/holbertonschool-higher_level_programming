#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda ele: replace if ele == search else ele, my_list))
