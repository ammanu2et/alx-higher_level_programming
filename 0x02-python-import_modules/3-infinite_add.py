#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv = sys.argv
    n = len(argv)
    if n == 1:
        print('{:d}'.format(n-1))
    else:
        sum = 0
        for i in argv[1:]:
            sum += int(i)
        print(sum)
