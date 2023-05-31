#!/bin/bash
# Display the size of the response body
curl -s -v "$1" --stderr - | grep Content-Length: | cut -d' '  -f 3
