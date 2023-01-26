#!/usr/bin/python3
def roman_to_int(roman_string):
    s = 0
    if not isinstance(roman_string, str):
        return 0
    ro = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)-1):
        if roman_string[i] in ro:
            if ro[roman_string[i]] < ro[roman_string[i+1]]:
                s -= ro[roman_string[i]]
            else:
                s += ro[roman_string[i]]
    if roman_string[-1] in ro:
        s += ro[roman_string[-1]]
    return s
