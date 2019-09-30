#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev = 0
    integer = 0
    for c in roman_string:
        if num[c] > prev:
            integer += num[c] - prev - prev
            prev = num[c]
        else:
            integer += num[c]
            prev = num[c]
    return integer
