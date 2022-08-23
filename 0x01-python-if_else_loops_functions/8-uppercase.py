#!/usr/bin/python3
def uppercase(str):
    for char in str:
        s = ord(char)
        if s >= 97 and s <= 122:
            s = s - 32
            print("{0:i}".format(s), end="")
    print()
