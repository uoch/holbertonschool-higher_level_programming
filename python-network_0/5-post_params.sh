#!/bin/bash
#cURL POST parameters
curl -s -X POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' "$1"
