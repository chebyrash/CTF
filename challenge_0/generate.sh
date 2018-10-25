#!/bin/bash

flag="CTF{Welcome_to_Microsoft_Windows}"

encoded_flag=$(echo ${flag} | base64)

exiftool -Comment=${encoded_flag} home/img && rm -rf home/*original

export filename=$(env LC_CTYPE=C tr -dc "A-Z0-9" < /dev/urandom | head -c 16 | xargs)

cd home/ && zip -r ${filename} img && rm -rf img