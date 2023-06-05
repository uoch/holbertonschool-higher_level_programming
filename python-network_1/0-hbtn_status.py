#!/usr/bin/python3
import urllib.request
"""0. What's my status? #0
"""
url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')


print("- Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: b'{}'".format(body))
print("\t- utf8 content:", body)