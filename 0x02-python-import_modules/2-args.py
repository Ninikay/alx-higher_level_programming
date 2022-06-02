#!/usr/bin/python3

import sys

if __name__ == "__main__":
    length = len(sys.argv)

    if length == 1:
        print("{:d} arguments.".format(length - 1))
    elif length == 2:
        print("{:d} arguments:".format(length - 1))
    else:
        print("{:d} arguments:".format(length - 1))
    for j in range(1, length):
        print("{:d}: {:s}".format(j, sys.argv[j]))
