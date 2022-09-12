#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    p = 0
    try:
        for n in range(x):
            print("{}".format(my_list[n]), end="")
    except:
        break
    else:
        p += 1
    print()
    return p
