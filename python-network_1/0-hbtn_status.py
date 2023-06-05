#!/usr/bin/python3
import urllib.request
"""0. What's my status? #0
"""
url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read()

print("- Body response:")
print("\t- type:", type(body))
print("\t- content:", body)