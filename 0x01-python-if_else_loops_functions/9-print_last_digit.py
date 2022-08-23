!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lnum = number % 10
    else:
        lnum = ((number * -1) % 10) * -1
print('{}'.format(lnum), end='')
return lnum
