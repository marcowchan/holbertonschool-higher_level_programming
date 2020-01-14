#!/usr/bin/python3
"""Handles HTTPErrors."""
if __name__ == '__main__':
    from sys import argv
    from urllib import request
    from urllib.error import HTTPError
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
    else:
        pass
