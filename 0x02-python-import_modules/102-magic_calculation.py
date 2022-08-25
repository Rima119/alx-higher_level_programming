#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if (a < b):
        s = add(a, b)
        for n in range(4, 6):
            s = add(s, n)
        return s
    else:
        return sub(a, b)
