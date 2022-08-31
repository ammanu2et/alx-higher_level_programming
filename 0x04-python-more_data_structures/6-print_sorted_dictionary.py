#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items(), key=lambda x: x[1]):
        print("{} : {}".format(key, value))
