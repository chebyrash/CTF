## Cluttered File System

## Description

    You decided to explore the file system, but there is so much garbage
    Let's see if you can find - not an executable, but a file 29 bytes long

## Flag

    CTF{Clippy_Office_Assistant}

## Post Solution

    Show the clippy assistant memes

## Deploy

    docker build -t challenge_3 .
    docker run -d -p 5003:1337 challenge_3

## Solution

    1) ls -la to find hidden folder
    2) cd into .hidden
    3) ls to list folders
    4) cd into - by specifying path ./- or full
    5) Use find . -type f ! -executable -size 29c