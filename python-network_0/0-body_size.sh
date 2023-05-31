#!/bin/bash
# Display the size of the response body
curl -s -I "$1" --stderr - | grep Content-Length: | cut -d' '  -f 3
