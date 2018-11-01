#!/bin/bash

. /generate.sh

rm -rf /generate.sh

socat \
  TCP-LISTEN:1337,bind=0.0.0.0,reuseaddr,fork \
  EXEC:"/usr/local/bin/python3 /home/main.py",pty,stderr,setsid,sigint,sane,echo=0 &

while true;
    do { printf 'HTTP/1.0 200 OK\r\nContent-Length: %d\r\nContent-Disposition: attachment; filename="%s.zip"\r\n\r\n' "$(wc -c < /home/${filename}.zip)" ${filename}; cat /home/${filename}.zip; } | nc -l -p 1338;
done