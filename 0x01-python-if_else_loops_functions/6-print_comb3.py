#!/usr/bin/python3
a = 0
while a < 10:
    b = 0
    while b < 10:
        if (a != b and a < b):
            print("{0:d}{1:d}".format(a, b), end="")
            if (a >= 8 and b >= 9):
                print()
            else:
                print(end=", ")
        b += 1
    a += 1
