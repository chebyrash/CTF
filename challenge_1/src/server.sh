#!/bin/bash

socat \
  TCP-LISTEN:1337,bind=0.0.0.0,reuseaddr,fork \
  EXEC:"/usr/bin/man mspaint",pty,stderr,setsid,sigint,sane