#!/usr/bin/python3
def remove_char_at(str, n):
    r_str = ""
    for i in range(0, len(str)):
        if i != n:
            r_str = r_str + str[i]
    print(r_str, end="")
