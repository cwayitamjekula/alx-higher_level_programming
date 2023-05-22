#!/usr/bin/python3

def roman_to_int(roman_string):
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    if roman_string and type(roman_string) == str:
        num = 0
        for n in range(len(roman_string)):
            for i in r.keys():
                if roman_string[:] is i:
                    num = r[i]
                    return num
                if roman_string[n:n+1] is i:
                    num += r[i]
                    break
        return num
    else:
        return 0
