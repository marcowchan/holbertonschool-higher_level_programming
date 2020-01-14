#!/usr/bin/python3
"""Displays the X-Request-Id response header value."""
if __name__ == "__main__":
    from sys import argv
    import requests
    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
