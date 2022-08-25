#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lnum = len(argv)
    if (lnum <= 1):
        print("{:d} arguments".format(lnum - 1))
    else:
        if (lnum == 2):
            print("{:d} argument:".format(lnum - 1))
        else:
            print("{:d} arguments:".format(lnum - 1))
            for n in range(1, lnum):
                print("{:d}: {}".format(n, argv[n]))
