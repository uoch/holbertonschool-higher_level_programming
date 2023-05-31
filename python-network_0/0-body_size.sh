#!/bin/bash
# Display the size of the response body
response_headers=$(curl -s -I "$1")
content_length=$(echo "$response_headers" | awk '/Content-Length/ {print $2}' | tr -d '\r')
echo $content_length 
