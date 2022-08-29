#!/usr/bin/python3
def no_c(my_string):
    rem = ['C', 'c']
    new = "".join(i for i in my_string if i not in rem)
    return (new)
