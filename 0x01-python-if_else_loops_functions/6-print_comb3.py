#!/usr/bin/python3
"""print different combos of 2 digits"""

for number in range(0, 10):
    for number2 in range(number+1, 10):
        if number ==8 and number2 ==9:
            print("{:d}{:d}".format(number, number2))
        else:
            print("{:d}{:d}".format(number.number2), end=", ")
