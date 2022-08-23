#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 65:
            print(chr(ord(char) - 32))
        else:
            print(str)
