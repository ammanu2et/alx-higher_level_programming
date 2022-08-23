#!/usr/bin/python3
def uppercase(str):
    for char in str:
        s = ord(char)
        if s > 96 and s < 123:
            s = s - 32
        print("{0:c}".format(s), end="")
    print()
