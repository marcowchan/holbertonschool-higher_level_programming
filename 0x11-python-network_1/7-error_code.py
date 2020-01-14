#!/usr/bin/python3
"""Handles HTTPErrors."""
if __name__ == "__main__":
    from sys import argv
    import requests
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
