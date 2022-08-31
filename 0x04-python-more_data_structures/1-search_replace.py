#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for n in my_list:
        if search == n:
            return replace
        else:
            return my_list
