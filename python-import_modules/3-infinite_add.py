#!/usr/bin/python3
import sys

if __name__ == "__main__":

    add = 0
    for i in sys.argv[1:]:
        add += int(i)
    print("{:d}".format(add))
