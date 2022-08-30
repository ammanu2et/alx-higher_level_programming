#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list)
    if i < 1:
        return None
    else:
        my_list.sort()
        return my_list[-1]
