#!/usr/bin/python3
def uppercase(str):
    for char in str:
        s = ord(char)
        if s >= 97 and s <= 122:
            print(chr(s - 32), end="")
        else:
            print(str)
