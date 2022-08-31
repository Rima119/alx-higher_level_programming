#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for n in range(len(roman_string)):
        if (rom[roman_string[n]] > rom[roman_string[n - 1]] and n > 0):
            num += rom[roman_string[n]] - 2 * rom[roman_string[n - 1]]
        else:
            num += rom[roman_string[n]]
    return (num)
