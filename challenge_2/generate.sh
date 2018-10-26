#!/bin/bash

cd home/ && ./compile.sh && rm -rf minesweeper.c compile.sh

cat minesweeper >> mine.ico

rm -rf minesweeper

export filename=$(env LC_CTYPE=C tr -dc "A-Z0-9" < /dev/urandom | head -c 16 | xargs)

zip -r ${filename} mine.ico && rm -rf mine.ico