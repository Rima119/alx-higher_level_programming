#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndic = {}
    for v, k in a_dictionary.items():
        ndic[k] = v * 2
    return ndic
