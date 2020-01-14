#!/usr/bin/python3
"""Queries a Star Wars API."""
if __name__ == "__main__":
    from sys import argv
    import requests
    r = requests.get("https://swapi.co/api/people/?search=" + argv[1])
    res = r.json()
    results = res.get('results')
    print("Number of results: " + str(res.get('count')))
    for r in results:
        print(r.get('name'))
