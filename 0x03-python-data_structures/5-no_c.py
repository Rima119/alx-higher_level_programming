#!/usr/bin/python3
def no_c(my_string):
    ch = ""
    for s in my_string:
        if s is not 'C' and s is not 'c':
            ch = ch + s
    return ch
