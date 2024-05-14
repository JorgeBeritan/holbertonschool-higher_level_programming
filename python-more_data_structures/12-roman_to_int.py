#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    traduced = 0
    char_prev = 0
    for char in roman_string:
        if char in roman:
            traduced += roman[char]
            if roman[char] > char_prev:
                traduced -= char_prev * 2
            char_prev = roman[char]
        else:
            return 0

    return traduced
