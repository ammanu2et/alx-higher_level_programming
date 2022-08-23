#!/usr/bin/python3
def uppercase(str):
    ch = ord(str)
    if ch > 96 and ch < 123:
        print("{:c}".format(ch - 32))
    else:
        print("{:c}".format(ch))
