#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(1, my_list[x]):
            print("{:d}".format(i), end="")
        print()
    except IndexError:
        print()
