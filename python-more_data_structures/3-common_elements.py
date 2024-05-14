#!/usr/bin/python3
def common_elements(set_1, set_2):
    set1 = list(set_1)
    set2 = list(set_2)
    value = []

    for i in set1:
        for i2 in set2:
            if i == i2:
                value += [i2]
    return value
