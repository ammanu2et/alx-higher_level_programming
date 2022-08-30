#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list)
    if i < 1:
        return None
    else:
        my_list.sort()
        return my_list[-1]

my_list = []
max_value = max_integer(my_list)
print("Max: {}".format(max_value))