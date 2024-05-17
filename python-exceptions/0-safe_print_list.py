#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for _ in my_list:
        count += 1
    if count < x:
        return
    try:
        for i in range(x):
            print(my_list[i], end="")
        return x
    except IndexError:
        return x

