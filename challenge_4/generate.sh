#!/bin/bash

export filename=$(env LC_CTYPE=C tr -dc "A-Z0-9" < /dev/urandom | head -c 16 | xargs)

cd home/ && zip ${filename} main.py