#!/usr/bin/python3
def uppercase(str):
    upper = 0
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upper = 32
        else:
            upper = 0
        print("{:c}".format(ord(c) - upper), end='')
    print("")
