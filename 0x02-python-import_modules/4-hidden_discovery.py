#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    n = dir(hidden_4)
    for m in n:
        if m[:2] != '__':
            print("{:s}".format(m))
