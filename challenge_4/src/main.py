#!/usr/bin/python3

import sqlite3
import random
import sys

MENU = """\
1) Add Song
2) Play Artist
3) Play Song
4) Shuffle
5) Exit"""

with open("/home/flag.txt") as fd:
    FLAG = fd.read()

with open("/home/banner.txt") as fd:
    BANNER = fd.read()

c = sqlite3.connect(":memory:").cursor()

c.execute("CREATE TABLE flags (flag text)")
c.execute("CREATE TABLE media (artist text, song text)")
c.execute(f"INSERT INTO flags VALUES ('{FLAG}')")


def my_print(s=""):
    sys.stdout.write(f"{s}\n")
    sys.stdout.flush()


def my_input():
    sys.stdout.write("> ")
    sys.stdout.flush()
    return input()


def print_playlist(query):
    my_print("== New Playlist ==")
    try:
        for i, res in enumerate(c.execute(query).fetchall()):
            my_print(f"{i + 1}: '{res[1]}' by '{res[0]}'")
    except Exception as e:
        my_print(e)
        exit(1)
    my_print()


if __name__ == "__main__":
    my_print(BANNER)

    while True:
        my_print(MENU)
        choice = my_input()

        if choice not in [str(x) for x in range(1, 6)]:
            my_print("Invalid Input")
            continue

        if choice == "1":
            my_print("Artist Name?")
            artist = my_input().replace('"', "")
            my_print("Song Name?")
            song = my_input().replace('"', "")

            try:
                c.execute(f"""INSERT INTO media VALUES ("{artist}", "{song}")""")
            except Exception as e:
                my_print(e)
                exit(1)

        elif choice == "2":
            my_print("Artist Name?")
            artist = my_input().replace("'", "")
            print_playlist(f"SELECT artist, song FROM media WHERE artist = '{artist}'")

        elif choice == "3":
            my_print("Song Name?")
            song = my_input().replace("'", "")
            print_playlist(f"SELECT artist, song FROM media WHERE song = '{song}'")

        elif choice == "4":
            artist = random.choice(list(c.execute("SELECT DISTINCT artist FROM media")))[0]
            my_print(f"Choosing songs from random artist: {artist}")
            print_playlist(f"SELECT artist, song FROM media WHERE artist = '{artist}'")

        elif choice == "5":
            my_print("Exiting")
            exit(0)
