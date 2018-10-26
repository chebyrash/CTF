# MS-Paint

# Description:

    You successfully logged in! Start menu brings you
    to Paint. Let's see if you can use Paint's manual
    to your advantage.
    
    [nc 0.0.0.0:5001](https://google.com)

# Flag:

    CTF{Photoshop_is_for_quitters}
    
# Deploy

    docker build -t challenge_1 .
    docker run -d -p 5001:1337 challenge_1
    
#Solution:

    1) Netcat to the server
    
    2) Use ! in _less_ to get code execution
    
    3) Navigate to /home/photoshop
    
    4) Cat flag.txt
