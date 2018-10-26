# Minesweeper

## Description

    TODO

## Flag

    CTF{Mouse_Right_Click_to_flag}

## Post Solution

    Animate donut from https://www.a1k0n.net/2011/07/20/donut-math.html
    in iframe

## Deploy

    docker run -d -p 5002:1337 ch2

## Solution

    1) binwalk minesweeper.ico
    2) Extract the binary
    3) Dump the ASM of the binary (disassemble main)
    4) Observe print_flag and donut functions next to each other
    5) Step through (ni in GDB) main until the call to donut()
    6) Step into (si in GDB) the donut function 
    7) Observe MOV of DWORD PTR [rbp-0x22b4] to edi
    8) Observe that edi is compared with 0x1
    9) Change edi register to 0 to fail CMP
    10) Continue stepping to escape to main and get the flag