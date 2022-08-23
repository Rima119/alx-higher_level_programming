#!/usr/bin/python3
for n in range(10):
    for m in range(n + 1, 10):
        print("{:d}{:d}".format(n, m), end=", ")
        if n == 8 and m == 9:
            print("{:d}{:d}".format(n, m))
