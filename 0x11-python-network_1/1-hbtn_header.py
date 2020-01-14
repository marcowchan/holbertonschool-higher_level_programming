#!/usr/bin/python3
"""Displays the X-Request-Id response header value."""
if __name__ == '__main__':
    from sys import argv
    from urllib import request
    with request.urlopen(argv[1]) as response:
        print(response.info().get('X-Request-Id'))
