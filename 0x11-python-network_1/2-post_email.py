#!/usr/bin/python3
"""Sends a POST request."""
if __name__ == "__main__":
    from sys import argv
    from urllib import parse, request
    data = parse.urlencode({"email": argv[2]})
    data = data.encode("ascii")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
