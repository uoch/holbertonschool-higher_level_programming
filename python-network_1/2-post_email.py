#!/usr/bin/python3
"""POST an email #0."""
import urllib.request
from sys import argv
import urllib.parse

if __name__ == "__main__":
    values = {
        'email': argv[2]
    }
    url = argv[1]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()