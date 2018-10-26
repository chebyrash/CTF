# MS-Paint

## Description

    You successfully logged in! Start menu brings you
    to Paint. Let's see if you can use Paint's manual
    to your advantage.
    
    nc 0.0.0.0:5001

## Flag

    CTF{Photoshop_is_for_quitters}

## Post Solution

    Embed https://jspaint.app/ in iframe 

## Deploy

    docker build -t challenge_1 .
    docker run -d -p 5001:1337 challenge_1

## Solution

    1) Netcat to the server
    
    2) Use ! in man (running less for paging) to get code execution
    
    3) Explore ~ to find /home/photoshop
    
    4) Cat flag.txt
