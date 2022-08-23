#!/usr/bin/python3
for n in range(10):
    for m in range(n + 1, 10):
        if m == 9 and n == 8:
            print("{:d}{:d}".format(n, m))
        else:
            print("{:d}{:d}".format(n, m), end=", ") 
