#!/bin/bash
# Display the size of the response body
curl -s -I --stderr - | grep Content-Length: | cut -d' '  -f 3

