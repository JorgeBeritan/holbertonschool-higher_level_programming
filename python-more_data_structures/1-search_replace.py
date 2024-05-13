#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    new[search] = replace
    return new
