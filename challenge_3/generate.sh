#!/bin/bash

mkdir -p /home/.hidden/- /home/.hidden/not_here && cd /home/.hidden/-

function create_file {
    filename=${1}/x${counter}/$(env LC_CTYPE=C tr -dc "A-Z0-9" < /dev/urandom | head -c 16 | xargs)
    if (( $RANDOM > 16383 )); then
        echo "not ${1} here" > ${filename}
    else
        echo "echo not ${1} here" > ${filename} && chmod +x ${filename}
    fi
}

function create_folders {
    for counter in {0..15};
        do {
            mkdir "${1}/x${counter}"
            create_file ${1}
        }
    done;
}

for counter in {0..255};
    do echo ${counter} && mkdir "x${counter}" && create_folders "x${counter}"
done;

echo "CTF{Clippy_Office_Assistant}" > "x133/x7/$(ls x133/x7/)"

cd /home