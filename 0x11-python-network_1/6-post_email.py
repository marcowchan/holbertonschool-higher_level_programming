#!/usr/bin/python3
"""Sends a POST request."""
if __name__ == "__main__":
    from sys import argv
    import requests
    r = requests.post(argv[1], data={"email": argv[2]})
    print(r.text)
