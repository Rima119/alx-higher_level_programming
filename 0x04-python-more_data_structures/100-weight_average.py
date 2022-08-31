#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    r1 = 0
    r2 = 0
    s = r1 / r2
    for a, b in my_list:
        r1 += a * b
        r2 += b
    return s
