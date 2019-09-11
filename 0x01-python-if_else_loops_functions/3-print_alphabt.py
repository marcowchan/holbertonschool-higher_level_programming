#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if x != ord('q') and x != ord('e'):
        print("{:c}".format(x), end='')
