#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lnum = number % 10
else:
    lnum = ((number * -1) % 10) * -1
if lnum > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, lnum))
elif lnum == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, lnum))
else:
    print("Last digit of of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lnum))
