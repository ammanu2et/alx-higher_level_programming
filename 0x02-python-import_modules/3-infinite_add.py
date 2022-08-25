#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv = sys.argv
    n = len(argv)
    sum = 0
    for i in range(1, n):
        if n == 1:
            print(f"{n-1:d}")
        else:
            print('{:d}'.format(sum += argv[i]))
