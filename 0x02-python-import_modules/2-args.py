#!/usr/bin/python3
import sys
if __name__ == '__main__':
    i = 0
    if argv[i] < 1:
        print("0 arguments.")

    if argv[1]:
        print("{:d} argument:".format(len(argv)), end="")
        print("{:d} : {:s}".format(argv[i], sys.argv[i]), end="")
    else:
        print("{:d} arguments:".format(len(argv)), end="")
        print("{:d} : {:s}".format(argv[i], sys.argv[i]), end="")
