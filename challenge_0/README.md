## Welcome

## Description

    While exploring your grandpa's attic you find
    a dusty PC. You bring it downstairs, plug it in
    and switch it on. After Windows XP loads up 
    a login prompt appears.
    The password shouldn't be that difficult to get.
    
    [Attachment](0.0.0.0:5000)

## Flag

    CTF{Welcome_to_Microsoft_Windows}

## Post Solution

    ![Welcome](welcome.jpg)

## Deploy

    docker build -t challenge_0 .
    docker run -d -p 5000:1337 challenge_0

## Solution

    1) Unzip the zip file
    
    2) Use exiftool to lookup the Comment tag
    
    3) Decode the base64 encoded string
    
    4) Extract the flag
