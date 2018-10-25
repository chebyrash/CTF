#!/bin/bash

. /generate.sh

rm -rf /generate.sh

while true;
    do { printf 'HTTP/1.0 200 OK\r\nContent-Length: %d\r\nContent-Disposition: attachment; filename="%s.zip"\r\n\r\n' "$(wc -c < /home/${filename}.zip)" ${filename}; cat /home/${filename}.zip; } | nc -l -p 1337;
done