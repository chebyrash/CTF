#!/bin/bash

flag="CTF{Photoshop_is_for_quitters}"

mkdir home/photoshop && echo ${flag} > home/photoshop/flag.txt

gzip home/mspaint.1 && cp home/mspaint.1.gz /usr/share/man/man1/

mandb

rm -rf home/mspaint.1.gz home/paint.txt && mv home/server.sh /