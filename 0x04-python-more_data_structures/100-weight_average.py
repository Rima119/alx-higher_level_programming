#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    r1 = 0
    r2 = 0
    for a in my_list:
        r1 += a[0] * a[1]
        r2 += a[1]
    return (r1 / r2)
