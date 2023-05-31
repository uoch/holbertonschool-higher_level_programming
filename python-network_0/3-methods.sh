#!/bin/bash
#displays the body of the response
curl -s -I -X OPTIONS "$1" | grep Allow:| cut -d' '  -f 2-
