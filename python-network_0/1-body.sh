#!/bin/bash
#displays the body of the response
curl -s -X GET -w "%{http_code}" "$1" | awk '/^200$/ {getline; print}'
