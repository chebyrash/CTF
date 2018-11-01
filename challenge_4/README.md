## DOS AMP

## Description

    Exploring Windows is boring wihout some music, right?
    This archaic MP3 player has a simple interface potentially riddled with bugs
    Let's see if you can manage to exploit it's internal media database

    nc 0.0.0.0 50041
    [Source code](0.0.0.0:50042)

## Flag

    CTF{First_MP3_Player_For_DOS}

## Post Solution

    Show DOSAMP ASCII logo

## Deploy

    docker build -t challenge_4 .
    docker run -d -p 50041:1337 -p 50042:1338 challenge_4

## Solution

    1) Download and inspect source code
    2) Observe raw SQL statements are escaped differently using " or '
    3) Use Add Song option to inject 'UNION SELECT flag, 1 FROM flags'
    4) Use Shuffle option to execute inserted SQL injection
    5) Copy the flag