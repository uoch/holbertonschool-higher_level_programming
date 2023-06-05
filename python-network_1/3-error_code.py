#!/usr/bin/python3
"""POST an email #0."""
import urllib.request
import urllib.error
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:{}'.format(response.status()))
