#!/usr/bin/python3
"""pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    rw = [1]
    tp = [0]
    m = []

    if n <= 0:
        return m
    for k in range(n):
        a.append(rw)
        rw = [a+b for a, b in zip(rw + tp, tp + rw)]
    return m
