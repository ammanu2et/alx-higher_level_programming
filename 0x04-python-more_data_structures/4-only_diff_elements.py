#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    li = (set_1, set_2)
    new = set()
    for i in li:
        new = new.symmetric_difference(i)
    return new
