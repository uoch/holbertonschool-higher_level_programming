#!/usr/bin/python3
"""What's my status? #1"""
import urllib.request
url = 'https://intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body.decode('utf-8'))
