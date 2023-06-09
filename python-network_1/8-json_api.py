#!/usr/bin/python3
"""https://docs.python-requests.org/en/latest/api/"""
from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        resp = r.json()
        if resp == {}:
            print("No result")
        else:
            id = resp['id']
            name = resp['name']
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
