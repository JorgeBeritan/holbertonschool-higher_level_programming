#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i, value in enumerate(new):
        if value == search:
            new[i] = replace
    return new
