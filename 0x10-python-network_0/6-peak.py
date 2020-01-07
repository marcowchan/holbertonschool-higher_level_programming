#!/usr/bin/python3
"""Finds a peak in a list"""


def recurse(arr, low, high, n):
    """Recursive peak finder"""
    mid = low + (high - low)//2
    if (mid == 0 or arr[mid - 1] <= arr[mid]) and\
            (mid == n - 1 or arr[mid + 1] <= arr[mid]):
        return arr[mid]
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return recurse(arr, low, mid - 1, n)
    else:
        return recurse(arr, mid + 1, high, n)


def find_peak(list_of_integers):
    """Finds a peak in a list of integers"""
    if not list_of_integers:
        return None
    return recurse(
            list_of_integers, 0,
            len(list_of_integers) - 1,
            len(list_of_integers)
        )
